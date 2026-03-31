import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_project.settings')
django.setup()

from quiz.models import Quiz, Question, Choice

def fix_quiz(title, questions_data):
    try:
        quiz = Quiz.objects.get(title=title)
        print(f"Updating Quiz: {quiz.title}")
        # Clear existing questions
        quiz.questions.all().delete()
        
        for q_text, choices, correct_idx in questions_data:
            q = Question.objects.create(quiz=quiz, text=q_text)
            for i, c_text in enumerate(choices):
                Choice.objects.create(question=q, text=c_text, is_correct=(i == correct_idx))
    except Quiz.DoesNotExist:
        print(f"Quiz '{title}' not found. Skipping...")

# --- DATA FOR QUIZZES ---

cyber_hacking = [
    ("What does SQL injection primarily target?", ["Operating Systems", "Databases", "Network Firewalls", "Web Browsers"], 1),
    ("Which protocol is used for securely accessing a remote computer's shell?", ["HTTP", "FTP", "SSH", "Telnet"], 2),
    ("What is 'Phishing'?", ["Searching for security holes", "Sending fake emails to steal data", "A type of firewall", "Network sniffing"], 1),
    ("Which of these is considered a 'Strong' password characteristic?", ["Using only lowercase", "Using your birth year", "Mixing symbols, numbers, and cases", "Using your pet's name"], 2),
    ("What does DDoS stand for?", ["Distributed Denial of Service", "Digital Data Operating System", "Direct Dual Operating Server", "Distributed Data Online System"], 0),
    ("Which of these is a symetric encryption algorithm?", ["RSA", "Diffie-Hellman", "AES", "ECC"], 2),
    ("What is the purpose of a 'Honeypot' in cybersecurity?", ["Storing passwords", "Attracting and trapping hackers", "Speeding up internet", "Blocking spam"], 1),
    ("What does a 'Man-in-the-Middle' attack involve?", ["Intercepting communication between two parties", "Cracking passwords locally", "Deleting server files", "Physical theft of hardware"], 0),
    ("Which port is typically used for HTTPS?", ["80", "21", "22", "443"], 3),
    ("What is 'Ransomware'?", ["Software that improves speed", "Malware that encrypts files for money", "A type of antivirus", "A browser plugin"], 1),
    ("What does VPN stand for?", ["Virtual Private Network", "Visual Private Node", "Virtual Public Network", "Verified Private Network"], 0),
    ("Which organization defines the Top 10 web vulnerabilities?", ["FBI", "IEEE", "OWASP", "ACM"], 2),
    ("What is 'Social Engineering'?", ["Coding in Python", "Manipulating people into giving secrets", "Building social media", "Optimizing network flow"], 1),
    ("What is an 'exploited' vulnerability?", ["A bug that has been patched", "A flaw that allows unauthorized access", "A feature requested by users", "A documentation error"], 1),
    ("Which Linux distribution is most famous for penetration testing?", ["Ubuntu", "Kali Linux", "Fedora", "CentOS"], 1),
    ("What is 'Two-Factor Authentication'?", ["Using two passwords", "Using a password and another method like a code", "Logging in from two devices", "Changing password twice"], 1),
    ("What is the 'Kernel' in an OS?", ["The user interface", "The core part that manages hardware", "A type of virus", "The file explorer"], 1),
    ("What is a 'Zero-Day' vulnerability?", ["A flaw fixed in 0 days", "A flaw unknown to the vendor and being exploited", "A very minor bug", "A flaw found 100 days ago"], 1),
    ("What is 'Cross-Site Scripting' (XSS)?", ["Writing scripts for multiple sites", "Injecting malicious scripts into web pages", "Server-side scripting", "CSS styling"], 1),
    ("What does 'Cold Boot' attack target?", ["Software source code", "System RAM data after shutdown", "Hard drive sectors", "GPU memory"], 1)
]

world_capitals = [
    ("What is the capital of Japan?", ["Kyoto", "Osaka", "Tokyo", "Hiroshima"], 2),
    ("In which country is the capital city 'Canberra' located?", ["New Zealand", "Australia", "Canada", "South Africa"], 1),
    ("What is the capital of France?", ["Lyon", "Marseille", "Paris", "Bordeaux"], 2),
    ("Which city is the capital of Brazil?", ["Rio de Janeiro", "São Paulo", "Brasília", "Salvador"], 2),
    ("What is the capital of Egypt?", ["Alexandria", "Luxor", "Cairo", "Giza"], 2),
    ("What is the capital of Germany?", ["Munich", "Frankfurt", "Berlin", "Hamburg"], 2),
    ("Which city is the capital of Russia?", ["Saint Petersburg", "Moscow", "Kazan", "Novosibirsk"], 1),
    ("What is the capital of Canada?", ["Toronto", "Vancouver", "Montreal", "Ottawa"], 3),
    ("What is the capital of Italy?", ["Milan", "Rome", "Florence", "Venice"], 1),
    ("What is the capital of India?", ["Mumbai", "Kolkata", "New Delhi", "Chennai"], 2),
    ("Which city is the capital of China?", ["Shanghai", "Beijing", "Guangzhou", "Shenzhen"], 1),
    ("What is the capital of Argentina?", ["Buenos Aires", "Cordoba", "Rosario", "Mendoza"], 0),
    ("What is the capital of Turkey?", ["Istanbul", "Ankara", "Izmir", "Antalya"], 1),
    ("Which city is the capital of South Korea?", ["Busan", "Incheon", "Seoul", "Daegu"], 2),
    ("What is the capital of Mexico?", ["Guadalajara", "Monterrey", "Cancun", "Mexico City"], 3),
    ("What is the capital of Spain?", ["Barcelona", "Madrid", "Valencia", "Seville"], 1),
    ("Which city is the capital of South Africa?", ["Cape Town", "Johannesburg", "Pretoria", "Durban"], 2),
    ("What is the capital of Thailand?", ["Phuket", "Chiang Mai", "Bangkok", "Pattaya"], 2),
    ("What is the capital of Greece?", ["Thessaloniki", "Patras", "Athens", "Heraklion"], 2),
    ("Which city is the capital of Sweden?", ["Gothenburg", "Malmo", "Stockholm", "Uppsala"], 2)
]

human_inventions = [
    ("Who is credited with inventing the light bulb?", ["Nikola Tesla", "Thomas Edison", "Albert Einstein", "Alexander Graham Bell"], 1),
    ("Which invention is considered the start of the Industrial Revolution?", ["The Steam Engine", "The Printing Press", "The Telephone", "The Internet"], 0),
    ("Who invented the telephone?", ["Guglielmo Marconi", "Alexander Graham Bell", "Samuel Morse", "Johann Philipp Reis"], 1),
    ("The Wright Brothers are famous for inventing the...", ["Car", "Airplane", "Rocket", "Helicopter"], 1),
    ("Which ancient civilization invented the wheel first?", ["Egyptians", "Greeks", "Sumerians", "Romans"], 2),
    ("Who developed the theory of relativity?", ["Isaac Newton", "Stephen Hawking", "Albert Einstein", "Marie Curie"], 2),
    ("Which invention allowed for the mass production of books?", ["Paper", "Ink", "The Printing Press", "The Quill"], 2),
    ("Who is often called the 'Father of the Computer'?", ["Bill Gates", "Steve Jobs", "Charles Babbage", "Alan Turing"], 2),
    ("Alexander Fleming discovered which life-saving invention?", ["Penicillin", "The X-Ray", "The Vaccine", "Insulin"], 0),
    ("Which device was invented by Eli Whitney in 1793?", ["The Steam Boat", "The Cotton Gin", "The Sewing Machine", "The Reaper"], 1),
    ("Guglielmo Marconi is best known for developing...", ["The Television", "The Radio", "The Radar", "The Microwave"], 1),
    ("Who invented the World Wide Web while at CERN?", ["Steve Wozniak", "Linus Torvalds", "Tim Berners-Lee", "Marc Andreessen"], 2),
    ("The first assembly line for mass producing cars was used by...", ["Karl Benz", "Henry Ford", "Enzo Ferrari", "Walter Chrysler"], 1),
    ("In which country was paper invented during the Han dynasty?", ["China", "India", "Egypt", "Greece"], 0),
    ("What was the first message sent via telegraph in 1844?", ["Hello World", "What hath God wrought", "SOS", "Incoming"], 1),
    ("Who invented the phonograph?", ["Thomas Edison", "Emile Berliner", "Alexander Melville Bell", "Leon Scott"], 0),
    ("The telescope was significantly improved by which astronomer in 1609?", ["Copernicus", "Galileo Galilei", "Kepler", "Brahe"], 1),
    ("Who invented the first practical vaccination?", ["Louis Pasteur", "Edward Jenner", "Jonas Salk", "Albert Sabin"], 1),
    ("Which invention used for navigation utilizes magnetism?", ["Astrolabe", "Compass", "Sextant", "Radar"], 1),
    ("The internal combustion engine was a key part of whose 1886 vehicle?", ["Henry Ford", "Karl Benz", "Gottlieb Daimler", "Rudolf Diesel"], 1)
]

art_literature = [
    ("Who painted the 'Mona Lisa'?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Michelangelo"], 1),
    ("Which author wrote the masterpiece 'Romeo and Juliet'?", ["Charles Dickens", "Mark Twain", "William Shakespeare", "Jane Austen"], 2),
    ("Which artist is known for cutting off his own ear?", ["Claude Monet", "Vincent van Gogh", "Salvador Dalí", "Rembrandt"], 1),
    ("Who wrote the 'Harry Potter' series?", ["J.R.R. Tolkien", "George R.R. Martin", "J.K. Rowling", "Stephen King"], 2),
    ("Which Spanish artist painted 'Guernica'?", ["Francisco Goya", "Salvador Dalí", "Pablo Picasso", "Diego Velázquez"], 2),
    ("Who wrote 'To Kill a Mockingbird'?", ["Harper Lee", "Ernest Hemingway", "F. Scott Fitzgerald", "John Steinbeck"], 0),
    ("Which sculptor created the marble statue 'David'?", ["Donatello", "Auguste Rodin", "Michelangelo", "Bernini"], 2),
    ("Which novel features the character 'Sherlock Holmes'?", ["A Study in Scarlet", "Moby Dick", "The Great Gatsby", "Oliver Twist"], 0),
    ("The 'Starry Night' is a famous work by which artist?", ["Edouard Manet", "Vincent van Gogh", "Gustav Klimt", "Henri Matisse"], 1),
    ("Who wrote 'The Odyssey'?", ["Virgil", "Homer", "Sophocles", "Euripides"], 1),
    ("Which artistic movement was Claude Monet a key figure in?", ["Surrealism", "Cubism", "Impressionism", "Expressionism"], 2),
    ("Who is the author of 'Pride and Prejudice'?", ["Charlotte Brontë", "Emily Brontë", "Jane Austen", "Mary Shelley"], 2),
    ("Which Russian author wrote 'War and Peace'?", ["Fyodor Dostoevsky", "Anton Chekhov", "Leo Tolstoy", "Vladimir Nabokov"], 2),
    ("The painting 'The Persistence of Memory' featuring melting clocks is by...", ["Pablo Picasso", "Salvador Dalí", "Joan Miró", "Frida Kahlo"], 1),
    ("Who wrote 'The Catcher in the Rye'?", ["J.D. Salinger", "Jack Kerouac", "Truman Capote", "Kurt Vonnegut"], 0),
    ("Which Renaissance artist painted the ceiling of the Sistine Chapel?", ["Raphael", "Leonardo da Vinci", "Michelangelo", "Botticelli"], 2),
    ("The play 'Hamlet' is a...", ["Comedy", "Tragedy", "History", "Romance"], 1),
    ("Who wrote the epic poem 'Paradise Lost'?", ["Geoffrey Chaucer", "John Milton", "John Keats", "Lord Byron"], 1),
    ("Which American author wrote 'The Old Man and the Sea'?", ["William Faulkner", "Ernest Hemingway", "John Steinbeck", "F. Scott Fitzgerald"], 1),
    ("Which art style is characterized by geometric shapes and multiple viewpoints?", ["Baroque", "Rococo", "Cubism", "Realism"], 2)
]

pop_music_80s_today = [
    ("Who is known as the 'King of Pop'?", ["Elvis Presley", "Michael Jackson", "Prince", "George Michael"], 1),
    ("Which 80s band sang 'Girls Just Want to Have Fun'?", ["Madonna", "Cyndi Lauper", "Whitney Houston", "Pat Benatar"], 1),
    ("Which artist released the album 'Thriller' in 1982?", ["Michael Jackson", "Rick James", "Lionel Richie", "Stevie Wonder"], 0),
    ("Who sang 'Like a Virgin' in 1984?", ["Britney Spears", "Madonna", "Paula Abdul", "Janet Jackson"], 1),
    ("What was the debut single of Britney Spears in 1998?", ["Toxic", "Oops!... I Did It Again", "...Baby One More Time", "I'm a Slave 4 U"], 2),
    ("Which 90s group sang 'Wannabe'?", ["Destiny's Child", "Spice Girls", "TLC", "En Vogue"], 1),
    ("Who released the hit song 'Shape of You' in 2017?", ["Justin Bieber", "Ed Sheeran", "The Weeknd", "Shawn Mendes"], 1),
    ("Which artist is known for the hit song 'Bad Guy'?", ["Ariana Grande", "Billie Eilish", "Dua Lipa", "Halsey"], 1),
    ("Who won the first season of American Idol?", ["Kelly Clarkson", "Carrie Underwood", "Adam Lambert", "Jordin Sparks"], 0),
    ("Which band released the song 'Smells Like Teen Spirit' in 1991?", ["Pearl Jam", "Soundgarden", "Nirvana", "Alice in Chains"], 2),
    ("Who is the artist behind the 2014 hit 'Shake It Off'?", ["Katy Perry", "Taylor Swift", "Lady Gaga", "Miley Cyrus"], 1),
    ("Which Latin artist broke records with 'Despacito'?", ["J Balvin", "Bad Bunny", "Luis Fonsi", "Ricky Martin"], 2),
    ("The 80s hit 'Purple Rain' is by which legendary musician?", ["Prince", "David Bowie", "Freddie Mercury", "Sting"], 0),
    ("Who sang 'Rolling in the Deep' in 2010?", ["Leona Lewis", "Amy Winehouse", "Adele", "Duffy"], 2),
    ("Which rapper released 'The Marshall Mathers LP' in 2000?", ["Jay-Z", "Eminem", "Dr. Dre", "Snoop Dogg"], 1),
    ("Which artist's fans are known as 'Beyhives'?", ["Rihanna", "Beyoncé", "Nicki Minaj", "Cardi B"], 1),
    ("What is the real name of Lady Gaga?", ["Stefani Germanotta", "Alecia Moore", "Katheryn Hudson", "Robyn Fenty"], 0),
    ("Which group released cross-over hit 'Dynamite' in 2020?", ["EXO", "Blackpink", "BTS", "Stray Kids"], 2),
    ("Who sang 'Born to Run' in the late 70s/80s era?", ["Bob Dylan", "Bruce Springsteen", "Billy Joel", "Tom Petty"], 1),
    ("Which artist released 'Blinding Lights' in 2019?", ["Ed Sheeran", "The Weeknd", "Post Malone", "Bruno Mars"], 1)
]

video_game_history = [
    ("What was the first commercially successful video game?", ["Pong", "Space Invaders", "Pac-Man", "Asteroids"], 0),
    ("Who is the creator of the 'Mario' and 'Zelda' franchises?", ["Hideo Kojima", "Shigeru Miyamoto", "Masahiro Sakurai", "Satoshi Tajiri"], 1),
    ("In which year was the first PlayStation console released in Japan?", ["1990", "1992", "1994", "1996"], 2),
    ("What is the highest-selling video game of all time (as of 2023)?", ["Minecraft", "Tetris", "GTA V", "Super Mario Bros."], 0),
    ("Which company developed the 'Halo' series initially?", ["Epic Games", "Bungie", "id Software", "Valve"], 1),
    ("Who is the protagonist of the 'Legend of Zelda' series?", ["Zelda", "Link", "Ganon", "Sheik"], 1),
    ("Which game introduced the 'Battle Royale' genre to massive popularity?", ["PUBG", "Fortnite", "H1Z1", "Apex Legends"], 0),
    ("What was the code name for the Nintendo GameCube during development?", ["Project Atlantis", "Project Reality", "Dolphin", "Revolution"], 2),
    ("Which game is known for the phrase 'The cake is a lie'?", ["Half-Life", "Portal", "Team Fortress 2", "BioShock"], 1),
    ("In 'Pac-Man', what is the name of the pink ghost?", ["Blinky", "Pinky", "Inky", "Clyde"], 1),
    ("Which console featured the first built-in CD-ROM drive?", ["Sega Saturn", "Sega CD", "PC Engine CD-ROM²", "PlayStation"], 2),
    ("What is the best-selling handheld console of all time?", ["Game Boy", "PSP", "Nintendo DS", "Nintendo Switch"], 2),
    ("Which game series features characters like Ryu and Ken?", ["Tekken", "Mortal Kombat", "Street Fighter", "SoulCalibur"], 2),
    ("Who founded the company Atari in 1972?", ["Steve Jobs", "Nolan Bushnell", "Jack Tramiel", "Hiroshi Yamauchi"], 1),
    ("The 'Master Chief' is the main character of which franchise?", ["Doom", "Gears of War", "Halo", "Mass Effect"], 2),
    ("Which game won Game of the Year in 2022?", ["Elden Ring", "God of War Ragnarok", "Stray", "Horizon Forbidden West"], 0),
    ("What was the first RPG to ever be released?", ["Final Fantasy", "Dragon Quest", "Dungeons & Dragons (Tabletop influce)", "Ultima I"], 3),
    ("In 'Sonic the Hedgehog', what is Sonic's sidekick's name?", ["Knuckles", "Shadow", "Tails", "Amy"], 2),
    ("Which company released the 'Xbox' in 2001?", ["Sony", "Sega", "Nintendo", "Microsoft"], 3),
    ("What is the primary objective in 'Tetris'?", ["Match 3 colors", "Clear lines of blocks", "Defeat a boss", "Protect a tower"], 1)
]

intro_psychology = [
    ("Who is known as the 'Father of modern psychology'?", ["Sigmund Freud", "Wilhelm Wundt", "William James", "B.F. Skinner"], 1),
    ("In psychology, what does 'ID' represent in Freud's theory?", ["Rational part", "Moral conscience", "Primal instincts", "Social ego"], 2),
    ("Which perspective in psychology focuses on observable behavior?", ["Cognitive", "Humanistic", "Behaviorism", "Psychodynamic"], 2),
    ("What is the 'Placebo Effect'?", ["A drug that cures everything", "Improvement due to belief in treatment", "A memory loss condition", "A type of hypnosis"], 1),
    ("What is 'Classical Conditioning' associated with?", ["B.F. Skinner", "Ivan Pavlov", "Abraham Maslow", "Carl Rogers"], 1),
    ("The study of how people change from birth to death is called...", ["Social Psychology", "Developmental Psychology", "Clinical Psychology", "Cognitive Psychology"], 1),
    ("What is the 'Amygdala' primarily responsible for?", ["Logic", "Memory storage", "Emotional processing", "Motor skills"], 2),
    ("Which sleep stage is most associated with dreaming?", ["Stage 1", "Stage 2", "Stage 3", "REM"], 3),
    ("What is 'Cognitive Dissonance'?", ["Loss of memory", "Mental discomfort from conflicting beliefs", "High intelligence", "Social anxiety"], 1),
    ("Abraham Maslow is famous for describing a 'Hierarchy of'...", ["Emotions", "Needs", "Behaviors", "Goals"], 1),
    ("What is 'Positive Reinforcement'?", ["Adding a pleasant stimulus to increase behavior", "Removing an unpleasant stimulus", "Punishing bad behavior", "Ignoring behavior"], 0),
    ("Which part of the brain is the 'Central Command' for the nervous system?", ["Cerebellum", "Brainstem", "Thalamus", "Cerebrum"], 3),
    ("What defines a 'Correlational Study'?", ["Proving cause and effect", "Observing relationships between variables", "Clinical treatment", "Brain scanning"], 1),
    ("Who developed the theory of 'Operant Conditioning'?", ["Jean Piaget", "B.F. Skinner", "Erik Erikson", "Carl Jung"], 1),
    ("What is 'Neuroplasticity'?", ["Brain surgery", "The brain's ability to reorganize itself", "Brain damage", "Plastic parts in the brain"], 1),
    ("In the 'Nature vs. Nurture' debate, 'Nurture' refers to...", ["Genetics", "Environment and experience", "Biological evolution", "Natural instincts"], 1),
    ("What is 'Sensory Adaptation'?", ["Loss of sight", "Reduced sensitivity to a constant stimulus", "Improved hearing", "Color blindness"], 1),
    ("The 'Big Five' personality traits include Openness, Conscientiousness, Extraversion, Agreeableness, and...", ["Neuroticism", "Narcissism", "Nihilism", "Negativity"], 0),
    ("What is 'Amnesia'?", ["Loss of sleep", "Loss of memory", "Loss of speech", "Loss of appetite"], 1),
    ("Which psychological term refers to a 'mental shortcut'?", ["Algorithm", "Heuristic", "Axiom", "Hypothesis"], 1)
]

social_behavior = [
    ("What is the 'Bystander Effect'?", ["Helping everyone", "Likelihood of helping decreases as others are present", "Watching sports", "Social media engagement"], 1),
    ("Who conducted the famous 'Stanford Prison Experiment'?", ["Stanley Milgram", "Philip Zimbardo", "Solomon Asch", "Leon Festinger"], 1),
    ("What is 'Conformity'?", ["Opposing social norms", "Changing behavior to match a group", "Leadership skills", "Isolation"], 1),
    ("The 'Milgram Experiment' studied obedience to...", ["Authority figures", "Peer pressure", "Social rules", "Internal ethics"], 0),
    ("What is 'Groupthink'?", ["Brainstorming", "Prioritizing group harmony over critical thinking", "Team building", "Collective intelligence"], 1),
    ("What is 'Prejudice'?", ["Positive actions", "An unjustified negative attitude toward a group", "Neutral observation", "Fact-based opinion"], 1),
    ("What is 'Altruism'?", ["Selfish behavior", "Disinterested and selfless concern for others", "Financial greed", "Fear of crowds"], 1),
    ("What is 'Social Facilitation'?", ["Better performance on simple tasks in front of others", "Social anxiety", "Helping others", "Teaching skills"], 0),
    ("What is the 'Self-Serving Bias'?", ["Helping coworkers", "Attributing success to oneself and failure to external factors", "Extreme modesty", "Always blaming oneself"], 1),
    ("What is 'Deindividuation'?", ["Feeling unique", "Loss of self-awareness in groups", "Making individual choices", "Personal branding"], 1),
    ("What is 'Implicit Bias'?", ["Conscious hate", "Unconscious associations or stereotypes", "Legal discrimination", "Public policy"], 1),
    ("Which term describes the 'foot-in-the-door' technique?", ["Persuasion by starting with a small request", "Hard selling", "Scare tactics", "Logical arguing"], 0),
    ("What is 'Stereotyping'?", ["Evaluating people fairly", "Generalized belief about a group seen as true for all members", "Scientific naming", "Professional photography"], 1),
    ("What is 'Prosocial Behavior'?", ["Behavior intended to help others", "Professional socializing", "Antisocial actions", "Networking"], 0),
    ("What is 'Cognitive Dissonance' in a social context?", ["Agreeing with everyone", "Conflict between behavior and attitudes", "Extreme happiness", "Silent treatment"], 1),
    ("Which factor most strongly influences 'Interpersonal Attraction'?", ["Proximity", "Intelligence", "Wealth", "Name"], 0),
    ("What is 'Social Loafing'?", ["Working hard in teams", "Exerting less effort when working in a group", "Baking bread with friends", "Job hunting"], 1),
    ("What is 'Aggression' in social psychology?", ["Physical exercise", "Behavior intended to harm another", "High ambition", "Defensive posture"], 1),
    ("What is 'Persuasion'?", ["Physical force", "Process of changing someone's attitude or behavior", "Direct command", "Silence"], 1),
    ("The 'Just-World Hypothesis' is the belief that...", ["Life is unfair", "People get what they deserve", "Everything is random", "Good things happen to bad people"], 1)
]

# Additional content for: Developmental Psychology, Abnormal Psychology
dev_psych = [
    ("Jean Piaget is famous for his theory of...", ["Social development", "Cognitive development in children", "Moral development", "Physical growth"], 1),
    ("What is 'Object Permanence'?", ["Believing objects are permanent", "Understanding objects exist even when unseen", "Fear of losing things", "Art appreciation"], 1),
    ("During which stage does Piaget say 'Egocentrism' is most common?", ["Sensorimotor", "Preoperational", "Concrete Operational", "Formal Operational"], 1),
    ("Who developed the 'Eight Stages of Psychosocial Development'?", ["Sigmund Freud", "Erik Erikson", "John Bowlby", "Noam Chomsky"], 1),
    ("What is 'Attachment Theory' primarily about?", ["Building houses", "Bonding between child and caregiver", "Learning to read", "Physical coordination"], 1),
    ("The first psychosocial stage in Erikson's theory is...", ["Autonomy vs Shame", "Trust vs Mistrust", "Initiative vs Guilt", "Identity vs Confusion"], 1),
    ("What is 'Puberty'?", ["Mental aging", "Biological transition to sexual maturity", "Learning to drive", "Career planning"], 1),
    ("What does 'Generativity vs Stagnation' focus on?", ["Infancy", "Early childhood", "Middle adulthood", "Old age"], 2),
    ("The 'Formal Operational' stage is characterized by...", ["Logical touch", "Abstract and hypothetical reasoning", "Crying", "Basic motor skills"], 1),
    ("Who studied 'Moral Development' and identified three levels?", ["Lawrence Kohlberg", "Albert Bandura", "Carl Rogers", "B.F. Skinner"], 0),
    ("What is 'Scaffolding' in Vygotsky's theory?", ["Building construction", "Temporary support as child learns a new task", "Physical punishment", "IQ testing"], 1),
    ("What is the 'Zone of Proximal Development'?", ["A safe space for kids", "Tasks a child can do with help but not alone", "A military zone", "The area near a school"], 1),
    ("The term 'Teratogen' refers to...", ["A type of dinosaur", "Agents that cause birth defects", "Biological nutrients", "A psychological test"], 1),
    ("What is 'Infantile Amnesia'?", ["Babies forgetting toys", "Inability to remember events before age 3", "Memory loss in old age", "Difficulty learning to speak"], 1),
    ("Which style of parenting is characterized by high warmth and high control?", ["Permissive", "Authoritative", "Authoritarian", "Neglectful"], 1),
    ("The 'Empty Nest' syndrome occurs when...", ["A bird leaves a tree", "Children leave home for adulthood", "Parents lose their jobs", "Moving to a new city"], 1),
    ("What is 'Conservation' in Piaget's theory?", ["Saving water", "Understanding that quantity stays same despite shape change", "Genetic coding", "Animal protection"], 1),
    ("The 'Strange Situation' was a test developed by...", ["Mary Ainsworth", "Diana Baumrind", "Carol Gilligan", "Margaret Mahler"], 0),
    ("According to Erikson, adolescence is a search for...", ["Wealth", "Identity", "Power", "Safety"], 1),
    ("What is 'Gerontology'?", ["Study of children", "Study of the aging process and elderly", "Study of genetics", "Study of rocks"], 1)
]

abnormal_psych = [
    ("What manual is used by psychiatrists to diagnose disorders?", ["WHO-10", "DSM-5", "APA-P", "Psych-Guide"], 1),
    ("Which disorder is characterized by extreme mood swings (Manic and Depressive)?", ["Schizophrenia", "Bipolar Disorder", "OCD", "Generalized Anxiety"], 1),
    ("What does OCD stand for?", ["Online Constant Data", "Obsessive-Compulsive Disorder", "Organic Clinical Disease", "Open Case Diagnosis"], 1),
    ("Schizophrenia is often associated with hallucinations and...", ["High appetite", "Delusions", "Better memory", "Clear thinking"], 1),
    ("What is a 'Phobia'?", ["A moderate dislike", "An irrational and extreme fear", "A type of medicine", "A professional degree"], 1),
    ("Which therapy focuses on changing negative thought patterns?", ["Physical Therapy", "Cognitive Behavioral Therapy (CBT)", "Massage Therapy", "Hypnosis"], 1),
    ("What is 'PTSD'?", ["Post-Traumatic Stress Disorder", "Pre-Treatment Social Data", "Personal Time Saving Device", "Primary Tension Skill"], 0),
    ("A 'Panic Attack' is often mistaken for...", ["A cold", "A heart attack", "Indigestion", "Tiredness"], 1),
    ("What is 'Anorexia Nervosa'?", ["An eating disorder", "A skin condition", "A sleep disorder", "A form of depression"], 0),
    ("The term 'Psychopathy' is often used to describe...", ["Extreme shyness", "Lack of empathy and antisocial behavior", "Strong intelligence", "Great artistic skill"], 1),
    ("Which disorder involves a persistent state of sadness and loss of interest?", ["ADHD", "Major Depressive Disorder", "Autism", "Insomnia"], 1),
    ("What is 'Dissociative Identity Disorder' previously known as?", ["Schizophrenia", "Multiple Personality Disorder", "Bipolar Type II", "Hysteria"], 1),
    ("Which medication is often used to treat Depression?", ["Antibiotics", "Antidepressants (SSRIs)", "Painkillers", "Vitamins"], 1),
    ("What is 'Agoraphobia'?", ["Fear of heights", "Fear of open or public spaces", "Fear of spiders", "Fear of water"], 1),
    ("The study of the causes of psychological disorders is called...", ["Epidemiology", "Etiology", "Ontology", "Pathology"], 1),
    ("Which professional can prescribe medication for mental health?", ["Psychologist", "Psychiatrist", "Social Worker", "Counselor"], 1),
    ("What is 'Narcissistic Personality Disorder' characterized by?", ["Extreme modesty", "Excessive interest in oneself and need for admiration", "Constant fear of others", "Desire to live alone"], 1),
    ("ADHD stands for Attention-Deficit/...", ["High-Data", "Hyperactivity Disorder", "Heuristic Design", "Hybrid Development"], 1),
    ("A 'Compulsion' in OCD is...", ["A random thought", "A repetitive behavior performed to reduce anxiety", "A type of medication", "A dream"], 1),
    ("What is 'Stigma' in mental health?", ["A cure", "A negative mark of disgrace or social disapproval", "A professional award", "A symptom of ADHD"], 1)
]

# --- EXECUTION ---

fix_quiz("Cybersecurity & Hacking Defense", cyber_hacking)
fix_quiz("World Capitals & Nations", world_capitals)
fix_quiz("Humanity's Greatest Inventions", human_inventions)
fix_quiz("Global Arts & Literature", art_literature)
fix_quiz("Pop Music: 80s, 90s, & Today", pop_music_80s_today)
fix_quiz("Video Game History & Legends", video_game_history)
fix_quiz("Introduction to Psychology", intro_psychology)
fix_quiz("Social Behavior & Influence", social_behavior)
fix_quiz("Developmental Psychology: Childhood to Adult", dev_psych)
fix_quiz("Abnormal Psychology & Clinical Cases", abnormal_psych)

print("\nDONE! All 10 targeted quizzes updated with 20 questions each.")
