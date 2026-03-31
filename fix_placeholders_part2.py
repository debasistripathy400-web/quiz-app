import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()

from quiz.models import Category, Quiz, Question, Choice

def fix_more_placeholders():
    full_data = {
        "Psychology": {
            "Social Behavior & Influence": [
                ("Who conducted the famous prison experiment at Stanford?", [("Philip Zimbardo", True), ("Stanley Milgram", False), ("Asch Solomon", False), ("Bandura", False)]),
                ("What is the bystander effect?", [("Diffusion of responsibility", True), ("Direct intervention", False), ("Groupthink", False), ("Prejudice", False)]),
                ("Milgram's experiment focused on?", [("Obedience to authority", True), ("Conformity", False), ("Memory", False), ("Conditioning", False)]),
                ("What is Groupthink?", [("Desire for harmony over logic", True), ("Competitive discussion", False), ("Shared data", False), ("Brainstorming", False)]),
                ("Cognitive Dissonance refers to?", [("Conflicting beliefs", True), ("Mental harmony", False), ("Memory loss", False), ("Logic errors", False)]),
                ("What is the halo effect?", [("One trait influencing overall rating", True), ("Positive vibes only", False), ("A saintly attitude", False), ("Visual distortion", False)]),
                ("The Zimbardo study showed?", [("Power of the situation", True), ("Genetic behavior", False), ("Intelligence differences", False), ("Emotional stability", False)]),
                ("Who studied conformity with vertical lines?", [("Solomon Asch", True), ("Milgram", False), ("Seligman", False), ("Maslow", False)]),
                ("What is prosocial behavior?", [("Altruism and helping others", True), ("Anti-social behavior", False), ("Marketing", False), ("Public speaking", False)]),
                ("Social loafing is?", [("Doing less in a group", True), ("Sleeping in class", False), ("Networking", False), ("Relaxing alone", False)]),
                ("What is deindividuation?", [("Loss of self-awareness in groups", True), ("Forming a unique identity", False), ("Depression", False), ("Loneliness", False)]),
                ("Stereotypes are?", [("Generalized beliefs", True), ("Factual data", False), ("Scientific laws", False), ("Individual traits", False)]),
                ("Prejudice is usually associated with?", [("Negative attitudes", True), ("Positive reinforcement", False), ("Neutral data", False), ("Logic", False)]),
                ("Aggression is influenced by?", [("Both biology & environment", True), ("Genetics only", False), ("Climate only", False), ("Diet only", False)]),
                ("The 'Fundamental Attribution Error' is?", [("Overestimating traits over situation", True), ("Logical math errors", False), ("Typing mistakes", False), ("False memories", False)]),
                ("The Chameleon Effect is?", [("Mimicking others unconsciously", True), ("Changing colors", False), ("Selfishness", False), ("Isolation", False)]),
                ("Interpersonal attraction is often based on?", [("Similarity", True), ("Opposition", False), ("Randomness", False), ("Wealth only", False)]),
                ("What is reciprocity?", [("Responding to actions with similar actions", True), ("Giving up easily", False), ("Ignoring favors", False), ("Competition", False)]),
                ("Self-serving bias is?", [("Attributing success internally, failure externally", True), ("Greed", False), ("Being humble", False), ("Helping yourself last", False)]),
                ("What is the foot-in-the-door technique?", [("Small request leading to large", True), ("Bargaining", False), ("Aggressive sales", False), ("Lockpicking", False)])
            ]
        },
        "Sports": {
            "Cricket & Football History": [
                ("Who scored the first 100 in International Cricket?", [("Charles Bannerman", True), ("W.G. Grace", False), ("Don Bradman", False), ("Jack Hobbs", False)]),
                ("Which country won the 1966 FIFA World Cup?", [("England", True), ("West Germany", False), ("Brazil", False), ("Portugal", False)]),
                ("Pele is from which country?", [("Brazil", True), ("Argentina", False), ("Portugal", False), ("Spain", False)]),
                ("Who is the 'King of Cricket'?", [("Virat Kohli", True), ("Viv Richards", False), ("Sachin Tendulkar", False), ("Ian Botham", False)]),
                ("What is the length of a cricket pitch?", [("22 yards", True), ("20 yards", False), ("25 yards", False), ("30 yards", False)]),
                ("Which footballer has won the most Ballon d'Or awards?", [("Lionel Messi", True), ("Cristiano Ronaldo", False), ("Johan Cruyff", False), ("Michel Platini", False)]),
                ("Where is the 'Home of Cricket'?", [("Lord's", True), ("MCG", False), ("The Oval", False), ("Eden Gardens", False)]),
                ("In which year was the first FIFA World Cup held?", [("1930", True), ("1920", False), ("1940", False), ("1950", False)]),
                ("Which country has won the most FIFA World Cups?", [("Brazil", True), ("Italy", False), ("Germany", False), ("Argentina", False)]),
                ("Who is the leading wicket-taker in Test Cricket?", [("Muttiah Muralitharan", True), ("Shane Warne", False), ("James Anderson", False), ("Anil Kumble", False)]),
                ("What is a 'Hat-trick' in cricket?", [("3 wickets in 3 balls", True), ("6 sixes in an over", False), ("100 runs in an hour", False), ("A diving catch", False)]),
                ("Who won the 2022 FIFA World Cup?", [("Argentina", True), ("France", False), ("Croatia", False), ("Morocco", False)]),
                ("What is 'LBW' in cricket?", [("Leg Before Wicket", True), ("Long Ball Walk", False), ("Low Bowler Win", False), ("Legal Boundary Wait", False)]),
                ("Diego Maradona scored the 'Hand of God' goal against?", [("England", True), ("Italy", False), ("Belgium", False), ("West Germany", False)]),
                ("How many players are on a soccer team on the field?", [("11", True), ("10", False), ("12", False), ("9", False)]),
                ("Who is known as the 'Hitman' in cricket?", [("Rohit Sharma", True), ("Chris Gayle", False), ("David Warner", False), ("MS Dhoni", False)]),
                ("What is 'Offside' in football?", [("Positioning rule", True), ("Foul on keeper", False), ("Handling ball", False), ("A type of kick", False)]),
                ("Who is the highest run-scorer in a single Test innings?", [("Brian Lara", True), ("Matthew Hayden", False), ("Virender Sehwag", False), ("Don Bradman", False)]),
                ("Which club has won the most UEFA Champions League titles?", [("Real Madrid", True), ("AC Milan", False), ("Bayern Munich", False), ("Liverpool", False)]),
                ("What is the duration of a standard football match (excluding injury time)?", [("90 minutes", True), ("60 minutes", False), ("100 minutes", False), ("80 minutes", False)])
            ]
        }
    }

    for cat_name, quizzes in full_data.items():
        try:
            category = Category.objects.get(name=cat_name)
            for quiz_title, questions in quizzes.items():
                try:
                    quiz = Quiz.objects.get(category=category, title=quiz_title)
                    quiz.questions.all().delete()
                    print(f"Fixing quiz: {quiz_title}")
                    for i, (q_text, choices) in enumerate(questions):
                        question = Question.objects.create(quiz=quiz, text=q_text, order=i)
                        for choice_text, is_correct in choices:
                            Choice.objects.create(question=question, text=choice_text, is_correct=is_correct)
                    print(f"Successfully fixed {len(questions)} questions for {quiz_title}")
                except Quiz.DoesNotExist:
                    print(f"Quiz {quiz_title} not found.")
        except Category.DoesNotExist:
            print(f"Category {cat_name} not found.")

if __name__ == "__main__":
    fix_more_placeholders()
