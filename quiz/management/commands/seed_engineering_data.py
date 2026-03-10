from django.core.management.base import BaseCommand
from quiz.models import Category, Quiz, Question, Choice
from django.utils.text import slugify

class Command(BaseCommand):
    help = 'Seeds the database with 10 engineering topics and 20 questions each'

    def handle(self, *args, **kwargs):
        engineering_data = {
            "Civil Engineering": {
                "icon": "fas fa-building",
                "questions": [
                    {"q": "What is the primary material used in reinforced concrete?", "a": [("Steel", True), ("Wood", False), ("Plastic", False), ("Glass", False)]},
                    {"q": "Which instrument is used for measuring angles in surveying?", "a": [("Theodolite", True), ("Barometer", False), ("Thermometer", False), ("Anemometer", False)]},
                    {"q": "What is the main purpose of a foundation?", "a": [("Distribute weight to soil", True), ("Make building look tall", False), ("Insulate the building", False), ("Store water", False)]},
                    {"q": "What does a slump test measure in concrete?", "a": [("Workability", True), ("Strength", False), ("Color", False), ("Density", False)]},
                    {"q": "Who is known as the father of Civil Engineering?", "a": [("John Smeaton", True), ("Isambard Brunel", False), ("Thomas Telford", False), ("Gustave Eiffel", False)]},
                    {"q": "What is the standard width of a broad gauge railway in India?", "a": [("1.676 m", True), ("1.000 m", False), ("1.435 m", False), ("0.762 m", False)]},
                    {"q": "Which type of dam is the Hoover Dam?", "a": [("Arch-gravity dam", True), ("Earth-fill dam", False), ("Buttress dam", False), ("Rock-fill dam", False)]},
                    {"q": "What is the unit of pressure in SI units?", "a": [("Pascal", True), ("Newton", False), ("Joule", False), ("Watt", False)]},
                    {"q": "What is the process of removing salt from seawater called?", "a": [("Desalination", True), ("Filtration", False), ("Oxidation", False), ("Reduction", False)]},
                    {"q": "What is the term for a bridge supported by cables?", "a": [("Suspension bridge", True), ("Arch bridge", False), ("Beam bridge", False), ("Truss bridge", False)]},
                    {"q": "What material is famously known for its high tensile strength in suspension bridges?", "a": [("Steel", True), ("Aluminum", False), ("Iron", False), ("Bronze", False)]},
                    {"q": "What is the study of soil properties called?", "a": [("Geotechnical Engineering", True), ("Hydrology", False), ("Structural Engineering", False), ("Surveying", False)]},
                    {"q": "Which law states that stress is proportional to strain within the elastic limit?", "a": [("Hooke's Law", True), ("Newton's Law", False), ("Pascal's Law", False), ("Bernoulli's Law", False)]},
                    {"q": "What is the main ingredient of bitumen?", "a": [("Petroleum", True), ("Coal", False), ("Natural Gas", False), ("Wood", False)]},
                    {"q": "What is the name of the tallest building in the world?", "a": [("Burj Khalifa", True), ("Shanghai Tower", False), ("Empire State Building", False), ("Lotte World Tower", False)]},
                    {"q": "What type of survey focuses on water bodies?", "a": [("Hydrographic Survey", True), ("Topographic Survey", False), ("Cadastral Survey", False), ("Geodetic Survey", False)]},
                    {"q": "What is the term for a beam supported at only one end?", "a": [("Cantilever", True), ("Continuous beam", False), ("Simply supported beam", False), ("Fixed beam", False)]},
                    {"q": "What determines the load-bearing capacity of a pile foundation?", "a": [("Skin friction and end bearing", True), ("Color of the pile", False), ("Length only", False), ("Shape only", False)]},
                    {"q": "What is the primary function of a retaining wall?", "a": [("Hold back soil", True), ("Support the roof", False), ("Decorative purpose", False), ("Fire protection", False)]},
                    {"q": "What is the common ratio of cement to sand to coarse aggregate in M20 concrete?", "a": [("1:1.5:3", True), ("1:2:4", False), ("1:3:6", False), ("1:4:8", False)]},
                ]
            },
            "Mechanical Engineering": {
                "icon": "fas fa-cogs",
                "questions": [
                    {"q": "What is the basic unit of energy in the SI system?", "a": [("Joule", True), ("Watt", False), ("Newton", False), ("Volt", False)]},
                    {"q": "Which law of thermodynamics defines entropy?", "a": [("Second Law", True), ("First Law", False), ("Third Law", False), ("Zeroth Law", False)]},
                    {"q": "What type of engine is used in most modern cars?", "a": [("Internal Combustion", True), ("Steam Engine", False), ("Electric Motor", False), ("Jet Engine", False)]},
                    {"q": "What is the term for the resistance of a fluid to flow?", "a": [("Viscosity", True), ("Density", False), ("Buoyancy", False), ("Pressure", False)]},
                    {"q": "A gear with 20 teeth drives a gear with 40 teeth. What is the gear ratio?", "a": [("2:1", True), ("1:2", False), ("4:1", False), ("1:1", False)]},
                    {"q": "What material is commonly used to make engine blocks due to its heat dissipation?", "a": [("Aluminum", True), ("Iron", False), ("Copper", False), ("Lead", False)]},
                    {"q": "What is the device used to measure the power of an engine?", "a": [("Dynamometer", True), ("Thermometer", False), ("Barometer", False), ("Spectrometer", False)]},
                    {"q": "Which mechanism converts linear motion to rotary motion in an engine?", "a": [("Crankshaft", True), ("Camshaft", False), ("Piston", False), ("Valve", False)]},
                    {"q": "What is the boiling point of water at sea level in Celsius?", "a": [("100", True), ("0", False), ("212", False), ("373", False)]},
                    {"q": "What does a governor do in a steam engine?", "a": [("Regulates speed", True), ("Heats water", False), ("Cools steam", False), ("Stores oil", False)]},
                    {"q": "What is the primary purpose of lubrication?", "a": [("Reduce friction", True), ("Increase weight", False), ("Cool the engine", False), ("Change color", False)]},
                    {"q": "What is the term for the stress that causes permanent deformation?", "a": [("Yield stress", True), ("Ultimate stress", False), ("Normal stress", False), ("Shear stress", False)]},
                    {"q": "Which cycle is used as the basis for gasoline engines?", "a": [("Otto cycle", True), ("Diesel cycle", False), ("Rankine cycle", False), ("Carnot cycle", False)]},
                    {"q": "What is the main component of steel?", "a": [("Iron", True), ("Copper", False), ("Aluminum", False), ("Zinc", False)]},
                    {"q": "In a 4-stroke engine, which stroke follows the intake stroke?", "a": [("Compression", True), ("Expansion", False), ("Exhaust", False), ("Spark", False)]},
                    {"q": "What is the unit of force in the SI system?", "a": [("Newton", True), ("Pound", False), ("Kg-force", False), ("Dyne", False)]},
                    {"q": "What type of heat transfer occurs through a solid material?", "a": [("Conduction", True), ("Convection", False), ("Radiation", False), ("Advection", False)]},
                    {"q": "What is the purpose of an intercooler in a turbocharged engine?", "a": [("Cool the intake air", True), ("Cool the fuel", False), ("Cool the oil", False), ("Cool the exhaust", False)]},
                    {"q": "What material is known for having the highest thermal conductivity?", "a": [("Diamond", True), ("Silver", False), ("Copper", False), ("Gold", False)]},
                    {"q": "What is the term for a body's resistance to a change in its state of motion?", "a": [("Inertia", True), ("Momentum", False), ("Friction", False), ("Velocity", False)]},
                ]
            },
            "Electrical Engineering": {
                "icon": "fas fa-bolt",
                "questions": [
                    {"q": "What is the unit of electrical resistance?", "a": [("Ohm", True), ("Volt", False), ("Ampere", False), ("Watt", False)]},
                    {"q": "Which law states that V = IR?", "a": [("Ohm's Law", True), ("Kirchhoff's Law", False), ("Faraday's Law", False), ("Lenz's Law", False)]},
                    {"q": "What device is used to step up or step down AC voltage?", "a": [("Transformer", True), ("Capacitor", False), ("Resistor", False), ("Inductor", False)]},
                    {"q": "What is the unit of capacitance?", "a": [("Farad", True), ("Henry", False), ("Tesla", False), ("Webber", False)]},
                    {"q": "Which material is best known for being a good conductor of electricity?", "a": [("Silver", True), ("Rubber", False), ("Plastic", False), ("Glass", False)]},
                    {"q": "What type of current flows in only one direction?", "a": [("Direct Current (DC)", True), ("Alternating Current (AC)", False), ("Eddy Current", False), ("Static Current", False)]},
                    {"q": "Who is credited with discovering electromagnetic induction?", "a": [("Michael Faraday", True), ("Nikola Tesla", False), ("Thomas Edison", False), ("James Maxwell", False)]},
                    {"q": "What is the standard frequency of AC power in the US?", "a": [("60 Hz", True), ("50 Hz", False), ("100 Hz", False), ("120 Hz", False)]},
                    {"q": "What does a multimeter measure?", "a": [("Voltage, Current, Resistance", True), ("Light intensity", False), ("Sound level", False), ("Weight", False)]},
                    {"q": "What is the purpose of a fuse in a circuit?", "a": [("Protect from overcurrent", True), ("Store energy", False), ("Increase voltage", False), ("Generate heat", False)]},
                    {"q": "What is the unit of magnetic flux density?", "a": [("Tesla", True), ("Pascal", False), ("Henry", False), ("Ohm", False)]},
                    {"q": "Which component stores energy in a magnetic field?", "a": [("Inductor", True), ("Capacitor", False), ("Resistor", False), ("Diode", False)]},
                    {"q": "What is the power factor of a purely resistive circuit?", "a": [("1.0", True), ("0.5", False), ("0", False), ("-1.0", False)]},
                    {"q": "What does LED stand for?", "a": [("Light Emitting Diode", True), ("Low Energy Device", False), ("Long Enduring Diode", False), ("Liquid Electronic Display", False)]},
                    {"q": "Which device converts mechanical energy into electrical energy?", "a": [("Generator", True), ("Motor", False), ("Battery", False), ("Capacitor", False)]},
                    {"q": "What is the function of a diode?", "a": [("Allow current in one direction", True), ("Store charge", False), ("Vary resistance", False), ("Step up voltage", False)]},
                    {"q": "What is the unit of power?", "a": [("Watt", True), ("Joule", False), ("Coulomb", False), ("Volt", False)]},
                    {"q": "Which bridge is used to measure unknown resistance precisely?", "a": [("Wheatstone Bridge", True), ("Maxwell Bridge", False), ("Wien Bridge", False), ("Schering Bridge", False)]},
                    {"q": "What is the core of an electromagnet usually made of?", "a": [("Soft Iron", True), ("Aluminum", False), ("Copper", False), ("Lead", False)]},
                    {"q": "What is the primary semiconductor used in solar cells?", "a": [("Silicon", True), ("Germanium", False), ("Arsenic", False), ("Gallium", False)]},
                ]
            },
            "Computer Science & Engineering": {
                "icon": "fas fa-desktop",
                "questions": [
                    {"q": "What does CPU stand for?", "a": [("Central Processing Unit", True), ("Computer Personal Unit", False), ("Central Power Unit", False), ("Control Processing Unit", False)]},
                    {"q": "Which data structure follows the LIFO principle?", "a": [("Stack", True), ("Queue", False), ("Linked List", False), ("Tree", False)]},
                    {"q": "What is the brain of a computer system?", "a": [("Microprocessor", True), ("Hard Disk", False), ("RAM", False), ("Motherboard", False)]},
                    {"q": "What does HTTP stand for?", "a": [("HyperText Transfer Protocol", True), ("High Tech Transfer Product", False), ("HyperText Transmit Process", False), ("Hidden Text Transfer Protocol", False)]},
                    {"q": "Which language is primarily used for Android App development?", "a": [("Kotlin", True), ("Swift", False), ("PHP", False), ("Objective-C", False)]},
                    {"q": "What is the time complexity of binary search?", "a": [("O(log n)", True), ("O(n)", False), ("O(n^2)", False), ("O(1)", False)]},
                    {"q": "Which company developed the Python programming language?", "a": [("Guido van Rossum (Individual)", True), ("Google", False), ("Microsoft", False), ("Sun Microsystems", False)]},
                    {"q": "What is an IP address?", "a": [("Internet Protocol address", True), ("Internal Phone number", False), ("International Port", False), ("Identifier Page", False)]},
                    {"q": "What does SQL stand for?", "a": [("Structured Query Language", True), ("Simple Quality Logic", False), ("Storage Query Level", False), ("Standard Query Language", False)]},
                    {"q": "Which bitwise operator is used for inversion?", "a": [("NOT (~)", True), ("AND (&)", False), ("OR (|)", False), ("XOR (^)", False)]},
                    {"q": "What is the main purpose of an OS?", "a": [("Manage hardware and software", True), ("Word processing", False), ("Browser management", False), ("Game development", False)]},
                    {"q": "What does RAM stand for?", "a": [("Random Access Memory", True), ("Read Access Memory", False), ("Ready Available Memory", False), ("Rapid Access Module", False)]},
                    {"q": "Which sorting algorithm is generally the fastest in practice?", "a": [("QuickSort", True), ("BubbleSort", False), ("SelectionSort", False), ("InsertionSort", False)]},
                    {"q": "What is the smallest unit of data in a computer?", "a": [("Bit", True), ("Byte", False), ("Nibble", False), ("Word", False)]},
                    {"q": "What is the default port for HTTP?", "a": [("80", True), ("443", False), ("21", False), ("25", False)]},
                    {"q": "Which layer of the OSI model is responsible for routing?", "a": [("Network Layer", True), ("Data Link Layer", False), ("Transport Layer", False), ("Physical Layer", False)]},
                    {"q": "What is the base of the Hexadecimal number system?", "a": [("16", True), ("10", False), ("8", False), ("2", False)]},
                    {"q": "Who is known as the father of Artificial Intelligence?", "a": [("John McCarthy", True), ("Alan Turing", False), ("Marvin Minsky", False), ("Claude Shannon", False)]},
                    {"q": "Which language is used for styling web pages?", "a": [("CSS", True), ("HTML", False), ("JS", False), ("XML", False)]},
                    {"q": "What is GitHub used for?", "a": [("Version Control and Hosting", True), ("Video Editing", False), ("Graphic Design", False), ("Database Management", False)]},
                ]
            },
            "Chemical Engineering": {
                "icon": "fas fa-flask",
                "questions": [
                    {"q": "What is the primary unit of substance in chemistry?", "a": [("Mole", True), ("Kg", False), ("Liter", False), ("Meter", False)]},
                    {"q": "What is the process of separating components by boiling points?", "a": [("Distillation", True), ("Filtration", False), ("Centrifugation", False), ("Crystallization", False)]},
                    {"q": "Which reactor type is best for continuous large-scale production?", "a": [("CSTR", True), ("Batch Reactor", False), ("PFR", False), ("Semi-batch Reactor", False)]},
                    {"q": "What is the pH value of pure water?", "a": [("7", True), ("0", False), ("14", False), ("1", False)]},
                    {"q": "What is the term for a substance that speeds up a reaction without being consumed?", "a": [("Catalyst", True), ("Inhibitor", False), ("Reactant", False), ("Solvent", False)]},
                    {"q": "What does 'STP' stand for in chemistry?", "a": [("Standard Temperature and Pressure", True), ("Standard Time and Power", False), ("Safe Tool Process", False), ("Simple Terminology Part", False)]},
                    {"q": "Which gas is known as the 'Laughing Gas'?", "a": [("Nitrous Oxide", True), ("Carbon Dioxide", False), ("Methane", False), ("Helium", False)]},
                    {"q": "What is the main component of natural gas?", "a": [("Methane", True), ("Propane", False), ("Butane", False), ("Ethane", False)]},
                    {"q": "What is the heaviest naturally occurring element?", "a": [("Uranium", True), ("Lead", False), ("Gold", False), ("Plutonium", False)]},
                    {"q": "What is the universal solvent?", "a": [("Water", True), ("Alcohol", False), ("Acetone", False), ("Ether", False)]},
                    {"q": "What is the process of breaking long-chain hydrocarbons into smaller ones?", "a": [("Cracking", True), ("Polymerization", False), ("Hydrogenation", False), ("Oxidation", False)]},
                    {"q": "What is the symbol for Gold on the periodic table?", "a": [("Au", True), ("Ag", False), ("Fe", False), ("Gd", False)]},
                    {"q": "Which law relates the pressure and volume of a gas at constant temperature?", "a": [("Boyle's Law", True), ("Charles's Law", False), ("Avogadro's Law", False), ("Dalton's Law", False)]},
                    {"q": "What is the term for a solution that cannot dissolve any more solute?", "a": [("Saturated", True), ("Unsaturated", False), ("Supersaturated", False), ("Diluted", False)]},
                    {"q": "What is the main byproduct of the Haber process?", "a": [("Ammonia", True), ("Sulfuric Acid", False), ("Nitric Acid", False), ("Ethylene", False)]},
                    {"q": "What is the bonding in a diamond? ", "a": [("Covalent", True), ("Ionic", False), ("Metallic", False), ("Hydrogen", False)]},
                    {"q": "What is the movement of particles from high to low concentration called?", "a": [("Diffusion", True), ("Osmosis", False), ("Convection", False), ("Effusion", False)]},
                    {"q": "Which element is common to all organic compounds?", "a": [("Carbon", True), ("Oxygen", False), ("Nitrogen", False), ("Hydrogen", False)]},
                    {"q": "What is the unit of dynamic viscosity?", "a": [("Poise", True), ("Stokes", False), ("Pascal", False), ("Newton", False)]},
                    {"q": "Who formulated the Periodic Table of elements?", "a": [("Dmitri Mendeleev", True), ("John Dalton", False), ("Ernest Rutherford", False), ("Niels Bohr", False)]},
                ]
            },
            "Aerospace Engineering": {
                "icon": "fas fa-plane",
                "questions": [
                    {"q": "What force keeps an airplane in the air?", "a": [("Lift", True), ("Weight", False), ("Thrust", False), ("Drag", False)]},
                    {"q": "Who achieved the first powered airplane flight?", "a": [("Wright Brothers", True), ("Charles Lindbergh", False), ("Amelia Earhart", False), ("Leonardo da Vinci", False)]},
                    {"q": "What is the term for the speed of sound?", "a": [("Mach 1", True), ("Knot", False), ("Light Speed", False), ("Velocity", False)]},
                    {"q": "What is the main structural part of an airplane wing?", "a": [("Spar", True), ("Rib", False), ("Skin", False), ("Flap", False)]},
                    {"q": "Which principle explains how lift is generated?", "a": [("Bernoulli's Principle", True), ("Newton's Third Law", False), ("Pascal's Principle", False), ("Archimedes' Principle", False)]},
                    {"q": "What is the gas used in most modern space rockets?", "a": [("Liquid Hydrogen", True), ("Helium", False), ("Nitrogen", False), ("Carbon Dioxide", False)]},
                    {"q": "What part of the airplane controls 'roll'?", "a": [("Ailerons", True), ("Rudder", False), ("Elevator", False), ("Spoiler", False)]},
                    {"q": "What does NASA stand for?", "a": [("National Aeronautics and Space Administration", True), ("North American Space Agency", False), ("New Age Space Association", False), ("National Aerospace Scientist Alliance", False)]},
                    {"q": "What is the layer of earth's atmosphere where planes fly?", "a": [("Troposphere/Stratosphere", True), ("Mesosphere", False), ("Exosphere", False), ("Thermosphere", False)]},
                    {"q": "What is the term for a spacecraft's return to Earth?", "a": [("Re-entry", True), ("Launch", False), ("Docking", False), ("Orbit", False)]},
                    {"q": "Who was the first human in space?", "a": [("Yuri Gagarin", True), ("Neil Armstrong", False), ("Buzz Aldrin", False), ("John Glenn", False)]},
                    {"q": "What is the primary material used in modern high-performance aircraft?", "a": [("Titanium/Carbon Fiber", True), ("Steel", False), ("Wood", False), ("Lead", False)]},
                    {"q": "What is the purpose of a vertical stabilizer?", "a": [("Maintain yaw stability", True), ("Provide lift", False), ("Reduce drag", False), ("Increase speed", False)]},
                    {"q": "What force opposes thrust in flight?", "a": [("Drag", True), ("Weight", False), ("Lift", False), ("Torque", False)]},
                    {"q": "What is the name of the first artificial satellite?", "a": [("Sputnik 1", True), ("Explorer 1", False), ("Voyager 1", False), ("Apollo 11", False)]},
                    {"q": "Which part of the rocket engine produces thrust?", "a": [("Nozzle", True), ("Payload", False), ("Fuel Tank", False), ("Guidance System", False)]},
                    {"q": "What is an Orbit?", "a": [("Curved path around a celestial body", True), ("A type of engine", False), ("The edge of atmosphere", False), ("A communication signal", False)]},
                    {"q": "What determines an aircraft's 'Pitch'?", "a": [("Elevators", True), ("Ailerons", False), ("Rudder", False), ("Throttle", False)]},
                    {"q": "What is the most famous telescope in space?", "a": [("Hubble Space Telescope", True), ("Kepler", False), ("James Webb", False), ("Spitzer", False)]},
                    {"q": "What is 'Escape Velocity'?", "a": [("Speed needed to break free from gravity", True), ("Speed of landing", False), ("Speed of sound", False), ("Speed of light", False)]},
                ]
            },
            "Biomedical Engineering": {
                "icon": "fas fa-heartbeat",
                "questions": [
                    {"q": "What is an ECG used to monitor?", "a": [("Heart activity", True), ("Brain waves", False), ("Muscle strength", False), ("Lung capacity", False)]},
                    {"q": "What is a prosthesis?", "a": [("Artificial body part", True), ("Medical drug", False), ("Virus", False), ("Surgical tool", False)]},
                    {"q": "What imaging technique uses large magnets and radio waves?", "a": [("MRI", True), ("X-Ray", False), ("Ultrasound", False), ("CT Scan", False)]},
                    {"q": "What does 'biocompatibility' mean?", "a": [("Living in harmony with tissue", True), ("Being made of plastic", False), ("Killing bacteria", False), ("Dissolving in water", False)]},
                    {"q": "What device is used to regulate the heart rhythm?", "a": [("Pacemaker", True), ("Ventilator", False), ("Dialysis machine", False), ("Defibrillator", False)]},
                    {"q": "What is the study of mechanical laws relating to life?", "a": [("Biomechanics", True), ("Kinematics", False), ("Biophysics", False), ("Biochemistry", False)]},
                    {"q": "Which metal is commonly used for orthopedic implants due to its strength and safety?", "a": [("Titanium", True), ("Aluminum", False), ("Lead", False), ("Zinc", False)]},
                    {"q": "What is genomic engineering also known as?", "a": [("Genetic engineering", True), ("Cloning", False), ("Tissue repair", False), ("Cellular biology", False)]},
                    {"q": "What does EEG stand for?", "a": [("Electroencephalogram", True), ("Electronic Energy Graph", False), ("Electric Echo Guard", False), ("External Energy Gauge", False)]},
                    {"q": "Which machine replaces the function of the kidneys?", "a": [("Dialysis Machine", True), ("Heart-Lung Machine", False), ("Incubator", False), ("X-ray Machine", False)]},
                    {"q": "What is a stent used for in the human body?", "a": [("Keep arteries open", True), ("Replace a tooth", False), ("Bind a bone", False), ("Filter blood", False)]},
                    {"q": "What is the primary function of a ventilator?", "a": [("Support breathing", True), ("Monitor heart rate", False), ("Inject medicine", False), ("Analyze blood", False)]},
                    {"q": "What is the use of 'smart' pills?", "a": [("Deliver targeted drugs", True), ("Enhance memory", False), ("Provide energy", False), ("Monitor sleep", False)]},
                    {"q": "What are bioreactors used for?", "a": [("Growing cells or tissues", True), ("Generating electricity", False), ("Filtering air", False), ("Storing DNA", False)]},
                    {"q": "What is an exoskeleton used for?", "a": [("Mobile rehabilitation", True), ("Skin protection", False), ("Internal support", False), ("Eye surgery", False)]},
                    {"q": "What kind of waves does an Ultrasound use?", "a": [("Sound waves", True), ("Light waves", False), ("X-rays", False), ("Microwaves", False)]},
                    {"q": "What is the purpose of tissue engineering?", "a": [("Repair damaged tissues", True), ("Study insects", False), ("Build robots", False), ("Analyze fossils", False)]},
                    {"q": "Which material is used for contact lenses?", "a": [("Hydrogel", True), ("Glass", False), ("Steel", False), ("Epoxy", False)]},
                    {"q": "What is an insulin pump used to treat?", "a": [("Diabetes", True), ("Cancer", False), ("Flu", False), ("Asthma", False)]},
                    {"q": "What does a pulse oximeter measure?", "a": [("Oxygen saturation and heart rate", True), ("Blood sugar", False), ("Temperature", False), ("Respiration rate", False)]},
                ]
            },
            "Software Engineering": {
                "icon": "fas fa-code-branch",
                "questions": [
                    {"q": "What does SDLC stand for?", "a": [("Software Development Life Cycle", True), ("System Design Logic Chart", False), ("Software Data Level Control", False), ("Systematic Development Life Cycle", False)]},
                    {"q": "Which methodology uses 'Sprints'?", "a": [("Agile/Scrum", True), ("Waterfall", False), ("Spiral", False), ("V-Model", False)]},
                    {"q": "What is the purpose of Version Control (e.g. Git)?", "a": [("Track changes in code", True), ("Speed up the computer", False), ("Encrypt the data", False), ("Compile the software", False)]},
                    {"q": "What is a 'Bug' in software?", "a": [("An error or flaw", True), ("A type of hardware", False), ("A new feature", False), ("A small insect inside computer", False)]},
                    {"q": "What does API stand for?", "a": [("Application Programming Interface", True), ("Advanced Program Intelligence", False), ("Applied Professional Insight", False), ("Automated Process Integrated", False)]},
                    {"q": "What is the purpose of unit testing?", "a": [("Test small components individually", True), ("Test the whole system at once", False), ("Test how much power it uses", False), ("Test user interface only", False)]},
                    {"q": "What does DRY stand for in programming?", "a": [("Don't Repeat Yourself", True), ("Data Retention Yield", False), ("Digital Robust Yield", False), ("Design React Yield", False)]},
                    {"q": "Which design pattern ensures only one instance of a class exists?", "a": [("Singleton", True), ("Factory", False), ("Observer", False), ("Strategy", False)]},
                    {"q": "What is 'Refactoring'?", "a": [("Improving internal code structure", True), ("Changing external behavior", False), ("Adding new features", False), ("Deleting the code", False)]},
                    {"q": "What is 'Backend' development?", "a": [("Server-side logic and database", True), ("User interface and design", False), ("Hardware manufacturing", False), ("Quality assurance", False)]},
                    {"q": "Which language is most used for web scripts?", "a": [("JavaScript", True), ("C++", False), ("Cobol", False), ("Pascal", False)]},
                    {"q": "What is 'DevOps'?", "a": [("Merging development and operations", True), ("A type of programming language", False), ("A video game console", False), ("An office layout", False)]},
                    {"q": "What is 'Cloud Computing'?", "a": [("Delivery of computing over internet", True), ("Using computers in high altitude", False), ("Weather forecasting", False), ("A type of hard drive", False)]},
                    {"q": "What is the purpose of 'Code Review'?", "a": [("Examine code for quality", True), ("Estimate the cost", False), ("Run the software", False), ("Write documentation", False)]},
                    {"q": "What is 'Deployment'?", "a": [("Making software available for use", True), ("Writing the code", False), ("Testing the logic", False), ("Planning the feature", False)]},
                    {"q": "What does IDE stand for?", "a": [("Integrated Development Environment", True), ("Internal Design Entity", False), ("Integrated Data Engine", False), ("Interactive Design Entry", False)]},
                    {"q": "What is a Database?", "a": [("Organized collection of data", True), ("A type of screen", False), ("A power supply", False), ("A programming language", False)]},
                    {"q": "What is 'Front-end' development?", "a": [("User interface and experience", True), ("Server logic", False), ("Database design", False), ("Hardware maintenance", False)]},
                    {"q": "What is 'Scalability'?", "a": [("Handle increased workload", True), ("Change the color", False), ("Measure the weight", False), ("Record a video", False)]},
                    {"q": "What is 'Legacy Code'?", "a": [("Existing code from older systems", True), ("Highly optimized code", False), ("Newest code written", False), ("Secret code", False)]},
                ]
            },
            "Environmental Engineering": {
                "icon": "fas fa-leaf",
                "questions": [
                    {"q": "What is the main goal of environmental engineering?", "a": [("Protect public health and environment", True), ("Build taller skyscrapers", False), ("Increase oil production", False), ("Develop new weapons", False)]},
                    {"q": "What is the term for the variety of life on Earth?", "a": [("Biodiversity", True), ("Ecology", False), ("Geology", False), ("Anthropology", False)]},
                    {"q": "Which gas is the primary contributor to global warming?", "a": [("Carbon Dioxide", True), ("Oxygen", False), ("Argon", False), ("Nitrogen", False)]},
                    {"q": "What is the process of recycling water called?", "a": [("Water Reclamation", True), ("Water Pollution", False), ("Water Exhaustion", False), ("Water Density", False)]},
                    {"q": "What does PPM stand for in pollution measurement?", "a": [("Parts Per Million", True), ("Power Per Meter", False), ("Pure Particles Measured", False), ("Point Product Method", False)]},
                    {"q": "What is 'Sustainable Development'?", "a": [("Meeting needs without compromising future", True), ("Building quickly without planning", False), ("Using all resources now", False), ("Ignoring environmental laws", False)]},
                    {"q": "Which energy source is considered renewable?", "a": [("Solar Power", True), ("Coal", False), ("Natural Gas", False), ("Nuclear (Fission)", False)]},
                    {"q": "What is the main cause of acid rain?", "a": [("Sulfur and Nitrogen oxides", True), ("Carbon Dioxide", False), ("Oxygen", False), ("Water vapor", False)]},
                    {"q": "What is 'Composting'?", "a": [("Biological decay of organic waste", True), ("Burning plastic", False), ("Burying glass", False), ("Dumping oil", False)]},
                    {"q": "What is 'Eutrophication'?", "a": [("Excessive richness of nutrients in water", True), ("Lack of air in a city", False), ("Dying of forests", False), ("Melting of ice caps", False)]},
                    {"q": "What protocol was designed to protect the ozone layer?", "a": [("Montreal Protocol", True), ("Kyoto Protocol", False), ("Paris Agreement", False), ("Geneva Convention", False)]},
                    {"q": "What is 'Deforestation'?", "a": [("Clearing of forests", True), ("Planting trees", False), ("Studying plants", False), ("Using forest products", False)]},
                    {"q": "What is the purpose of an Environmental Impact Assessment (EIA)?", "a": [("Predict environmental effects of projects", True), ("Measure building height", False), ("Count employees", False), ("Check financial status", False)]},
                    {"q": "What is 'Greywater'?", "a": [("Waste water from sinks and showers", True), ("Water from toilets", False), ("Pure drinking water", False), ("Ocean water", False)]},
                    {"q": "What is the 'Greenhouse Effect'?", "a": [("Trapping of heat in atmosphere", True), ("Growing plants in glass", False), ("Using green paint", False), ("Reflecting sunlight", False)]},
                    {"q": "Which organization leads global environmental efforts?", "a": [("UNEP", True), ("WHO", False), ("WTO", False), ("IMF", False)]},
                    {"q": "What is 'Urban Sprawl'?", "a": [("Uncontrolled expansion of cities", True), ("Building parks in cities", False), ("Cleaning city air", False), ("Reducing city population", False)]},
                    {"q": "What does the '3 Rs' stand for?", "a": [("Reduce, Reuse, Recycle", True), ("Release, Repair, Return", False), ("Read, Revise, Repeat", False), ("Run, Ride, Rest", False)]},
                    {"q": "What is the primary method of disposal for municipal solid waste?", "a": [("Landfill", True), ("Dumping in ocean", False), ("Deep space storage", False), ("Burying in backyard", False)]},
                    {"q": "What is a 'Carbon Footprint'?", "a": [("Total greenhouse gas emissions caused", True), ("A print left on coal", False), ("A type of shoe", False), ("Measuring the weight of carbon", False)]},
                ]
            },
            "Structural Engineering": {
                "icon": "fas fa-hard-hat",
                "questions": [
                    {"q": "What is the main purpose of a structural frame?", "a": [("Support the loads of the building", True), ("Keep the building warm", False), ("Hold the windows", False), ("Decorative pattern", False)]},
                    {"q": "What is the term for the maximum weight a structure can take?", "a": [("Ultimate Load", True), ("Initial Load", False), ("Dead Load", False), ("Wind Load", False)]},
                    {"q": "What is a 'Truss'?", "a": [("Framework of triangles", True), ("A type of cement", False), ("A large bolt", False), ("A painting method", False)]},
                    {"q": "What does F.O.S stands for in structural design?", "a": [("Factor of Safety", True), ("Floor of System", False), ("Force of Stability", False), ("Frequency of Strain", False)]},
                    {"q": "Which material has the highest strength-to-weight ratio for buildings?", "a": [("Structural Steel", True), ("Concrete", False), ("Brick", False), ("Stone", False)]},
                    {"q": "What is 'Buckling'?", "a": [("Sudden failure of a column under compression", True), ("A type of floor tiling", False), ("A painting defect", False), ("Rusting of steel", False)]},
                    {"q": "What is 'Pre-stressed' concrete?", "a": [("Concrete with internal compression", True), ("Concrete that is very old", False), ("Colored concrete", False), ("Concrete with no steel", False)]},
                    {"q": "What is the primary function of a column?", "a": [("Resist axial compression", True), ("Support a wall", False), ("Provide shade", False), ("Store wires", False)]},
                    {"q": "What determines a structure's resistance to earthquakes?", "a": [("Ductility and strength", True), ("Beauty", False), ("Weight only", False), ("Location only", False)]},
                    {"q": "What is a 'Live Load'?", "a": [("Temporary loads like people and furniture", True), ("Weight of the building itself", False), ("Wind force", False), ("Weight of snow", False)]},
                    {"q": "What is the term for the internal resistance per unit area?", "a": [("Stress", True), ("Strain", False), ("Deformation", False), ("Force", False)]},
                    {"q": "What is 'Torsion'?", "a": [("Twisting of an object", True), ("Stretching of a wire", False), ("Bending of a beam", False), ("Breaking of a bolt", False)]},
                    {"q": "What is a 'Foundation'?", "a": [("Base that transfers load to ground", True), ("The top floor", False), ("The outer skin", False), ("The elevator shaft", False)]},
                    {"q": "What is the name of the theory used to analyze structures?", "a": [("Structural Analysis", True), ("Fluid Dynamics", False), ("Thermodynamics", False), ("Quantum Mechanics", False)]},
                    {"q": "What is the purpose of 'Shear Walls'?", "a": [("Resist lateral forces like wind/quake", True), ("Divide rooms", False), ("Support the roof", False), ("Decorative look", False)]},
                    {"q": "What is the most common shape for a structural steel beam?", "a": [("I-beam", True), ("O-beam", False), ("L-beam", False), ("U-beam", False)]},
                    {"q": "What is 'Dead Load'?", "a": [("Weight of permanent structures", True), ("Weight of cars in garage", False), ("Wind pressure", False), ("Weight of rain", False)]},
                    {"q": "What is 'Deflection'?", "a": [("Degree to which a structural element is displaced", True), ("The color change", False), ("The cost of materials", False), ("The time to build", False)]},
                    {"q": "What is 'Reinforcement'?", "a": [("Adding steel to concrete to handle tension", True), ("Painting the walls", False), ("Adding more windows", False), ("Cleaning the site", False)]},
                    {"q": "Which design method is primarily used in modern structural codes?", "a": [("Limit State Design", True), ("Working Stress Method", False), ("Empirical Method", False), ("Trial and Error", False)]},
                ]
            }
        }

        self.stdout.write('Starting Engineering Data Expansion...')

        for cat_name, details in engineering_data.items():
            category, _ = Category.objects.get_or_create(
                name=cat_name,
                defaults={
                    "description": f"Master the fundamentals of {cat_name}.",
                    "icon_class": details["icon"]
                }
            )

            quiz_title = f"{cat_name} - Fundamentals Challenge"
            quiz, created = Quiz.objects.get_or_create(
                category=category,
                title=quiz_title,
                defaults={
                    "description": f"A comprehensive {len(details['questions'])}-question test on core {cat_name} concepts.",
                    "time_limit_minutes": 15,
                    "slug": slugify(quiz_title)
                }
            )

            if created:
                for i, q_data in enumerate(details["questions"], 1):
                    question = Question.objects.create(
                        quiz=quiz,
                        text=q_data["q"],
                        order=i
                    )
                    for choice_text, is_correct in q_data["a"]:
                        Choice.objects.create(
                            question=question,
                            text=choice_text,
                            is_correct=is_correct
                        )
                self.stdout.write(self.style.SUCCESS(f'Created quiz: {quiz_title}'))
            else:
                self.stdout.write(self.style.WARNING(f'Quiz already exists: {quiz_title}'))

        self.stdout.write(self.style.SUCCESS('Successfully seeded 200 engineering questions!'))
