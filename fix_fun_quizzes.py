import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()

from quiz.models import Category, Quiz, Question, Choice

def fix_all_placeholders_final_v4():
    fun_quizzes = {
        "Internet Memes & Viral Trends": [
            ("Which character is associated with the 'This is Fine' meme?", [("A dog in a fire", True), ("A cat at a table", False), ("A grumpy frog", False), ("A confused turtle", False)]),
            ("What year did the 'Ice Bucket Challenge' go viral?", [("2014", True), ("2012", False), ("2016", False), ("2010", False)]),
            ("The 'Doge' meme features which breed of dog?", [("Shiba Inu", True), ("Golden Retriever", False), ("Pug", False), ("Husky", False)]),
            ("Who is the 'Grumpy Cat'?", [("Tardar Sauce", True), ("Lil Bub", False), ("Maru", False), ("Salem", False)]),
            ("What does 'YOLO' stand for?", [("You Only Live Once", True), ("You Often Lose Out", False), ("Young Ones Love Online", False), ("You Obey Law Only", False)]),
            ("Which YouTube video was the first to hit 1 billion views?", [("Gangnam Style", True), ("Baby", False), ("Despacito", False), ("See You Again", False)]),
            ("Who is famously seen 'confused' in a white suit meme?", [("John Travolta", True), ("Nicolas Cage", False), ("Tom Cruise", False), ("Leonardo DiCaprio", False)]),
            ("The 'Harlem Shake' was a viral trend in which year?", [("2013", True), ("2011", False), ("2015", False), ("2009", False)]),
            ("What is the name of the frog meme used on Reddit and 4chan?", [("Pepe the Frog", True), ("Dat Boi", False), ("Kermit", False), ("Slippy", False)]),
            ("The 'Distracted Boyfriend' meme features which profession?", [("Photographer", True), ("Chef", False), ("Doctor", False), ("Architect", False)]),
            ("Which social media platform popularized the 'Selfie'?", [("Instagram", True), ("Facebook", False), ("Twitter", False), ("Myspace", False)]),
            ("The 'Woman Yelling at a Cat' meme features a cat named?", [("Smudge", True), ("Grumpy", False), ("Lil Bub", False), ("Nala", False)]),
            ("What was the result of the 'Storm Area 51' viral event?", [("Naruto runners showed up", True), ("Aliens were found", False), ("A massive concert", False), ("Nothing happened", False)]),
            ("Which movie is the 'I'm the Captain now' meme from?", [("Captain Phillips", True), ("Titanic", False), ("Sully", False), ("Life of Pi", False)]),
            ("What is 'Rickrolling'?", [("Bait-and-switch with Rick Astley", True), ("Rolling a Rick", False), ("A type of dance", False), ("A musical game", False)]),
            ("Which game features the phrase 'Leroy Jenkins'?", [("World of Warcraft", True), ("Halo", False), ("Call of Duty", False), ("Minecraft", False)]),
            ("What was the 'Mannequin Challenge'?", [("Staying still like a mannequin", True), ("Running fast", False), ("Dressing up", False), ("Dancing", False)]),
            ("The 'Success Kid' meme features a baby on the beach with?", [("A clenched fist", True), ("A bucket", False), ("A crab", False), ("A hat", False)]),
            ("What was the 'Tide Pod Challenge'?", [("Eating laundry pods (dangerous)", True), ("Washing clothes fast", False), ("A dance", False), ("A photo trend", False)]),
            ("Who was the star of the 'Old Spice' viral commercials?", [("Isaiah Mustafa", True), ("Terry Crews", True), ("Will Smith", False), ("The Rock", False)])
        ],
        "Classic Board Games & Puzzles": [
            ("How many squares are on a standard chessboard?", [("64", True), ("48", False), ("81", False), ("100", False)]),
            ("In Monopoly, what is the most expensive property?", [("Boardwalk / Mayfair", True), ("Park Place", False), ("Reading Railroad", False), ("Illinois Avenue", False)]),
            ("How many tiles are in a standard Scrabble set?", [("100", True), ("120", False), ("80", False), ("150", False)]),
            ("Which classic game involves suspects, weapons, and rooms?", [("Clue / Cluedo", True), ("Risk", False), ("Battleship", False), ("Sorry!", False)]),
            ("What color is the 2,000-point piece in Trivial Pursuit?", [("Purple", False), ("Blue", False), ("Orange", False), ("None (Wound pie)", True)]),
            ("How many colors are on a Rubik's Cube?", [("6", True), ("4", False), ("8", False), ("9", False)]),
            ("Which game features the phrase 'You sunk my battleship!'?", [("Battleship", True), ("Risk", False), ("Connect Four", False), ("Stratego", False)]),
            ("In Chess, which piece can only move diagonally?", [("Bishop", True), ("Knight", False), ("Rook", False), ("Queen", False)]),
            ("What is the total number of dots on a pair of dice?", [("42", True), ("21", False), ("36", False), ("48", False)]),
            ("Which puzzle features numbers and a 9x9 grid?", [("Sudoku", True), ("Crossword", False), ("Word Search", False), ("Jigsaw", False)]),
            ("Who invented the Rubik's Cube?", [("Erno Rubik", True), ("Nikola Tesla", False), ("Elon Musk", False), ("Steve Jobs", False)]),
            ("In Scrabble, which two letters are worth 10 points?", [("Q and Z", True), ("X and J", False), ("K and W", False), ("Y and V", False)]),
            ("How many players are in a standard game of Bridge?", [("4", True), ("2", False), ("3", False), ("6", False)]),
            ("Which game objective is to 'capture the flag'?", [("Stratego", True), ("Risk", False), ("Checkers", False), ("Backgammon", False)]),
            ("What is the name of the 'Free' space in Bingo?", [("Center space", True), ("Corner", False), ("Zero", False), ("Jackpot", False)]),
            ("Which game is played with a set of 28 tiles?", [("Dominoes", True), ("Mahjong", False), ("Jenga", False), ("Uno", False)]),
            ("In the game of Risk, which continent is the hardest to conquer?", [("Asia", True), ("Europe", False), ("Africa", False), ("Australia", False)]),
            ("What is the total number of cards in a standard deck?", [("52", True), ("54", False), ("50", False), ("48", False)]),
            ("Which game involves pulling wooden blocks from a tower?", [("Jenga", True), ("Kerplunk", False), ("Connect Four", False), ("Mouse Trap", False)]),
            ("In backgammon, how many checkers does each player have?", [("15", True), ("10", False), ("12", False), ("20", False)])
        ],
        "Food & Cuisine Around the Globe": [
            ("Which country is famous for the dish 'Sushi'?", [("Japan", True), ("China", False), ("Thailand", False), ("Korea", False)]),
            ("What is the main ingredient of 'Guacamole'?", [("Avocado", True), ("Tomato", False), ("Onion", False), ("Chili", False)]),
            ("Where did 'Pizza' originate?", [("Italy", True), ("USA", False), ("Greece", False), ("France", False)]),
            ("Which spice is known as 'Red Gold'?", [("Saffron", True), ("Paprika", False), ("Cinnamon", False), ("Turmeric", False)]),
            ("What is the national dish of England?", [("Chicken Tikka Masala", True), ("Fish and Chips", False), ("Roast Beef", False), ("Pudding", False)]),
            ("Which fruit is known as the 'King of Fruits' and has a strong smell?", [("Durian", True), ("Mango", False), ("Jackfruit", False), ("Pineapple", False)]),
            ("What is 'Hummus' made from?", [("Chickpeas", True), ("Lentils", False), ("Beans", False), ("Pease", False)]),
            ("Which country produces the most coffee?", [("Brazil", True), ("Vietnam", False), ("Ethiopia", False), ("Colombia", False)]),
            ("What is the name of the traditional French soup made with onions?", [("French Onion Soup", True), ("Bouillabaisse", False), ("Consomme", False), ("Bisque", False)]),
            ("Which cheese is traditionally used on a classic Margherita pizza?", [("Mozzarella", True), ("Cheddar", False), ("Parmesan", False), ("Feta", False)]),
            ("What is 'Kimchi'?", [("Fermented vegetables (Korea)", True), ("Japanese soup", False), ("Indian bread", False), ("Mexican wrap", False)]),
            ("Which country is the origin of the 'Taco'?", [("Mexico", True), ("Spain", False), ("Peru", False), ("Brazil", False)]),
            ("What is the main ingredient in 'Risotto'?", [("Rice", True), ("Pasta", False), ("Quinoa", False), ("Bulgur", False)]),
            ("Which nut is used to make Marzipan?", [("Almonds", True), ("Walnuts", False), ("Pistachios", False), ("Hazelnuts", False)]),
            ("What is the name of the Japanese horseradish often served with sushi?", [("Wasabi", True), ("Ginger", False), ("Soy", False), ("Miso", False)]),
            ("Which country is associated with 'Poutine'?", [("Canada", True), ("Belgium", False), ("France", False), ("USA", False)]),
            ("What is the primary ingredient in a 'Meringue'?", [("Egg whites", True), ("Butter", False), ("Cream", False), ("Flour", False)]),
            ("Which Greek dip is made from yogurt and cucumber?", [("Tzatziki", True), ("Hummus", False), ("Baba Ganoush", False), ("Taramasalata", False)]),
            ("What is 'Baklava'?", [("Middle Eastern sweet pastry", True), ("Indian curry", False), ("Turkish coffee", False), ("Greek salad", False)]),
            ("Which country is famous for its 'Stroopwafels'?", [("Netherlands", True), ("Belgium", False), ("Germany", False), ("Denmark", False)])
        ]
    }

    for quiz_title, questions in fun_quizzes.items():
        try:
            quiz = Quiz.objects.get(title=quiz_title)
            quiz.questions.all().delete()
            print(f"Fixing quiz: {quiz_title}")
            for i, (q_text, choices) in enumerate(questions):
                question = Question.objects.create(quiz=quiz, text=q_text, order=i)
                for choice_text, is_correct in choices:
                    Choice.objects.create(question=question, text=choice_text, is_correct=is_correct)
            print(f"Successfully fixed all questions for {quiz_title}")
        except Quiz.DoesNotExist:
            print(f"Quiz {quiz_title} not found.")

if __name__ == "__main__":
    fix_all_placeholders_final_v4()
