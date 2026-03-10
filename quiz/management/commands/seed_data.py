from django.core.management.base import BaseCommand
from quiz.models import Category, Quiz, Question, Choice
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with initial quiz data'

    def handle(self, *args, **kwargs):
        # Create Categories
        prog, _ = Category.objects.get_or_create(
            name='Programming', 
            description='Test your coding knowledge across various languages.',
            icon_class='fas fa-code'
        )
        gen, _ = Category.objects.get_or_create(
            name='General Knowledge', 
            description='A mix of geography, history, and science.',
            icon_class='fas fa-globe'
        )

        # Create a Quiz
        quiz_title = 'Python Basics Challenge'
        quiz, created = Quiz.objects.get_or_create(
            category=prog,
            title=quiz_title,
            defaults={
                'description': 'A quick test on Python fundamental concepts.',
                'time_limit_minutes': 5,
                'slug': slugify(quiz_title)
            }
        )

        if created:
            # Questions
            q1 = Question.objects.create(quiz=quiz, text='What is the correct file extension for Python files?', order=1)
            Choice.objects.create(question=q1, text='.py', is_correct=True)
            Choice.objects.create(question=q1, text='.python', is_correct=False)
            Choice.objects.create(question=q1, text='.pyt', is_correct=False)
            Choice.objects.create(question=q1, text='.pt', is_correct=False)

            q2 = Question.objects.create(quiz=quiz, text='Which of the following is used to define a block of code in Python?', order=2)
            Choice.objects.create(question=q2, text='Curly braces', is_correct=False)
            Choice.objects.create(question=q2, text='Indentation', is_correct=True)
            Choice.objects.create(question=q2, text='Parentheses', is_correct=False)
            Choice.objects.create(question=q2, text='Square brackets', is_correct=False)

            q3 = Question.objects.create(quiz=quiz, text='How do you create a variable with the numeric value 5?', order=3)
            Choice.objects.create(question=q3, text='x = 5', is_correct=True)
            Choice.objects.create(question=q3, text='x = "5"', is_correct=False)
            Choice.objects.create(question=q3, text='int x = 5', is_correct=False)
            Choice.objects.create(question=q3, text='var x = 5', is_correct=False)

            self.stdout.write(self.style.SUCCESS('Successfully seeded quiz data'))
        else:
            self.stdout.write(self.style.WARNING('Quiz data already exists'))
