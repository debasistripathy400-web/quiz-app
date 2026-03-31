import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()

from quiz.models import Category, Quiz, Question, Choice

def fix_all_placeholders():
    full_data = {
        "Science": {
            "Biology: The Human Body": [
                ("What is the largest organ in the human body?", [("Skin", True), ("Liver", False), ("Brain", False), ("Heart", False)]),
                ("How many bones are in the adult human skeleton?", [("206", True), ("196", False), ("216", False), ("250", False)]),
                ("What is our body's major source of energy?", [("Carbohydrates", True), ("Proteins", False), ("Fats", False), ("Vitamins", False)]),
                ("Which organ pumps blood throughout the body?", [("Heart", True), ("Lungs", False), ("Kidney", False), ("Stomach", False)]),
                ("What is the name of the pigment that gives skin its color?", [("Melanin", True), ("Serotonin", False), ("Hemoglobin", False), ("Insulin", False)]),
                ("Which part of the eye is responsible for color vision?", [("Cones", True), ("Rods", False), ("Pupil", False), ("Iris", False)]),
                ("How many chambers are in the human heart?", [("4", True), ("2", False), ("3", False), ("5", False)]),
                ("What represents the 'building blocks of life'?", [("Cells", True), ("Atoms", False), ("Organs", False), ("Molecules", False)]),
                ("Which gas do we exhale as a waste product?", [("Carbon Dioxide", True), ("Oxygen", False), ("Nitrogen", False), ("Hydrogen", False)]),
                ("What is the main function of red blood cells?", [("Carry oxygen", True), ("Fight infection", False), ("Clot blood", False), ("Digestion", False)]),
                ("What is the brain's largest part?", [("Cerebrum", True), ("Cerebellum", False), ("Medulla", False), ("Pituitary", False)]),
                ("Which mineral is important for strong bones?", [("Calcium", True), ("Iron", False), ("Zinc", False), ("Sodium", False)]),
                ("What is the average human body temperature in Celsius?", [("37", True), ("34", False), ("40", False), ("42", False)]),
                ("What is the liquid part of blood called?", [("Plasma", True), ("Serum", False), ("Lymph", False), ("Cytoplasm", False)]),
                ("Which organ is responsible for filtering blood?", [("Kidneys", True), ("Lungs", False), ("Spleen", False), ("Liver", False)]),
                ("What is the name of the voice box?", [("Larynx", True), ("Pharynx", False), ("Esophagus", False), ("Trachea", False)]),
                ("Which vitamin is produced when skin is exposed to sunlight?", [("Vitamin D", True), ("Vitamin C", False), ("Vitamin A", False), ("Vitamin B12", False)]),
                ("What connects muscles to bones?", [("Tendons", True), ("Ligaments", False), ("Cartilage", False), ("Nerves", False)]),
                ("What is the master gland of the endocrine system?", [("Pituitary", True), ("Thyroid", False), ("Adrenal", False), ("Pancreas", False)]),
                ("What type of blood vessel carries blood away from the heart?", [("Arteries", True), ("Veins", False), ("Capillaries", False), ("Venules", False)])
            ],
            "Chemistry: Periodic Table & Elements": [
                ("What is the chemical symbol for Gold?", [("Au", True), ("Ag", False), ("Gd", False), ("Fe", False)]),
                ("Which element is the lightest?", [("Hydrogen", True), ("Helium", False), ("Lithium", False), ("Oxygen", False)]),
                ("What is the atomic number of Oxygen?", [("8", True), ("16", False), ("10", False), ("6", False)]),
                ("Which metal is liquid at room temperature?", [("Mercury", True), ("Lead", False), ("Zinc", False), ("Silver", False)]),
                ("Salt is a compound of which two elements?", [("Sodium and Chlorine", True), ("Potassium and Chlorine", False), ("Sodium and Oxygen", False), ("Calcium and Carbon", False)]),
                ("Which element is essential for organic life?", [("Carbon", True), ("Silicon", False), ("Iron", False), ("Helium", False)]),
                ("What is the most abundant gas in Earth's atmosphere?", [("Nitrogen", True), ("Oxygen", False), ("Carbon Dioxide", False), ("Argon", False)]),
                ("Which element is used in pencils?", [("Carbon (Graphite)", True), ("Lead", False), ("Silver", False), ("Iron", False)]),
                ("What is the chemical symbol for Iron?", [("Fe", True), ("Ir", False), ("In", False), ("Sn", False)]),
                ("Which group of elements are found on the far right of the table?", [("Noble Gases", True), ("Alkali Metals", False), ("Halogens", False), ("Transition Metals", False)]),
                ("What is the symbol for Silver?", [("Ag", True), ("Si", False), ("Sl", False), ("Au", False)]),
                ("Which element has the atomic number 1?", [("Hydrogen", True), ("Helium", False), ("Oxygen", False), ("Carbon", False)]),
                ("What is the heaviest naturally occurring element?", [("Uranium", True), ("Plutonium", False), ("Lead", False), ("Tungsten", False)]),
                ("Diamonds are a pure form of which element?", [("Carbon", True), ("Silicon", False), ("Sulfur", False), ("Calcium", False)]),
                ("What is the symbol for Potassium?", [("K", True), ("P", False), ("Po", False), ("Pt", False)]),
                ("Which gas is produced in the reaction between vinegar and baking soda?", [("Carbon Dioxide", True), ("Oxygen", False), ("Hydrogen", False), ("Methane", False)]),
                ("What is the atomic symbol for Copper?", [("Cu", True), ("Cp", False), ("Co", False), ("Cr", False)]),
                ("Which element is the primary component of steel?", [("Iron", True), ("Aluminium", False), ("Nickel", False), ("Copper", False)]),
                ("What is the atomic symbol for Sodium?", [("Na", True), ("S", False), ("So", False), ("Ni", False)]),
                ("Which element is known as the 'Brimstone'?", [("Sulfur", True), ("Phosphorus", False), ("Iodine", False), ("Chlorine", False)])
            ],
            "Astronomy: Exploring the Cosmos": [
                ("Which planet is known as the Red Planet?", [("Mars", True), ("Venus", False), ("Jupiter", False), ("Saturn", False)]),
                ("What is the largest planet in our solar system?", [("Jupiter", True), ("Saturn", False), ("Neptune", False), ("Uranus", False)]),
                ("Which star is at the center of our solar system?", [("The Sun", True), ("Sirius", False), ("Polaris", False), ("Proxima Centauri", False)]),
                ("What galaxy is Earth located in?", [("The Milky Way", True), ("Andromeda", False), ("Sombrero", False), ("Whirlpool", False)]),
                ("How many planets are in our solar system?", [("8", True), ("9", False), ("7", False), ("10", False)]),
                ("What is the smallest planet?", [("Mercury", True), ("Mars", False), ("Venus", False), ("Pluto", False)]),
                ("Which planet has prominent rings?", [("Saturn", True), ("Jupiter", False), ("Mars", False), ("Neptune", False)]),
                ("What is the term for a star that explodes?", [("Supernova", True), ("Nebula", False), ("Black Hole", False), ("Quasar", False)]),
                ("Which planet is closest to the Sun?", [("Mercury", True), ("Venus", False), ("Earth", False), ("Mars", False)]),
                ("What is the moon's gravity compared to Earth?", [("1/6th", True), ("1/2", False), ("1/4th", False), ("1/10th", False)]),
                ("What is the hottest planet in our solar system?", [("Venus", True), ("Mercury", False), ("Mars", False), ("Jupiter", False)]),
                ("Who was the first person to walk on the moon?", [("Neil Armstrong", True), ("Buzz Aldrin", False), ("Yuri Gagarin", False), ("John Glenn", False)]),
                ("What is a light-year a measure of?", [("Distance", True), ("Time", False), ("Speed", False), ("Brightness", False)]),
                ("Which planet is known as the Morning Star?", [("Venus", True), ("Mars", False), ("Mercury", False), ("Jupiter", False)]),
                ("What is the name of the first artificial satellite?", [("Sputnik 1", True), ("Explorer 1", False), ("Vostok 1", False), ("Apollo 11", False)]),
                ("What force keeps planets in orbit?", [("Gravity", True), ("Magnetism", False), ("Centrifugal", False), ("Nuclear", False)]),
                ("What are the icy bodies that have 'tails'?", [("Comets", True), ("Asteroids", False), ("Meteors", False), ("Moons", False)]),
                ("What is the name of Uranus's sibling planet?", [("Neptune", True), ("Saturn", False), ("Jupiter", False), ("Earth", False)]),
                ("Which planet rotates on its side?", [("Uranus", True), ("Venus", False), ("Saturn", False), ("Pluto", False)]),
                ("What is the darkest object in space?", [("Black Hole", True), ("Dark Nebula", False), ("Dead Moon", False), ("Comet", False)])
            ]
        },
        "Compiler Design": {
            "Lexical Analysis & Parsing": [
                ("What phase converts characters to tokens?", [("Lexical Analysis", True), ("Parsing", False), ("Optimization", False), ("Code Gen", False)]),
                ("What does 'AST' stand for?", [("Abstract Syntax Tree", True), ("Auto Syntax Type", False), ("Applied Semantic tool", False), ("Annual System Tier", False)]),
                ("A grammar that can produce two parse trees is?", [("Ambiguous", True), ("Context-free", False), ("Recursive", False), ("Regular", False)]),
                ("Which tool generates lexical analyzers?", [("Lex", True), ("Yacc", False), ("Bison", False), ("Make", False)]),
                ("Who proposed the hierarchy of languages?", [("Chomsky", True), ("Knuth", False), ("Hopper", False), ("Turing", False)]),
                ("What is the root of an AST?", [("Operator or keyword", True), ("Leaf", False), ("Variable", False), ("Literal", False)]),
                ("What is a lexeme?", [("Sequence of characters in source", True), ("Output token", False), ("Error message", False), ("Symbol table entry", False)]),
                ("Which parser is Top-Down?", [("Recursive Descent", True), ("LR", False), ("SLR", False), ("LALR", False)]),
                ("Which parser is Bottom-Up?", [("LR", True), ("LL", False), ("Recursive Descent", False), ("Predictive", False)]),
                ("Regular expressions describe?", [("Regular Languages", True), ("Context-free languages", False), ("Context-sensitive", False), ("Recursive", False)]),
                ("NFA can be converted to?", [("DFA", True), ("PDA", False), ("TM", False), ("LBA", False)]),
                ("What is 'Handle' in parsing?", [("A substring to be reduced", True), ("An error handler", False), ("A pointer", False), ("A stack top", False)]),
                ("Symbol table is used for?", [("Attribute management", True), ("Tokenizing", False), ("File I/O", False), ("Memory allocation", False)]),
                ("What is Semantic Analysis check?", [("Meaning and consistency", True), ("Syntax errors", False), ("Speed", False), ("Spelling", False)]),
                ("Type checking occurs in?", [("Semantic Analysis", True), ("Lexical Analysis", False), ("Parsing", False), ("Target code gen", False)]),
                ("DAG represents?", [("Directed Acyclic Graph", True), ("Data Access Gateway", False), ("Digital Array Grid", False), ("Directed Array Group", False)]),
                ("Intermediate code is for?", [("Machine independence", True), ("Speed only", False), ("Direct hardware run", False), ("Encryption", False)]),
                ("A compiler for a high level language that runs on one machine and produces code for another?", [("Cross Compiler", True), ("Multi Compiler", False), ("Incremental Compiler", False), ("One-pass Compiler", False)]),
                ("Left recursion is bad for?", [("Top-Down Parsers", True), ("Bottom-Up Parsers", False), ("Lexers", False), ("Optimizers", False)]),
                ("Parsing is also called?", [("Syntax Analysis", True), ("Source Analysis", False), ("Text Mapping", False), ("Token Sorting", False)])
            ]
        }
    }

    # Iterate over existing categories
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
    fix_all_placeholders()
