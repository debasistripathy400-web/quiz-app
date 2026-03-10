from django.core.management.base import BaseCommand
from quiz.models import Category, Quiz, Question, Choice

class Command(BaseCommand):
    help = 'Seeds 2 General Knowledge topics with 20 questions each'

    def handle(self, *args, **kwargs):
        try:
            gk_category = Category.objects.get(id=2)
            
            topics = [
                {
                    "title": "World History Essentials",
                    "questions": [
                        {"q": "Who was the first President of the United States?", "a": [("George Washington", True), ("Thomas Jefferson", False), ("Abraham Lincoln", False), ("John Adams", False)]},
                        {"q": "In which year did World War II end?", "a": [("1945", True), ("1944", False), ("1946", False), ("1939", False)]},
                        {"q": "Who discovered America in 1492?", "a": [("Christopher Columbus", True), ("Vasco da Gama", False), ("Marco Polo", False), ("Ferdinand Magellan", False)]},
                        {"q": "Which empire was ruled by Julius Caesar?", "a": [("Roman Empire", True), ("Greek Empire", False), ("Ottoman Empire", False), ("Persian Empire", False)]},
                        {"q": "The French Revolution began in which year?", "a": [("1789", True), ("1776", False), ("1812", False), ("1848", False)]},
                        {"q": "Who was known as the 'Maid of Orleans'?", "a": [("Joan of Arc", True), ("Queen Victoria", False), ("Marie Antoinette", False), ("Cleopatra", False)]},
                        {"q": "What was the name of the ship that brought the Pilgrims to America?", "a": [("Mayflower", True), ("Santa Maria", False), ("Beagle", False), ("Endeavour", False)]},
                        {"q": "Which wall fell in 1989, symbolizing the end of the Cold War?", "a": [("Berlin Wall", True), ("Great Wall of China", False), ("Western Wall", False), ("Hadrian's Wall", False)]},
                        {"q": "Who was the leader of the Soviet Union during WWII?", "a": [("Joseph Stalin", True), ("Vladimir Lenin", False), ("Nikita Khrushchev", False), ("Mikhail Gorbachev", False)]},
                        {"q": "The Magna Carta was signed in which country?", "a": [("England", True), ("France", False), ("Germany", False), ("Italy", False)]},
                        {"q": "Who was the primary author of the Declaration of Independence?", "a": [("Thomas Jefferson", True), ("Benjamin Franklin", False), ("James Madison", False), ("Alexander Hamilton", False)]},
                        {"q": "Which Pharaoh's tomb was discovered by Howard Carter in 1922?", "a": [("Tutankhamun", True), ("Ramesses II", False), ("Akhenaten", False), ("Thutmose III", False)]},
                        {"q": "The industrial revolution started in which country?", "a": [("Great Britain", True), ("USA", False), ("Germany", False), ("France", False)]},
                        {"q": "Who was the first human to travel into space?", "a": [("Yuri Gagarin", True), ("Neil Armstrong", False), ("Buzz Aldrin", False), ("John Glenn", False)]},
                        {"q": "In what year did the Titanic sink?", "a": [("1912", True), ("1900", False), ("1920", False), ("1915", False)]},
                        {"q": "Which ancient civilization built the pyramids?", "a": [("Egyptians", True), ("Mayans", False), ("Aztecs", False), ("Incas", False)]},
                        {"q": "Who wrote the 'Communist Manifesto' along with Karl Marx?", "a": [("Friedrich Engels", True), ("Vladimir Lenin", False), ("Leon Trotsky", False), ("Joseph Stalin", False)]},
                        {"q": "The Battle of Waterloo saw the defeat of which leader?", "a": [("Napoleon Bonaparte", True), ("Duke of Wellington", False), ("Louis XIV", False), ("Charles de Gaulle", False)]},
                        {"q": "Which country bombed Pearl Harbor in 1941?", "a": [("Japan", True), ("Germany", False), ("Italy", False), ("Soviet Union", False)]},
                        {"q": "Who was the first female Prime Minister of the United Kingdom?", "a": [("Margaret Thatcher", True), ("Theresa May", False), ("Angela Merkel", False), ("Indira Gandhi", False)]}
                    ]
                },
                {
                    "title": "Geography Mastermind",
                    "questions": [
                        {"q": "What is the largest country in the world by land area?", "a": [("Russia", True), ("Canada", False), ("China", False), ("USA", False)]},
                        {"q": "Which ocean is the largest on Earth?", "a": [("Pacific Ocean", True), ("Atlantic Ocean", False), ("Indian Ocean", False), ("Arctic Ocean", False)]},
                        {"q": "What is the capital of Japan?", "a": [("Tokyo", True), ("Kyoto", False), ("Osaka", False), ("Nagoya", False)]},
                        {"q": "Which river is the longest in the world?", "a": [("Nile", True), ("Amazon", False), ("Yangtze", False), ("Mississippi", False)]},
                        {"q": "In which continent is the Sahara Desert located?", "a": [("Africa", True), ("Asia", False), ("Australia", False), ("South America", False)]},
                        {"q": "What is the smallest country in the world?", "a": [("Vatican City", True), ("Monaco", False), ("Nauru", False), ("San Marino", False)]},
                        {"q": "Mount Everest is located in which mountain range?", "a": [("Himalayas", True), ("Andes", False), ("Rockies", False), ("Alps", False)]},
                        {"q": "Which country is also known as the Land of the Rising Sun?", "a": [("Japan", True), ("China", False), ("Korea", False), ("Thailand", False)]},
                        {"q": "What is the largest island in the world?", "a": [("Greenland", True), ("Australia", False), ("New Guinea", False), ("Borneo", False)]},
                        {"q": "Which canal connects the Atlantic and Pacific Oceans?", "a": [("Panama Canal", True), ("Suez Canal", False), ("Erie Canal", False), ("Kiel Canal", False)]},
                        {"q": "What is the capital of France?", "a": [("Paris", True), ("Lyon", False), ("Marseille", False), ("Berlin", False)]},
                        {"q": "Which country has the most population?", "a": [("India", True), ("China", False), ("USA", False), ("Indonesia", False)]},
                        {"q": "Which desert is the largest in the world?", "a": [("Antarctic Desert", True), ("Sahara", False), ("Gobi", False), ("Arabian", False)]},
                        {"q": "What is the capital city of Australia?", "a": [("Canberra", True), ("Sydney", False), ("Melbourne", False), ("Perth", False)]},
                        {"q": "Which is the highest waterfall in the world?", "a": [("Angel Falls", True), ("Niagara Falls", False), ("Victoria Falls", False), ("Iguazu Falls", False)]},
                        {"q": "Which sea is located between Europe and Africa?", "a": [("Mediterranean Sea", True), ("Red Sea", False), ("Black Sea", False), ("Caribbean Sea", False)]},
                        {"q": "Which country is the largest in South America?", "a": [("Brazil", True), ("Argentina", False), ("Colombia", False), ("Peru", False)]},
                        {"q": "Which city is known as the 'City of Love'?", "a": [("Paris", True), ("Venice", False), ("Rome", False), ("Prague", False)]},
                        {"q": "What is the capital of Canada?", "a": [("Ottawa", True), ("Toronto", False), ("Vancouver", False), ("Montreal", False)]},
                        {"q": "Which state in the USA is the largest by area?", "a": [("Alaska", True), ("Texas", False), ("California", False), ("Montana", False)]}
                    ]
                }
            ]

            for t in topics:
                quiz, created = Quiz.objects.get_or_create(
                    category=gk_category,
                    title=t["title"],
                    defaults={'time_limit_minutes': 10}
                )
                
                if created:
                    for i, q_data in enumerate(t["questions"]):
                        question = Question.objects.create(
                            quiz=quiz,
                            text=q_data["q"],
                            order=i + 1
                        )
                        for choice_text, is_correct in q_data["a"]:
                            Choice.objects.create(
                                question=question,
                                text=choice_text,
                                is_correct=is_correct
                            )
                    self.stdout.write(self.style.SUCCESS(f'Successfully created quiz: {quiz.title}'))
                else:
                    self.stdout.write(self.style.WARNING(f'Quiz "{quiz.title}" already exists, skipping questions creation.'))

        except Category.DoesNotExist:
            self.stdout.write(self.style.ERROR('General Knowledge category (ID 2) not found.'))
