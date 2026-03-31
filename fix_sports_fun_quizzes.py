import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Quiz, Question, Choice

def fix_quiz(title, questions_data):
    try:
        quiz = Quiz.objects.get(title=title)
        print(f"Updating Quiz: {quiz.title}")
        quiz.questions.all().delete()
        
        for q_text, choices, correct_idx in questions_data:
            q = Question.objects.create(quiz=quiz, text=q_text)
            for i, c_text in enumerate(choices):
                Choice.objects.create(question=q, text=c_text, is_correct=(i == correct_idx))
    except Quiz.DoesNotExist:
        print(f"Quiz '{title}' not found. Skipping...")

# --- DATA FOR QUIZZES ---

olympic_games = [
    ("In which city were the first modern Olympic Games held in 1896?", ["Paris", "London", "Athens", "Rome"], 2),
    ("How often are the Summer Olympic Games held?", ["Every 2 years", "Every 4 years", "Every 5 years", "Every 6 years"], 1),
    ("Who holds the record for the most Olympic gold medals ever won?", ["Usain Bolt", "Michael Phelps", "Carl Lewis", "Larisa Latynina"], 1),
    ("The five interlocking rings on the Olympic flag represent...", ["The five original sports", "The five continents", "The five founding members", "The five ring masters"], 1),
    ("Which country has won the most gold medals in Olympic history?", ["China", "Great Britain", "USA", "Russia"], 2),
    ("Which athlete is known as the 'Fastest Man in the World'?", ["Tyson Gay", "Usain Bolt", "Yohan Blake", "Justin Gatlin"], 1),
    ("In which year were the Olympic Games cancelled due to WWII?", ["1936", "1940 & 1944", "1948", "1952"], 1),
    ("Which of these is not an Olympic sport?", ["Canoeing", "Fencing", "Cricket", "Handball"], 2),
    ("The first Winter Olympic Games were held in which country?", ["Norway", "Switzerland", "France", "USA"], 2),
    ("What is the motto of the Olympic Games?", ["Faster, Higher, Stronger", "Win at all costs", "United in Diversity", "Sport for all"], 0),
    ("Who is the most decorated female Olympian of all time?", ["Simone Biles", "Katie Ledecky", "Larisa Latynina", "Serena Williams"], 2),
    ("Which city will host the 2024 Summer Olympic Games?", ["Tokyo", "Los Angeles", "Paris", "Brisbane"], 2),
    ("The Olympic flame was first introduced in which games?", ["1928 Amsterdam", "1896 Athens", "1936 Berlin", "1952 Helsinki"], 0),
    ("Which country traditionally enters the stadium last during the opening ceremony?", ["The host country", "Greece", "USA", "China"], 0),
    ("Which country traditionally enters the stadium FIRST during the opening ceremony?", ["Greece", "The host country", "Alphabetical order", "Past winner"], 0),
    ("Usain Bolt's 100m world record was set at which Olympics?", ["2004 Athens", "2008 Beijing", "2012 London", "2016 Rio"], 1),
    ("What color is the middle ring on the Olympic flag?", ["Blue", "Yellow", "Black", "Green"], 2),
    ("Which city hosted the first Olympics in the southern hemisphere?", ["Sydney", "Melbourne", "Rio de Janeiro", "Johannesburg"], 1),
    ("Nadia Comăneci was the first gymnast to be awarded a perfect score of 10 in which year?", ["1972", "1976", "1980", "1984"], 1),
    ("The ancient Olympic Games were held in honor of which Greek god?", ["Poseidon", "Apollo", "Zeus", "Hades"], 2)
]

formula_1 = [
    ("Who holds the record for the most Formula 1 World Championship titles?", ["Michael Schumacher", "Lewis Hamilton", "Sebastian Vettel", "Both Michael Schumacher & Lewis Hamilton"], 3),
    ("Which team has won the most Constructors' Championships in F1 history?", ["McLaren", "Williams", "Ferrari", "Mercedes"], 2),
    ("Who was the first ever F1 World Champion in 1950?", ["Juan Manuel Fangio", "Giuseppe Farina", "Alberto Ascari", "Stirling Moss"], 1),
    ("What is the name of the famous street circuit in Monaco?", ["Silverstone", "Circuit de Monaco", "Spa-Francorchamps", "Monza"], 1),
    ("Which driver is known for the nickname 'The Iceman'?", ["Mika Hakkinen", "Kimi Raikkonen", "Valtteri Bottas", "Nico Rosberg"], 1),
    ("In which country is the Interlagos circuit located?", ["Portugal", "Spain", "Brazil", "Italy"], 2),
    ("Who is the youngest driver ever to win an F1 World Championship?", ["Lewis Hamilton", "Sebastian Vettel", "Max Verstappen", "Fernando Alonso"], 1),
    ("What does the 'DRS' stand for in Formula 1?", ["Double Race Speed", "Drag Reduction System", "Direct Racing Steering", "Driver Response System"], 1),
    ("Which legendary driver passed away during the 1994 San Marino Grand Prix?", ["Gilles Villeneuve", "Ayrton Senna", "Jim Clark", "James Hunt"], 1),
    ("What is the traditional color of Ferrari in F1?", ["Blue", "Yellow", "Red", "Silver"], 2),
    ("The 'Chequered Flag' in F1 indicates...", ["The race start", "A warning", "The race finish", "A safety car entry"], 2),
    ("Which race is often called the 'Temple of Speed'?", ["Silverstone", "Monaco", "Monza", "Suzuka"], 2),
    ("Who is the dominant driver of the 2021-2023 F1 seasons?", ["Max Verstappen", "Lewis Hamilton", "Charles Leclerc", "Lando Norris"], 0),
    ("Which F1 team is based in Brackley, UK?", ["Ferrari", "Red Bull Racing", "Mercedes", "Alpine"], 2),
    ("How many wheels does a standard modern F1 car have?", ["4", "6", "3", "5"], 0),
    ("What is the primary material used for the chassis of an F1 car?", ["Steel", "Aluminum", "Carbon Fiber", "Titanium"], 2),
    ("Who is the legendary F1 commentator known as the 'Voice of F1'?", ["Martin Brundle", "Murray Walker", "David Croft", "Ted Kravitz"], 1),
    ("Which driver won the 2016 World Championship and then retired?", ["Nico Rosberg", "Jenson Button", "Felipe Massa", "Mark Webber"], 0),
    ("Which circuit is home to the 'Eau Rouge' corner?", ["Monza", "Spa-Francorchamps", "Hockenheimring", "Silverstone"], 1),
    ("Juan Manuel Fangio won championships with how many different teams?", ["2", "3", "4", "5"], 2)
]

tennis_golf = [
    ("Who holds the record for the most Men's Grand Slam singles titles?", ["Roger Federer", "Rafael Nadal", "Novak Djokovic", "Pete Sampras"], 2),
    ("Which city hosts the Wimbledon Tennis Championships?", ["New York", "Paris", "London", "Melbourne"], 2),
    ("The 'Masters' tournament in golf is played at which famous course?", ["St. Andrews", "Augusta National", "Pebble Beach", "Pinehurst"], 1),
    ("What surface is the French Open played on?", ["Grass", "Hard", "Clay", "Carpet"], 2),
    ("Who was the first woman to win 23 Grand Slam singles titles in the Open Era?", ["Serena Williams", "Steffi Graf", "Martina Navratilova", "Margaret Court"], 0),
    ("In golf, what is the term for scoring one under par on a hole?", ["Eagle", "Birdie", "Bogey", "Albatross"], 1),
    ("Which tennis player is known as the 'King of Clay'?", ["Novak Djokovic", "Roger Federer", "Rafael Nadal", "Bjorn Borg"], 2),
    ("What is the name of the oldest golf tournament in the world?", ["The Masters", "The US Open", "The Open Championship (British Open)", "The PGA Championship"], 2),
    ("A 'Grand Slam' in tennis involves winning how many major tournaments in a year?", ["2", "3", "4", "5"], 2),
    ("Who is the legendary golfer known as the 'Golden Bear'?", ["Tiger Woods", "Arnold Palmer", "Jack Nicklaus", "Gary Player"], 2),
    ("Which country has won the most Davis Cup (Tennis) titles?", ["Spain", "France", "USA", "Australia"], 2),
    ("In tennis, what follows 'Deuce' in a game?", ["Game", "Ad-in or Ad-out", "Tie-break", "Setpoint"], 1),
    ("Tiger Woods won his first Masters title at what age?", ["21", "25", "28", "19"], 0),
    ("Who is the only person to have won a Golden Slam in a single year?", ["Roger Federer", "Steffi Graf", "Serena Williams", "Andre Agassi"], 1),
    ("The 'Ryder Cup' in golf is a biennial competition between...", ["USA and UK", "USA and Europe", "Asia and Europe", "USA and Canada"], 1),
    ("What is the length of a professional tennis court for singles?", ["78 feet", "82 feet", "90 feet", "65 feet"], 0),
    ("Which golfer has the most PGA Tour wins of all time?", ["Tiger Woods", "Sam Snead", "Jack Nicklaus", "Both Tiger Woods & Sam Snead"], 3),
    ("What color jacket is awarded to the winner of The Masters in golf?", ["Blue", "Red", "Green", "White"], 2),
    ("Who was the 'Ice Man' of 70s/80s tennis career fame?", ["John McEnroe", "Bjorn Borg", "Jimmy Connors", "Ivan Lendl"], 1),
    ("The US Open tennis tournament is played in which borough of New York?", ["Manhattan", "Brooklyn", "Queens", "The Bronx"], 2)
]

riddles_fun = [
    ("I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?", ["A Globe", "A Map", "A Puzzle", "A Book"], 1),
    ("What has to be broken before you can use it?", ["A Promise", "An Egg", "A Heart", "A Mirror"], 1),
    ("I'm tall when I'm young, and I'm short when I'm old. What am I?", ["A Tree", "A Person", "A Candle", "A Pencil"], 2),
    ("What month of the year has 28 days?", ["February", "March", "December", "All of them"], 3),
    ("What is full of holes but still holds water?", ["A Sponge", "A Cloud", "A Sieve", "A Bucket"], 0),
    ("What question can you never answer 'yes' to?", ["Are you ready?", "Are you asleep?", "Can you hear me?", "Do you like cake?"], 1),
    ("What is always in front of you but can’t be seen?", ["The Shadow", "The Future", "The Wind", "Your Ego"], 1),
    ("There’s a one-story house where everything is yellow. What color are the stairs?", ["Yellow", "Orange", "There are no stairs", "White"], 2),
    ("What can you break, even if you never pick it up or touch it?", ["A promise", "A record", "A rule", "A silence"], 0),
    ("What goes up but never comes down?", ["A Balloon", "The Temperature", "Your Age", "The Smoke"], 2),
    ("A man who was outside in the rain without an umbrella or hat didn’t get a single hair on his head wet. Why?", ["He was using a tarp", "He was bald", "It wasn't raining hard", "He was indoors"], 1),
    ("What gets wet while drying?", ["A Sponge", "A Towel", "An Umbrella", "The Grass"], 1),
    ("What can you keep after giving to someone?", ["Your word", "A gift", "A cold", "Money"], 0),
    ("I shave every day, but my beard stays the same. What am I?", ["A Barber", "A Mirror", "A Statue", "A Razor"], 0),
    ("I have branches, but no fruit, trunk, or leaves. What am I?", ["A Bank", "A River", "A Family", "A Road"], 0),
    ("What has words, but never speaks?", ["A Book", "A Statue", "A Ghost", "A Movie"], 0),
    ("What runs all around a backyard, yet never moves?", ["A Fence", "A Dog", "A Tree", "A Path"], 0),
    ("What can travel all around the world without leaving its corner?", ["A Stamp", "A Bird", "A Plane", "A Thought"], 0),
    ("What has a thumb and four fingers, but is not a hand?", ["A Glove", "A Toy", "A Monkey", "A Shadow"], 0),
    ("What has many keys but can’t open a single lock?", ["A Piano", "A Prison", "A Map", "A Laptop"], 0)
]

# --- EXECUTION ---

fix_quiz("Olympic Games: History & Records", olympic_games)
fix_quiz("Formula 1 & Motorsport Legends", formula_1)
fix_quiz("Tennis & Golf Grand Slam History", tennis_golf)
fix_quiz("Random Riddles & Curiosities", riddles_fun)

print("\nDONE! All 4 targeted quizzes updated with 20 questions each.")
