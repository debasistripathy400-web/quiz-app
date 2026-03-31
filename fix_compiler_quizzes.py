import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quiz_project.settings")
django.setup()

from quiz.models import Category, Quiz, Question, Choice

def fix_all_placeholders_final_v3():
    compiler_quizzes = {
        "Code Generation & Optimization": [
            ("What is the goal of the code optimizer?", [("Reduced execution time", True), ("Increased file size", False), ("Debugging", False), ("Formatting", False)]),
            ("What is 'Inlining'?", [("Replacing function calls with bodies", True), ("Adding comments", False), ("Deleting code", False), ("Error detection", False)]),
            ("What is a 'Basic Block'?", [("Sequence of code with one entry & exit", True), ("A type of variable", False), ("A memory address", False), ("A hardware part", False)]),
            ("Who proposed the 'Constant Folding' optimization?", [("John Cocke", True), ("Turing", False), ("Knuth", False), ("Hopper", False)]),
            ("Dead code elimination means?", [("Removing unreachable or unused code", True), ("Removing bugs", False), ("Removing documentation", False), ("Removing data", False)]),
            ("Loop unrolling is used for?", [("Reducing loop overhead", True), ("Deleting loops", False), ("Adding complexity", False), ("Increasing latency", False)]),
            ("Static Single Assignment (SSA) is useful for?", [("Data flow analysis", True), ("Syntax highlighting", False), ("File compression", False), ("User input", False)]),
            ("What is a 'Register' in code generation?", [("Small, fast storage on CPU", True), ("A file on disk", False), ("A database index", False), ("A RAM block", False)]),
            ("Code motion refers to?", [("Moving code out of loops", True), ("Moving files", False), ("Moving variable declarations", False), ("UI transitions", False)]),
            ("Strength reduction means?", [("Replacing expensive ops with cheaper ones", True), ("Reducing variable names", False), ("Deleting comments", False), ("Reducing power usage", False)]),
            ("Common Subexpression Elimination (CSE)?", [("Replacing repeat computations with one", True), ("Deleting functions", False), ("Adding variables", False), ("Renaming classes", False)]),
            ("What is an 'Activation Record'?", [("Data used for function calls", True), ("A music track", False), ("A persistent log", False), ("A security token", False)]),
            ("Peephole optimization is?", [("Optimizing small code windows", True), ("Checking for spyware", False), ("Visual formatting", False), ("Large scale refactoring", False)]),
            ("Dependency analysis is for?", [("Finding order in computations", True), ("Finding bugs", False), ("Analyzing libraries", False), ("Checking network", False)]),
            ("Instruction scheduling is?", [("Arranging ops to avoid pipeline stalls", True), ("Setting calendar dates", False), ("Mapping keys", False), ("Loading files", False)]),
            ("What is 'Spilling' in registers?", [("Moving variables to memory", True), ("Losing data", False), ("Crashing the app", False), ("Adding registers", False)]),
            ("Interprocedural analysis?", [("Analyzing across functions", True), ("Analyzing within one line", False), ("Analyzing UI", False), ("Analyzing database", False)]),
            ("What is a 'Control Flow Graph'?", [("Graph of all code paths", True), ("A type of spreadsheet", False), ("A network map", False), ("A visual layout", False)]),
            ("Backpatching is used in?", [("One-pass compilers", True), ("Multi-pass compilers", False), ("Interpreters", False), ("Web browsers", False)]),
            ("Vectorization is for?", [("Parallelism", True), ("Compression", False), ("Encryption", False), ("Sorting", False)])
        ],
        "Runtime Environments & Storage": [
            ("What is the 'Stack' in runtime?", [("Storage for function calls", True), ("Storage for global files", False), ("A type of database", False), ("A hardware cable", False)]),
            ("What is the 'Heap' used for?", [("Dynamic memory allocation", True), ("Static code storage", False), ("System logs", False), ("Networking", False)]),
            ("Garbage collection is?", [("Auto memory management", True), ("Deleting files", False), ("Fixing bugs", False), ("Clearing cache", False)]),
            ("What is a 'Memory Leak'?", [("Memory not freed after use", True), ("Physical RAM dripping", False), ("Slow internet", False), ("Hard drive theft", False)]),
            ("Binding refers to?", [("Association of names to addresses", True), ("Connecting cables", False), ("Grouping files", False), ("Locking code", False)]),
            ("Static storage allocation happens at?", [("Compile time", True), ("Runtime", False), ("Install time", False), ("Boot time", False)]),
            ("Stack storage allocation happens at?", [("Runtime", True), ("Compile time", False), ("Boot time", False), ("Ship time", False)]),
            ("What is a 'Dangling Pointer'?", [("Pointer to freed memory", True), ("Unused pointer", False), ("Ghost variable", False), ("Hardware part", False)]),
            ("Buffer overflow is a?", [("Security vulnerability", True), ("Storage feature", False), ("Speed increase", False), ("Design pattern", False)]),
            ("What is the 'Main' function in most runtimes?", [("Starting point", True), ("Ending point", False), ("Error handler", False), ("File loader", False)]),
            ("Linking is?", [("Combining object files into one", True), ("Connecting to Wi-Fi", False), ("Sending emails", False), ("Writing documents", False)]),
            ("Dynamic linking happens?", [("At runtime", True), ("At compile time", False), ("Never", False), ("After install", False)]),
            ("What is 'Scope'?", [("Visibility of names", True), ("Length of code", False), ("Speed of app", False), ("Area of use", False)]),
            ("Global variables reside in?", [("Static area", True), ("Stack", False), ("Heap", False), ("Temp area", False)]),
            ("What is 'Segmentation'?", [("Memory management technique", True), ("Breaking code into lines", False), ("User groups", False), ("Data sorting", False)]),
            ("Virtual memory provides?", [("Address space isolation", True), ("Faster RAM", False), ("More storage", False), ("Better Wi-Fi", False)]),
            ("A 'System Call' is?", [("App requesting service from OS", True), ("A phone call", False), ("An error beep", False), ("An auto update", False)]),
            ("What is 'Fragmentation'?", [("Inefficient memory use", True), ("Data loss", False), ("Broken hardware", False), ("Disk speed", False)]),
            ("Reference counting is for?", [("Garbage collection", True), ("Data math", False), ("Page views", False), ("Loop counting", False)]),
            ("What is the 'Data Segment'?", [("Memory for initialized globals", True), ("Area for local variables", False), ("Disk storage", False), ("Network buffer", False)])
        ],
        "Intermediate Representations": [
            ("What is 'Three-Address Code'?", [("Format with max 3 addresses per op", True), ("A post code", False), ("A hardware limit", False), ("A network tag", False)]),
            ("What is a 'Quadruple'?", [("Four fields to represent logic", True), ("Four variables", False), ("A 4-bit number", False), ("A quad-core CPU", False)]),
            ("A 'Triple' in IR lacks?", [("Explicit result location", True), ("Opcode", False), ("Arg 1", False), ("Arg 2", False)]),
            ("Static Single Assignment (SSA) ensures?", [("Each variable is assigned once", True), ("Speed increase", False), ("Zero errors", False), ("File compression", False)]),
            ("Why use Intermediate Representation?", [("Machine independence", True), ("Speed increase", False), ("Direct hardware execution", False), ("Formatting", False)]),
            ("A Postfix notation is also called?", [("Reverse Polish Notation", True), ("Standard Notation", False), ("Binary Notation", False), ("Hex Notation", False)]),
            ("Control Flow Graphs are?", [("Graphical IR of code", True), ("A type of map", False), ("A data sheet", False), ("A visual layout", False)]),
            ("Symbol tables are used for?", [("Name mapping & type checking", True), ("Storing code", False), ("Running math", False), ("Loading icons", False)]),
            ("What is 'Attribute Grammar'?", [("Augmenting grammar with properties", True), ("Fancy syntax", False), ("New language", False), ("Spelling rules", False)]),
            ("Synthesis phase output is?", [("Target machine code", True), ("Source code", False), ("Tokens", False), ("Error messages", False)]),
            ("Analysis phase output is?", [("Intermediate Representation", True), ("Final binary", False), ("Executable", False), ("User manual", False)]),
            ("Type checking is done using?", [("Semantic rules", True), ("Syntax rules", False), ("Lexical rules", False), ("Spelling rules", False)]),
            ("Code motion is done on?", [("Intermediate code", True), ("Final binary", False), ("Source code", False), ("Comments", False)]),
            ("A DAG represents?", [("Directed Acyclic Graph", True), ("Digital Array Data", False), ("Data Access Grid", False), ("Driven Array Group", False)]),
            ("Backpatching fixes?", [("Forward references", True), ("Old code", False), ("Security", False), ("User bugs", False)]),
            ("A Syntax Tree is a?", [("Hierarchical IR", True), ("Flat file", False), ("Direct bit map", False), ("Logic gate", False)]),
            ("Linear IR includes?", [("Three-address code", True), ("Syntax trees", False), ("Graphs", False), ("Bitmaps", False)]),
            ("Graphical IR includes?", [("Control Flow Graphs", True), ("Quadruples", False), ("Triples", False), ("Linear code", False)]),
            ("Hybrid IR may use?", [("Both trees and linear code", True), ("Only binaries", False), ("Zero logic", False), ("Random data", False)]),
            ("What is 'Optimization' done on IR?", [("High-level optimization", True), ("Hardware wiring", False), ("Disk formatting", False), ("Text editing", False)])
        ]
    }

    for quiz_title, questions in compiler_quizzes.items():
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
    fix_all_placeholders_final_v3()
