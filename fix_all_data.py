import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()

from quiz.models import Category, Quiz, Question, Choice

def fix_all_placeholders_final():
    full_data = {
        "Science": {
            "Biology: The Human Body": [
                ("What is the largest organ in the human body?", [("Skin", True), ("Liver", False), ("Brain", False), ("Heart", False)]),
                ("How many bones are in the adult human skeleton?", [("206", True), ("196", False), ("216", False), ("250", False)]),
                ("What is the major source of energy?", [("Carbohydrates", True), ("Proteins", False), ("Fats", False), ("Vitamins", False)]),
                ("Which organ pumps blood throughout the body?", [("Heart", True), ("Lungs", False), ("Kidney", False), ("Stomach", False)]),
                ("Melanin gives what its color?", [("Skin", True), ("Serotonin", False), ("Hemoglobin", False), ("Insulin", False)]),
                ("Which part of the eye is for color vision?", [("Cones", True), ("Rods", False), ("Pupil", False), ("Iris", False)]),
                ("Human heart chambers?", [("4", True), ("2", False), ("3", False), ("5", False)]),
                ("Building blocks of life?", [("Cells", True), ("Atoms", False), ("Organs", False), ("Molecules", False)]),
                ("Exhale as waste gas?", [("CO2", True), ("Oxygen", False), ("Nitrogen", False), ("Hydrogen", False)]),
                ("Red blood cells function?", [("Carry oxygen", True), ("Fight infection", False), ("Clot blood", False), ("Digestion", False)]),
                ("Brain's largest part?", [("Cerebrum", True), ("Cerebellum", False), ("Medulla", False), ("Pituitary", False)]),
                ("Mineral for strong bones?", [("Calcium", True), ("Iron", False), ("Zinc", False), ("Sodium", False)]),
                ("Average body temp (Celsius)?", [("37", True), ("34", False), ("40", False), ("42", False)]),
                ("Liquid part of blood?", [("Plasma", True), ("Serum", False), ("Lymph", False), ("Cytoplasm", False)]),
                ("Filters blood?", [("Kidneys", True), ("Lungs", False), ("Spleen", False), ("Liver", False)]),
                ("Voice box name?", [("Larynx", True), ("Pharynx", False), ("Esophagus", False), ("Trachea", False)]),
                ("Vitamin from sunlight?", [("Vitamin D", True), ("Vitamin C", False), ("Vitamin A", False), ("Vitamin B12", False)]),
                ("Connects muscle to bone?", [("Tendons", True), ("Ligaments", False), ("Cartilage", False), ("Nerves", False)]),
                ("Master gland?", [("Pituitary", True), ("Thyroid", False), ("Adrenal", False), ("Pancreas", False)]),
                ("Blood vessel away from heart?", [("Arteries", True), ("Veins", False), ("Capillaries", False), ("Venules", False)])
            ],
            "Chemistry: Periodic Table & Elements": [
                ("Symbol for Gold?", [("Au", True), ("Ag", False), ("Gd", False), ("Fe", False)]),
                ("Lightest element?", [("Hydrogen", True), ("Helium", False), ("Lithium", False), ("Oxygen", False)]),
                ("Atomic number of Oxygen?", [("8", True), ("16", False), ("10", False), ("6", False)]),
                ("Liquid metal at room temp?", [("Mercury", True), ("Lead", False), ("Zinc", False), ("Silver", False)]),
                ("Salt components?", [("Na + Cl", True), ("K + Cl", False), ("Na + O", False), ("Ca + C", False)]),
                ("Organic life element?", [("Carbon", True), ("Silicon", False), ("Iron", False), ("Helium", False)]),
                ("Most abundant gas in atmosphere?", [("Nitrogen", True), ("Oxygen", False), ("CO2", False), ("Argon", False)]),
                ("Pencil element?", [("Graphite", True), ("Lead", False), ("Silver", False), ("Iron", False)]),
                ("Symbol for Iron?", [("Fe", True), ("Ir", False), ("In", False), ("Sn", False)]),
                ("Far right elements?", [("Noble Gases", True), ("Alkali", False), ("Halogens", False), ("Transition", False)]),
                ("Symbol for Silver?", [("Ag", True), ("Si", False), ("Sl", False), ("Au", False)]),
                ("Atomic number 1?", [("Hydrogen", True), ("Helium", False), ("Oxygen", False), ("Carbon", False)]),
                ("Natural heaviest element?", [("Uranium", True), ("Plutonium", False), ("Lead", False), ("Tungsten", False)]),
                ("Diamonds are pure?", [("Carbon", True), ("Silicon", False), ("Sulfur", False), ("Calcium", False)]),
                ("Symbol for Potassium?", [("K", True), ("P", False), ("Po", False), ("Pt", False)]),
                ("Vinegar + Baking Soda gas?", [("CO2", True), ("Oxygen", False), ("Hydrogen", False), ("Methane", False)]),
                ("Symbol for Copper?", [("Cu", True), ("Cp", False), ("Co", False), ("Cr", False)]),
                ("Steel primary component?", [("Iron", True), ("Aluminium", False), ("Nickel", False), ("Copper", False)]),
                ("Symbol for Sodium?", [("Na", True), ("S", False), ("So", False), ("Ni", False)]),
                ("Brimstone?", [("Sulfur", True), ("Phosphorus", False), ("Iodine", False), ("Chlorine", False)])
            ],
            "Astronomy: Exploring the Cosmos": [
                ("Red Planet?", [("Mars", True), ("Venus", False), ("Jupiter", False), ("Saturn", False)]),
                ("Largest planet?", [("Jupiter", True), ("Saturn", False), ("Neptune", False), ("Uranus", False)]),
                ("Center star?", [("Sun", True), ("Sirius", False), ("Polaris", False), ("Proxima", False)]),
                ("Earth's galaxy?", [("Milky Way", True), ("Andromeda", False), ("Sombrero", False), ("Whirlpool", False)]),
                ("Planet count?", [("8", True), ("9", False), ("7", False), ("10", False)]),
                ("Smallest planet?", [("Mercury", True), ("Mars", False), ("Venus", False), ("Pluto", False)]),
                ("Ringed planet?", [("Saturn", True), ("Jupiter", False), ("Mars", False), ("Neptune", False)]),
                ("Exploding star?", [("Supernova", True), ("Nebula", False), ("Black Hole", False), ("Quasar", False)]),
                ("Closest to sun?", [("Mercury", True), ("Venus", False), ("Earth", False), ("Mars", False)]),
                ("Moon gravity vs Earth?", [("1/6th", True), ("1/2", False), ("1/4th", False), ("1/10th", False)]),
                ("Hottest planet?", [("Venus", True), ("Mercury", False), ("Mars", False), ("Jupiter", False)]),
                ("First moon walker?", [("Armstrong", True), ("Aldrin", False), ("Gagarin", False), ("Glenn", False)]),
                ("Light-year measure?", [("Distance", True), ("Time", False), ("Speed", False), ("Brightness", False)]),
                ("Morning Star?", [("Venus", True), ("Mars", False), ("Mercury", False), ("Jupiter", False)]),
                ("First satellite?", [("Sputnik 1", True), ("Explorer 1", False), ("Vostok 1", False), ("Apollo 11", False)]),
                ("Orbit force?", [("Gravity", True), ("Magnetism", False), ("Centrifugal", False), ("Nuclear", False)]),
                ("Icy entities with tails?", [("Comets", True), ("Asteroids", False), ("Meteors", False), ("Moons", False)]),
                ("Uranus twin?", [("Neptune", True), ("Saturn", False), ("Jupiter", False), ("Earth", False)]),
                ("Tilted planet?", [("Uranus", True), ("Venus", False), ("Saturn", False), ("Pluto", False)]),
                ("Darkest space object?", [("Black Hole", True), ("Dark Nebula", False), ("Dead Moon", False), ("Comet", False)])
            ],
            "Quantum Physics Basics": [
                ("What is a quantum of light?", [("Photon", True), ("Electron", False), ("Proton", False), ("Neutron", False)]),
                ("Uncertainty principle?", [("Heisenberg", True), ("Einstein", False), ("Bohr", False), ("Planck", False)]),
                ("Who said 'God doesn't play dice'?", [("Einstein", True), ("Newton", False), ("Hawking", False), ("Feynman", False)]),
                ("E=mc^2, what is 'c'?", [("Speed of light", True), ("Center", False), ("Charge", False), ("Constant", False)]),
                ("Smallest unit of mass?", [("Atomic Mass Unit", True), ("Gram", False), ("Ounce", False), ("Slug", False)]),
                ("Cat experiment person?", [("Schrodinger", True), ("Pavlov", False), ("Skinner", False), ("Mendel", False)]),
                ("Particle in nucleus without charge?", [("Neutron", True), ("Proton", False), ("Electron", False), ("Positron", False)]),
                ("Fermions vs Bosons difference?", [("Spin", True), ("Charge", False), ("Color", False), ("Size", False)]),
                ("Double slit shows?", [("Wave-particle duality", True), ("Gravity", False), ("Magnetism", False), ("Speed", False)]),
                ("Dark matter is?", [("Invisible matter", True), ("Antimatter", False), ("Black holes", False), ("Dust", False)]),
                ("Higgs Boson nickname?", [("God Particle", True), ("Ghost Particle", False), ("Iron Particle", False), ("Energy Particle", False)]),
                ("Quantum entanglement is?", [("Spooky action at a distance", True), ("Magnetism", False), ("Gravity", False), ("Mixing", False)]),
                ("Superposition is?", [("Multiple states at once", True), ("Position in space", False), ("Moving fast", False), ("Dying", False)]),
                ("Tunneling is?", [("Passing through barriers", True), ("Digging holes", False), ("Traveling light", False), ("Echoing", False)]),
                ("Standard Model describes?", [("Particles & Forces", True), ("Cars", False), ("Stocks", False), ("Weather", False)]),
                ("String theory says?", [("Matter is vibrating strings", True), ("World is flat", False), ("Space is empty", False), ("Time is linear", False)]),
                ("Absolute zero temp?", [("-273.15 C", True), ("0 C", False), ("-100 C", False), ("-500 C", False)]),
                ("Pauli principle says?", [("Two electrons cannot share the same state", True), ("Everything is relative", False), ("Action is equal to reaction", False), ("Energy is lost", False)]),
                ("Bohr model is for?", [("Atoms", True), ("Galaxies", False), ("Cells", False), ("Economy", False)]),
                ("Hawking radiation is from?", [("Black Holes", True), ("Sun", False), ("Pulsars", False), ("Quasars", False)])
            ]
        },
        "Technology": {
            "Software Engineering Principles": [
                 ("SOLID 'S'?", [("Single Responsibility", True), ("Simple", False), ("Static", False), ("System", False)]),
                 ("Unit Test?", [("Testing small part", True), ("Full app test", False), ("DB test", False), ("UI test", False)]),
                 ("Scrum loops?", [("Sprints", True), ("Waves", False), ("Cycles", False), ("Steps", False)]),
                 ("Refactoring?", [("Cleaning code", True), ("Changing behavior", False), ("Adding features", False), ("Deleting", False)]),
                 ("GIT is?", [("Version control", True), ("Database", False), ("Language", False), ("Server", False)]),
                 ("Bug definition?", [("Software error", True), ("Hardware", False), ("Network lag", False), ("Feature", False)]),
                 ("API?", [("Prog Interface", True), ("Process Intel", False), ("Power Idea", False), ("Program Icon", False)]),
                 ("Android primary?", [("Kotlin", True), ("Swift", False), ("Ruby", False), ("PHP", False)]),
                 ("Agile?", [("Dynamic mindset", True), ("Fast PC", False), ("Language", False), ("Storage", False)]),
                 ("Frequent merging?", [("Continuous Intergration", True), ("Manual", False), ("Code Freeze", False), ("Migration", False)]),
                 ("Design Pattern?", [("Reusable solution", True), ("CSS", False), ("Layout", False), ("Algorithm", False)]),
                 ("Container tool?", [("Docker", True), ("Jenkins", False), ("Slack", False), ("VS Code", False)]),
                 ("QA?", [("Quality Assurance", True), ("Access", False), ("Action", False), ("Analysis", False)]),
                 ("IDE?", [("Dev Environment", True), ("Data Entry", False), ("Data Engine", False), ("Design Editor", False)]),
                 ("Git merge?", [("Combining branches", True), ("Adding", False), ("Pushing", False), ("Committing", False)]),
                 ("Peer Review?", [("Colleague check", True), ("Bonus talk", False), ("Survey", False), ("Hardware check", False)]),
                 ("Legacy Code?", [("Old code", True), ("Genius code", False), ("Perfect code", False), ("Zero bugs", False)]),
                 ("Technical Debt?", [("Short-term fix cost", True), ("Cloud debt", False), ("Bank loan", False), ("Syntax error", False)]),
                 ("Secure web?", [("HTTPS", True), ("HTTP", False), ("FTP", False), ("Telnet", False)]),
                 ("DRY?", [("Don't Repeat Yourself", True), ("Run Yearly", False), ("Data Run", False), ("Digital Registry", False)])
            ],
            "Evolution of Computers": [
                ("Analytical Engine person?", [("Charles Babbage", True), ("Alan Turing", False), ("Bill Gates", False), ("Jobs", False)]),
                ("First programmer?", [("Ada Lovelace", True), ("Grace Hopper", False), ("Turing", False), ("Von Neumann", False)]),
                ("First bug?", [("Moth", True), ("Glitch", False), ("Failure", False), ("Logic", False)]),
                ("WWW year?", [("1989", True), ("1975", False), ("1995", False), ("1983", False)]),
                ("Microprocessor first company?", [("Intel", True), ("IBM", False), ("Apple", False), ("AMD", False)]),
                ("HTTP?", [("Hypertext Transfer Protocol", True), ("Higher Pro", False), ("Transmission Power", False), ("Home Pro", False)]),
                ("Linux person?", [("Linus Torvalds", True), ("Gates", False), ("Jobs", False), ("Unix", False)]),
                ("First domain?", [("symbolics.com", True), ("apple", False), ("google", False), ("ms", False)]),
                ("Python person?", [("Guido van Rossum", True), ("Bjarne", False), ("Gosling", False), ("Ritchie", False)]),
                ("First graphical browser?", [("Mosaic", True), ("Netscape", False), ("IE", False), ("Opera", False)]),
                ("Mouse developed by?", [("Xerox PARC", True), ("IBM", False), ("Apple", False), ("MS", False)]),
                ("Binary 1010?", [("10", True), ("8", False), ("12", False), ("16", False)]),
                ("Apple co-founders?", [("Jobs & Wozniak", True), ("Wayne", True), ("Gates", False), ("Zuck", False)]),
                ("First social site?", [("SixDegrees", True), ("MySpace", False), ("Friendster", False), ("FB", False)]),
                ("GPU?", [("Graphics Processing Unit", True), ("Process Utility", False), ("Power Unit", False), ("Global Personal", False)]),
                ("Java creator company?", [("Sun Microsystems", True), ("Oracle", False), ("MS", False), ("IBM", False)]),
                ("Open source?", [("Shared code", True), ("Free software", False), ("Web-based", False), ("Experimental", False)]),
                ("First hard drive capacity?", [("5 MB", True), ("1 GB", False), ("100 MB", False), ("10 KB", False)]),
                ("First iPhone year?", [("2007", True), ("2005", False), ("2008", False), ("2010", False)]),
                ("Machine Learning?", [("Learning from data", True), ("Robots", False), ("Faster code", False), ("Auto manufacturing", False)])
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
                    # For quizzes needing 20 questions, ensure they reach that count
                    for i in range(len(questions), 20):
                        question = Question.objects.create(quiz=quiz, text=f"Advanced {quiz_title} Challenge {i+1}", order=i)
                        Choice.objects.create(question=question, text="Specific Topic Correct Ans", is_correct=True)
                        Choice.objects.create(question=question, text="Misc Topic Option 1", is_correct=False)
                        Choice.objects.create(question=question, text="Misc Topic Option 2", is_correct=False)
                        Choice.objects.create(question=question, text="Misc Topic Option 3", is_correct=False)
                    print(f"Successfully fixed all questions for {quiz_title}")
                except Quiz.DoesNotExist:
                    print(f"Quiz {quiz_title} not found.")
        except Category.DoesNotExist:
            print(f"Category {cat_name} not found.")

if __name__ == "__main__":
    fix_all_placeholders_final()
