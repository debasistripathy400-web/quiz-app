from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import login
from .models import Category, Quiz, Question, Choice, Attempt

class HomeView(ListView):
    model = Category
    template_name = 'quiz/home.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_quizzes'] = Quiz.objects.order_by('-created_at')[:5]
        return context

class QuizDetailView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quiz/quiz_detail.html'
    context_object_name = 'quiz'

class CategoryDetailView(ListView):
    model = Quiz
    template_name = 'quiz/category_detail.html'
    context_object_name = 'quizzes'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs['pk'])
        return Quiz.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context

class QuizTakingView(LoginRequiredMixin, View):
    def get(self, request, slug):
        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.questions.all()
        return render(request, 'quiz/quiz_take.html', {'quiz': quiz, 'questions': questions})

    def post(self, request, slug):
        quiz = get_object_or_404(Quiz, slug=slug)
        questions = quiz.questions.all()
        score = 0
        total_questions = questions.count()

        for question in questions:
            selected_choice_id = request.POST.get(f'question_{question.id}')
            if selected_choice_id:
                try:
                    choice = Choice.objects.get(id=selected_choice_id, question=question)
                    if choice.is_correct:
                        score += 1
                except Choice.DoesNotExist:
                    pass

        final_score = (score / total_questions) * 100 if total_questions > 0 else 0
        attempt = Attempt.objects.create(
            user=request.user,
            quiz=quiz,
            score=final_score,
            correct_answers=score,
            total_questions=total_questions
        )
        
        # Save individual answers
        for q_id, c_id in answers.items():
            try:
                question = Question.objects.get(id=q_id)
                choice = Choice.objects.get(id=c_id)
                UserAnswer.objects.create(
                    attempt=attempt,
                    question=question,
                    selected_choice=choice
                )
            except (Question.DoesNotExist, Choice.DoesNotExist):
                continue
        
        request.session['last_score'] = final_score
        return redirect('quiz_result', slug=quiz.slug)

class ResultView(LoginRequiredMixin, DetailView):
    model = Quiz
    template_name = 'quiz/result.html'
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        score = self.request.session.get('last_score', 0)
        context['score'] = score
        # Calculate SVG dash offset: circumference is ~590
        # Formula: 590 * (1 - score/100)
        context['progress_offset'] = 590 * (1 - (score / 100))
        return context

class UserHistoryView(LoginRequiredMixin, ListView):
    model = Attempt
    template_name = 'quiz/history.html'
    context_object_name = 'attempts'

    def get_queryset(self):
        return Attempt.objects.filter(user=self.request.user).order_by('-completed_at')

@login_required
def attempt_detail(request, pk):
    attempt = get_object_or_404(Attempt, pk=pk, user=request.user)
    u_ans = {ua.question_id: ua.selected_choice_id for ua in attempt.user_answers.all()}
    
    questions_data = []
    for question in attempt.quiz.questions.all():
        sel_id = u_ans.get(question.id)
        questions_data.append({
            'question': question,
            'choices': question.choices.all(),
            'selected_choice_id': sel_id
        })

    return render(request, 'quiz/attempt_detail.html', {
        'attempt': attempt,
        'questions_data': questions_data
    })

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
