from django.core.management.base import BaseCommand
from quiz.models import Quiz, Question, Choice

class Command(BaseCommand):
    help = 'Updates Python Basics Challenge with 17 more questions and 15 min limit'

    def handle(self, *args, **kwargs):
        try:
            quiz = Quiz.objects.get(title='Python Basics Challenge')
            quiz.time_limit_minutes = 15
            quiz.save()
            self.stdout.write(self.style.SUCCESS(f'Updated time limit for {quiz.title} to 15 minutes.'))

            # New questions (starting from order 4 since 1-3 exist)
            new_questions = [
                {"q": "Which of the following is an immutable data type in Python?", "a": [("Tuple", True), ("List", False), ("Dictionary", False), ("Set", False)]},
                {"q": "How do you start a comment in Python?", "a": [("#", True), ("//", False), ("/*", False), ("<!--", False)]},
                {"q": "What is the output of 3 * '7'?", "a": [("'777'", True), ("21", False), ("Error", False), ("'21'", False)]},
                {"q": "Which function is used to get the length of a list?", "a": [("len()", True), ("length()", False), ("size()", False), ("count()", False)]},
                {"q": "What is the correct way to create a function in Python?", "a": [("def my_func():", True), ("function my_func():", False), ("create my_func():", False), ("func my_func():", False)]},
                {"q": "Which operator is used for floor division?", "a": [("//", True), ("/", False), ("%", False), ("**", False)]},
                {"q": "How do you add an element to the end of a list?", "a": [("append()", True), ("add()", False), ("insert()", False), ("push()", False)]},
                {"q": "What keyword is used for 'else if' in Python?", "a": [("elif", True), ("elseif", False), ("else if", False), ("elsif", False)]},
                {"q": "What does the 'range(5)' function generate?", "a": [("Numbers from 0 to 4", True), ("Numbers from 1 to 5", False), ("Numbers from 0 to 5", False), ("Numbers from 1 to 4", False)]},
                {"q": "Which of these is used to handle exceptions in Python?", "a": [("try...except", True), ("try...catch", False), ("do...catch", False), ("throw...catch", False)]},
                {"q": "What is the result of 2**3?", "a": [("8", True), ("6", False), ("9", False), ("5", False)]},
                {"q": "How do you convert a string to an integer in Python?", "a": [("int()", True), ("str()", False), ("float()", False), ("to_int()", False)]},
                {"q": "Which collection is ordered, changeable, and allows duplicate members?", "a": [("List", True), ("Tuple", False), ("Set", False), ("Dictionary", False)]},
                {"q": "Which method removes the last element from a list?", "a": [("pop()", True), ("remove()", False), ("delete()", False), ("discard()", False)]},
                {"q": "What is the value of 'True and False'?", "a": [("False", True), ("True", False), ("None", False), ("Error", False)]},
                {"q": "How can you return multiple values from a function?", "a": [("Return them as a tuple", True), ("Using multiple return statements", False), ("It's not possible", False), ("By using global variables", False)]},
                {"q": "What is the purpose of the 'pass' statement?", "a": [("An empty placeholder", True), ("To skip a loop", False), ("To exit a function", False), ("To throw an error", False)]},
            ]

            start_order = 4
            for i, q_data in enumerate(new_questions):
                question = Question.objects.create(
                    quiz=quiz,
                    text=q_data["q"],
                    order=start_order + i
                )
                for choice_text, is_correct in q_data["a"]:
                    Choice.objects.create(
                        question=question,
                        text=choice_text,
                        is_correct=is_correct
                    )
            
            self.stdout.write(self.style.SUCCESS(f'Added 17 new questions to {quiz.title}. Total: 20.'))

        except Quiz.DoesNotExist:
            self.stdout.write(self.style.ERROR('Quiz "Python Basics Challenge" not found.'))
