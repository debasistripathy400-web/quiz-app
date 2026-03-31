import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()

from quiz.models import Category, Quiz, Question, Choice

def fix_all_placeholders_final_v2():
    history_quizzes = {
        "Ancient Civilizations: Rome & Egypt": [
            ("Who was the first emperor of Rome?", [("Augustus", True), ("Julius Caesar", False), ("Nero", False), ("Trajan", False)]),
            ("Which river was central to Ancient Egyptian life?", [("Nile", True), ("Tigris", False), ("Euphrates", False), ("Indus", False)]),
            ("What were the major structures built as Egyptian tombs?", [("Pyramids", True), ("Ziggurats", False), ("Colosseum", False), ("Acropolis", False)]),
            ("The Roman 'Pax Romana' means?", [("Roman Peace", True), ("Roman Law", False), ("Roman War", False), ("Roman Power", False)]),
            ("Who was the last pharaoh of Ancient Egypt?", [("Cleopatra VII", True), ("Ramses II", False), ("Tutankhamun", False), ("Akhenaten", False)]),
            ("Ancient Rome was founded on how many hills?", [("7", True), ("10", False), ("5", False), ("3", False)]),
            ("What writing system did Ancient Egyptians use?", [("Hieroglyphics", True), ("Cuneiform", False), ("Latin", False), ("Sanskrit", False)]),
            ("Rome defeated which rival in the Punic Wars?", [("Carthage", True), ("Greece", False), ("Persia", False), ("Gaul", False)]),
            ("The Great Sphinx has the head of a human and the body of a?", [("Lion", True), ("Eagle", False), ("Bull", False), ("Snake", False)]),
            ("Which Roman general was assassinated on the Ides of March?", [("Julius Caesar", True), ("Pompey", False), ("Mark Antony", False), ("Brutus", False)]),
            ("What material did Egyptians use for writing surface?", [("Papyrus", True), ("Parchment", False), ("Copper", False), ("Vellum", False)]),
            ("Which Roman architectural marvel was a stadium for gladiator fights?", [("Colosseum", True), ("Pantheon", False), ("Forum", False), ("Circus Maximus", False)]),
            ("The process of preserving bodies in Egypt is called?", [("Mummification", True), ("Embalming", False), ("Cremation", False), ("Ossification", False)]),
            ("Who was the Roman god of war?", [("Mars", True), ("Jupiter", False), ("Neptune", False), ("Vulcan", False)]),
            ("What is the name of the Egyptian sun god?", [("Ra", True), ("Anubis", False), ("Osiris", False), ("Horus", False)]),
            ("Who famously crossed the Alps with elephants to attack Rome?", [("Hannibal", True), ("Alexander", False), ("Genghis Khan", False), ("Attila", False)]),
            ("What was the primary language of the Roman Empire?", [("Latin", True), ("Greek", False), ("English", False), ("Aramaic", False)]),
            ("Ancient Egyptian kings were called?", [("Pharaohs", True), ("Tsars", False), ("Emperors", False), ("Sultans", False)]),
            ("Which Roman leader was known for the 'Commentaries on the Gallic War'?", [("Julius Caesar", True), ("Cicero", False), ("Sulla", False), ("Crassus", False)]),
            ("The Rosetta Stone was key to deciphering?", [("Hieroglyphics", True), ("Latin", False), ("Cuneiform", False), ("Greek", False)])
        ],
        "The Industrial Revolution": [
            ("Where did the Industrial Revolution begin?", [("Great Britain", True), ("USA", False), ("Germany", False), ("France", False)]),
            ("Who improved the steam engine in the late 18th century?", [("James Watt", True), ("John Kay", False), ("Samuel Crompton", False), ("Richard Arkwright", False)]),
            ("What was the first industry to be industrialized?", [("Textiles", True), ("Mining", False), ("Agriculture", False), ("Transport", False)]),
            ("Who invented the 'Spinning Jenny'?", [("James Hargreaves", True), ("Eli Whitney", False), ("Henry Ford", False), ("Graham Bell", False)]),
            ("What energy source replaced wood during the Industrial Revolution?", [("Coal", True), ("Oil", False), ("Electricity", False), ("Natural Gas", False)]),
            ("Who invented the cotton gin?", [("Eli Whitney", True), ("Thomas Edison", False), ("James Watt", False), ("George Stephenson", False)]),
            ("The 'Rocket' was an early example of a?", [("Steam Locomotive", True), ("Automobile", False), ("Rocket ship", False), ("Steamship", False)]),
            ("The movement of people from rural areas to cities is called?", [("Urbanization", True), ("Migration", False), ("Emigration", False), ("Colonization", False)]),
            ("Who developed the assembly line for automobiles?", [("Henry Ford", True), ("Karl Benz", False), ("Nikola Tesla", False), ("Thomas Edison", False)]),
            ("The Industrial Revolution led to the rise of which economic system?", [("Capitalism", True), ("Feudalism", False), ("Manorialism", False), ("Socialism", False)]),
            ("Who invented the telegraph?", [("Samuel Morse", True), ("Alexander Graham Bell", False), ("Guglielmo Marconi", False), ("Isaac Newton", False)]),
            ("Which act regulated child labor in British factories?", [("Factory Act", True), ("Mining Act", False), ("Education Act", False), ("Navigation Act", False)]),
            ("What was the primary mode of transport for goods before railways?", [("Canals", True), ("Trucks", False), ("Planes", False), ("Bicycles", False)]),
            ("Who invented the first practical incandescent light bulb?", [("Thomas Edison", True), ("Nikola Tesla", False), ("Benjamin Franklin", False), ("Michael Faraday", False)]),
            ("What was the name of the first steamship to cross the Atlantic?", [("Savannah", True), ("Titanic", False), ("Lusitania", False), ("Great Eastern", False)]),
            ("Who is known as the 'Father of the Railways'?", [("George Stephenson", True), ("James Watt", False), ("Richard Trevithick", False), ("Robert Fulton", False)]),
            ("The 'Great Exhibition' of 1851 was held in?", [("London", True), ("Paris", False), ("New York", False), ("Berlin", False)]),
            ("Who invented the telephone?", [("Alexander Graham Bell", True), ("Elisha Gray", False), ("Antonio Meucci", False), ("Thomas Edison", False)]),
            ("What was the name of the process for mass-producing steel?", [("Bessemer Process", True), ("Haber Process", False), ("Open Hearth Process", False), ("Siemens Process", False)]),
            ("The Luddites were known for?", [("Destroying machinery", True), ("Building factories", False), ("Inventing tools", False), ("Promoting unions", False)])
        ],
        "Cold War Eras & Beyond": [
            ("What was the metaphorical barrier dividing Europe during the Cold War?", [("Iron Curtain", True), ("Berlin Wall", False), ("Bamboo Curtain", False), ("Great Wall", False)]),
            ("Who was the leader of the Soviet Union during the Cuban Missile Crisis?", [("Nikita Khrushchev", True), ("Joseph Stalin", False), ("Leonid Brezhnev", False), ("Mikhail Gorbachev", False)]),
            ("What was the military alliance formed by Western nations in 1949?", [("NATO", True), ("Warsaw Pact", False), ("SEATO", False), ("UN", False)]),
            ("Which event is widely seen as the end of the Cold War in Europe?", [("Fall of the Berlin Wall", True), ("Cuban Missile Crisis", False), ("Korean War", False), ("Vietnam War", False)]),
            ("What was the name of the first satellite launched by the USSR?", [("Sputnik 1", True), ("Luna 1", False), ("Vostok 1", False), ("Mir", False)]),
            ("The 'Bay of Pigs' invasion was an attempt to overthow whom?", [("Fidel Castro", True), ("Che Guevara", False), ("Hugo Chavez", False), ("Daniel Ortega", False)]),
            ("What was the policy of 'Containment' designed to stop?", [("Spread of Communism", True), ("Nuclear testing", False), ("Trade embargoes", False), ("Colonization", False)]),
            ("Who was the US President during the end of the Cold War?", [("Ronald Reagan", True), ("John F. Kennedy", False), ("Richard Nixon", False), ("Lyndon Johnson", False)]),
            ("What was the 'Red Scare'?", [("Fear of Communism in the US", True), ("A type of illness", False), ("A volcanic eruption", False), ("A financial crash", False)]),
            ("The 'Vietnam War' was fought between North and South Vietnam from?", [("1955-1975", True), ("1945-1965", False), ("1965-1985", False), ("1950-1970", False)]),
            ("What does 'Perestroika' mean?", [("Restructuring", True), ("Openness", False), ("Justice", False), ("Peace", False)]),
            ("What does 'Glasnost' mean?", [("Openness", True), ("Restructuring", False), ("Unity", False), ("Strength", False)]),
            ("Who was the Soviet leader who introduced Glasnost and Perestroika?", [("Mikhail Gorbachev", True), ("Yuri Andropov", False), ("Konstantin Chernenko", False), ("Boris Yeltsin", False)]),
            ("What was the name of the US plan to rebuild Europe after WWII?", [("Marshall Plan", True), ("Truman Doctrine", False), ("Molotov Plan", False), ("Dawes Plan", False)]),
            ("Which war in the 1950s ended in a stalemate at the 38th parallel?", [("Korean War", True), ("Vietnam War", False), ("Balkan War", False), ("Gulf War", False)]),
            ("What was the 'Cuban Missile Crisis'?", [("Nuclear standoff in 1962", True), ("A trade dispute", False), ("An election crisis", False), ("A naval battle", False)]),
            ("The 'SALT' treaties were about?", [("Strategic Arms Limitation", True), ("Salt trade agreements", False), ("Space exploration", False), ("Sea navigation", False)]),
            ("Which country was divided into East and West after WWII?", [("Germany", True), ("Poland", False), ("France", False), ("Austria", False)]),
            ("The 'Kitchen Debate' was between Nixon and whom?", [("Khrushchev", True), ("Stalin", False), ("Brezhnev", False), ("Gorbachev", False)]),
            ("What was the name of the first human to travel into space?", [("Yuri Gagarin", True), ("Neil Armstrong", False), ("John Glenn", False), ("Alan Shepard", False)])
        ]
    }

    for quiz_title, questions in history_quizzes.items():
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
    fix_all_placeholders_final_v2()
