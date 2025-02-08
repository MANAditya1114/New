import streamlit as st
import random
import time

# Dictionary to store user ID and name mapping
if 'user_data' not in st.session_state:
    st.session_state.user_data = {}

# Define your question bank for various languages
question_bank = {
    "C": [
        {"question": "Which function is used to print output in C?", "options": ["Select an answer", "printf()", "print()", "echo()", "cout"], "answer": "printf()"},
        {"question": "What is the default return type of the main() function in C?", "options": ["Select an answer", "void", "int", "float", "char"], "answer": "int"},
        {"question": "Which header file is used for standard I/O operations?", "options": ["Select an answer", "stdio.h", "stdlib.h", "math.h", "string.h"], "answer": "stdio.h"},
        {"question": "Which operator is used to access the value of a variable through a pointer?", "options": ["Select an answer", "", "&", "->", "."], "answer": ""},
        {"question": "What is the correct syntax to declare an array in C?", "options": ["Select an answer", "int arr[10];", "array int arr;", "int[10] arr;", "None"], "answer": "int arr[10];"},
        {"question": "Which symbol is used to comment a single line in C?", "options": ["Select an answer", "//", "/* */", "#", "None"], "answer": "//"},
        {"question": "What does 'void' mean in C?", "options": ["Select an answer", "No return value", "Integer return value", "String return value", "Char return value"], "answer": "No return value"},
        {"question": "Which of these is NOT a valid keyword in C?", "options": ["Select an answer", "volatile", "typedef", "class", "const"], "answer": "class"},
        {"question": "What is the output of: printf(\"%d\", 5+3);", "options": ["Select an answer", "5", "8", "Error", "None"], "answer": "8"},
        {"question": "Which function is used to read a string in C?", "options": ["Select an answer", "scanf()", "gets()", "fgets()", "All of the above"], "answer": "gets()"},
        {"question": "Which of the following is a storage class in C?", "options": ["Select an answer", "auto", "extern", "register", "All of the above"], "answer": "All of the above"},
        {"question": "What does the 'break' statement do in C?", "options": ["Select an answer", "Terminates a loop", "Skips an iteration", "Exits a program", "None"], "answer": "Terminates a loop"},
        {"question": "What is a pointer in C?", "options": ["Select an answer", "A variable that stores the address of another variable", "A special operator", "A data type", "None"], "answer": "A variable that stores the address of another variable"},
        {"question": "Which function is used to dynamically allocate memory?", "options": ["Select an answer", "malloc()", "calloc()", "realloc()", "All of the above"], "answer": "All of the above"},
        {"question": "What is the size of an int data type in C?", "options": ["Select an answer", "2 bytes", "4 bytes", "Depends on compiler", "8 bytes"], "answer": "Depends on compiler"},
        {"question": "What is a segmentation fault?", "options": ["Select an answer", "Accessing memory out of bounds", "Division by zero", "Infinite loop", "Syntax error"], "answer": "Accessing memory out of bounds"},
        {"question": "What is the output of: printf(\"%c\", 65);", "options": ["Select an answer", "A", "65", "Error", "None"], "answer": "A"},
        {"question": "Which of the following is NOT a loop structure in C?", "options": ["Select an answer", "for", "while", "do-while", "foreach"], "answer": "foreach"},
        {"question": "How do you declare a constant in C?", "options": ["Select an answer", "const int a;", "#define a 10", "Both", "None"], "answer": "Both"},
        {"question": "Which operator is used for conditional operations?", "options": ["Select an answer", "?:", "??", "&&", "None"], "answer": "?:"},
        {"question": "What is the purpose of a header file in C?", "options": ["Select an answer", "To declare functions and macros", "To execute code", "To provide memory", "None"], "answer": "To declare functions and macros"},
        {"question": "Which keyword is used to define a macro in C?", "options": ["Select an answer", "#define", "macro", "#macro", "None"], "answer": "#define"},
        {"question": "Which of these operators is used for bitwise AND?", "options": ["Select an answer", "&", "&&", "|", "^"], "answer": "&"},
        {"question": "Which data type can store a single character in C?", "options": ["Select an answer", "char", "int", "string", "None"], "answer": "char"},
        {"question": "What is the result of the expression: 5 == 5?", "options": ["Select an answer", "true", "false", "1", "None"], "answer": "1"},
        {"question": "What is the purpose of the 'return' statement in C?", "options": ["Select an answer", "Exit from a function", "Restart a loop", "Stop compilation", "Allocate memory"], "answer": "Exit from a function"},
        {"question": "Which header file is required for mathematical functions in C?", "options": ["Select an answer", "math.h", "stdio.h", "stdlib.h", "conio.h"], "answer": "math.h"},
        {"question": "What is the default value of a local variable in C?", "options": ["Select an answer", "Garbage value", "0", "Depends on the compiler", "None"], "answer": "Garbage value"},
        {"question": "Which keyword is used to declare a function in C?", "options": ["Select an answer", "void", "function", "define", "None"], "answer": "void"},
        {"question": "What is the output of: printf(\"%d\", sizeof(char));?", "options": ["Select an answer", "1", "2", "4", "8"], "answer": "1"}
    ],
    "C++": [
        {"question": "What is the extension of a C++ source file?", "options": ["Select an answer", ".cpp", ".cxx", ".cc", ".c"], "answer": ".cpp"},
        {"question": "Which of these is used to include a library in C++?", "options": ["Select an answer", "#include", "import", "using", "include"], "answer": "#include"},
        {"question": "Which keyword is used to declare a constant in C++?", "options": ["Select an answer", "const", "final", "static", "immutable"], "answer": "const"},
        {"question": "Which of the following is a correct syntax for defining a function in C++?", "options": ["Select an answer", "int func()", "void func[]", "void func{}", "def func()"], "answer": "int func()"},
        {"question": "What is the size of an integer in C++?", "options": ["Select an answer", "4 bytes", "8 bytes", "2 bytes", "1 byte"], "answer": "4 bytes"},
        {"question": "Which of these is used to create a new object in C++?", "options": ["Select an answer", "new", "create", "instantiate", "object"], "answer": "new"},
        {"question": "Which operator is used to access a class member in C++?", "options": ["Select an answer", "->", ".", "&", "*"], "answer": "."},
        {"question": "Which of the following is not a valid data type in C++?", "options": ["Select an answer", "int", "char", "float", "string"], "answer": "string"},
        {"question": "What is the output of the following C++ code: 'cout << 10 / 3;'", "options": ["Select an answer", "3", "3.333", "3.0", "10/3"], "answer": "3"},
        {"question": "What is the default value of a boolean variable in C++?", "options": ["Select an answer", "true", "false", "0", "undefined"], "answer": "false"},
        {"question": "What is the correct syntax to declare a pointer in C++?", "options": ["Select an answer", "int* ptr;", "int ptr*;", "pointer int;", "int ptr[];"], "answer": "int* ptr;"},
        {"question": "Which of the following operators is used for memory allocation in C++?", "options": ["Select an answer", "new", "malloc", "alloc", "create"], "answer": "new"},
        {"question": "Which of the following is the correct syntax for a 'for' loop in C++?", "options": ["Select an answer", "for (int i = 0; i < 5; i++)", "for int i = 0, i < 5, i++", "for (int i <= 5; i++)", "for int i = 0 to 5"], "answer": "for (int i = 0; i < 5; i++)"},
        {"question": "What is the result of '5 + 5 + '5'' in C++?", "options": ["Select an answer", "55", "15", "10", "Error"], "answer": "55"},
        {"question": "Which of the following is used to handle exceptions in C++?", "options": ["Select an answer", "try-catch", "throw-catch", "catch-finally", "try-except"], "answer": "try-catch"},
        {"question": "What does the 'void' keyword mean in C++?", "options": ["Select an answer", "No value", "Empty function", "Undefined return type", "None of the above"], "answer": "No value"},
        {"question": "What is the purpose of the 'return' statement in C++?", "options": ["Select an answer", "Exit the program", "Return a value from a function", "Pause the program", "Exit from a loop"], "answer": "Return a value from a function"},
        {"question": "Which of the following is a valid syntax for creating a class in C++?", "options": ["Select an answer", "class MyClass {}", "Class MyClass {}", "MyClass class {}", "create MyClass {}"], "answer": "class MyClass {}"},
        {"question": "Which of these is used to access a member of a class through a pointer?", "options": ["Select an answer", "->", ".", ":", "::"], "answer": "->"},
        {"question": "Which of these data types is used to represent a single character in C++?", "options": ["Select an answer", "char", "string", "byte", "int"], "answer": "char"},
        {"question": "What is the result of 'sizeof(int)' in C++?", "options": ["Select an answer", "4", "2", "8", "Depends on the system"], "answer": "4"},
        {"question": "What is the correct way to define a constructor in C++?", "options": ["Select an answer", "MyClass()", "void MyClass()", "MyClass{}", "constructor MyClass()"], "answer": "MyClass()"},
        {"question": "Which of these is used to define an inline function in C++?", "options": ["Select an answer", "inline", "def", "static", "auto"], "answer": "inline"},
        {"question": "What does the keyword 'virtual' do in C++?", "options": ["Select an answer", "Defines a virtual function", "Defines a static function", "Defines a constant", "None of the above"], "answer": "Defines a virtual function"},
        {"question": "Which function is used to dynamically allocate memory in C++?", "options": ["Select an answer", "malloc()", "calloc()", "new", "alloc()"], "answer": "new"},
        {"question": "What is the correct way to declare a vector in C++?", "options": ["Select an answer", "vector<int> vec;", "int vec[];", "vector vec<int>;", "array<int> vec;"], "answer": "vector<int> vec;"},
        {"question": "Which of the following is a valid member of the C++ Standard Library?", "options": ["Select an answer", "vector", "list", "queue", "All of the above"], "answer": "All of the above"},
        {"question": "What is the correct way to define a destructor in C++?", "options": ["Select an answer", "~MyClass()", "MyClass()", "void ~MyClass()", "void MyClass()"], "answer": "~MyClass()"},
        {"question": "Which of these is used to access a member of a structure in C++?", "options": ["Select an answer", ".", "&", "-", "*"], "answer": "."},
        {"question": "What is the purpose of the 'friend' keyword in C++?", "options": ["Select an answer", "Allows access to private members of a class", "Defines a function outside of a class", "Defines a constant", "None of the above"], "answer": "Allows access to private members of a class"},
        {"question": "Which of these is used to call a base class constructor from a derived class in C++?", "options": ["Select an answer", "super()", "base()", "parent()", "constructor()"], "answer": "base()"},
        {"question": "What does 'std::cout' represent in C++?", "options": ["Select an answer", "Standard input", "Standard output", "Standard error", "Standard object"], "answer": "Standard output"},
        {"question": "Which of these operators is used for logical AND in C++?", "options": ["Select an answer", "&&", "&", "and", "&&&"], "answer": "&&"},
        {"question": "What is the purpose of the 'new' operator in C++?", "options": ["Select an answer", "Allocate memory on the heap", "Allocate memory on the stack", "Create an object", "Both 1 and 3"], "answer": "Both 1 and 3"},
        {"question": "Which of these is not a loop in C++?", "options": ["Select an answer", "for", "while", "do-while", "foreach"], "answer": "foreach"},
        {"question": "What is the syntax for a switch statement in C++?", "options": ["Select an answer", "switch (x) { case 1: break; }", "switch x { case 1: break; }", "switch { x: case 1; break; }", "case switch (x) { 1: break; }"], "answer": "switch (x) { case 1: break; }"}
    ],
    "Java": [
        {"question": "What is the extension of compiled Java files?", "options": ["Select an answer", ".class", ".java", ".jar", ".jv"], "answer": ".class"},
        {"question": "What is used to define a class in Java?", "options": ["Select an answer", "class", "Class", "define", "public"], "answer": "class"},
        {"question": "Which keyword is used to inherit a class in Java?", "options": ["Select an answer", "extends", "inherits", "implements", "super"], "answer": "extends"},
        {"question": "What is the size of int in Java?", "options": ["Select an answer", "4 bytes", "2 bytes", "8 bytes", "1 byte"], "answer": "4 bytes"},
        {"question": "Which of these is a reserved keyword in Java?", "options": ["Select an answer", "goto", "var", "constant", "None"], "answer": "goto"},
        {"question": "What is the default value of a boolean variable in Java?", "options": ["Select an answer", "true", "false", "null", "0"], "answer": "false"},
        {"question": "Which of these types cannot be used to define a variable in Java?", "options": ["Select an answer", "int", "char", "double", "float32"], "answer": "float32"},
        {"question": "Which method is the entry point of a Java program?", "options": ["Select an answer", "main()", "init()", "start()", "execute()"], "answer": "main()"},
        {"question": "Which of these is not a primitive data type in Java?", "options": ["Select an answer", "boolean", "int", "char", "String"], "answer": "String"},
        {"question": "Which keyword is used to declare a constant in Java?", "options": ["Select an answer", "constant", "final", "static", "immutable"], "answer": "final"},
        {"question": "What is the default value of a reference variable in Java?", "options": ["Select an answer", "null", "0", "false", "undefined"], "answer": "null"},
        {"question": "Which exception is thrown when a null object reference is accessed?", "options": ["Select an answer", "NullPointerException", "ArrayIndexOutOfBoundsException", "ArithmeticException", "FileNotFoundException"], "answer": "NullPointerException"},
        {"question": "Which of the following is used to create an object in Java?", "options": ["Select an answer", "new", "create", "instantiate", "make"], "answer": "new"},
        {"question": "Which method is used to start a thread in Java?", "options": ["Select an answer", "run()", "execute()", "start()", "init()"], "answer": "start()"},
        {"question": "Which of these classes are part of the java.lang package?", "options": ["Select an answer", "String", "Scanner", "Math", "All of the above"], "answer": "All of the above"},
        {"question": "What is the output of 'System.out.println(10 / 3);' in Java?", "options": ["Select an answer", "3", "3.33", "3.0", "10/3"], "answer": "3"},
        {"question": "What is the result of '5 + 5 + '5'' in Java?", "options": ["Select an answer", "55", "15", "10", "Error"], "answer": "55"},
        {"question": "Which of the following is used to handle errors in Java?", "options": ["Select an answer", "try-catch", "throw-catch", "error-try", "catch-finally"], "answer": "try-catch"},
        {"question": "Which of these is a superclass of all exceptions in Java?", "options": ["Select an answer", "Throwable", "Error", "Exception", "RuntimeException"], "answer": "Throwable"},
        {"question": "Which method is used to read user input from the console in Java?", "options": ["Select an answer", "read()", "next()", "input()", "Scanner()"], "answer": "next()"},
        {"question": "Which of the following is a valid constructor in Java?", "options": ["Select an answer", "public ClassName()", "ClassName()", "ClassName{}", "public void ClassName()"], "answer": "public ClassName()"},
        {"question": "Which collection class is used to store elements in Java?", "options": ["Select an answer", "ArrayList", "HashMap", "Queue", "All of the above"], "answer": "All of the above"},
        {"question": "Which of these is the correct syntax for declaring an array in Java?", "options": ["Select an answer", "int arr[];", "int[] arr;", "arr int[];", "arr[] int;"], "answer": "int[] arr;"},
        {"question": "What is the default value of a local variable in Java?", "options": ["Select an answer", "null", "0", "false", "undefined"], "answer": "undefined"},
        {"question": "What does the keyword 'this' refer to in Java?", "options": ["Select an answer", "The current object", "The parent class", "The method itself", "None of the above"], "answer": "The current object"},
        {"question": "Which of these methods is used to compare two strings in Java?", "options": ["Select an answer", "==", "equals()", "compare()", "compareTo()"], "answer": "equals()"},
        {"question": "Which of these is used to access a member of an interface in Java?", "options": ["Select an answer", "object.method()", "Interface.method()", "Class.method()", "None of the above"], "answer": "Interface.method()"},
        {"question": "What is the base class for all exceptions in Java?", "options": ["Select an answer", "Error", "Throwable", "Exception", "RuntimeException"], "answer": "Throwable"},
        {"question": "Which of these is not a valid access modifier in Java?", "options": ["Select an answer", "private", "protected", "internal", "public"], "answer": "internal"},
        {"question": "Which of these is the correct syntax for the 'for' loop in Java?", "options": ["Select an answer", "for (int i = 0; i < 5; i++)", "for (int i = 0; i <= 5; i++)", "for (i = 0; i < 5; i++)", "for (i; i < 5; ++i)"], "answer": "for (int i = 0; i < 5; i++)"},
        {"question": "Which class is used to handle files in Java?", "options": ["Select an answer", "File", "FileHandler", "FileWriter", "FileReader"], "answer": "File"},
        {"question": "What is the purpose of the 'super' keyword in Java?", "options": ["Select an answer", "To call a superclass constructor", "To call a subclass constructor", "To access superclass members", "Both 1 and 3"], "answer": "Both 1 and 3"},
        {"question": "Which of these is not a valid data type in Java?", "options": ["Select an answer", "int", "float", "boolean", "real"], "answer": "real"}
    ],
    "Python": [
        {"question": "Which of the following is the correct extension for a Python file?", "options": ["Select an answer", ".py", ".python", ".pyt", ".pyc"], "answer": ".py"},
        {"question": "Which of the following is used to print output in Python?", "options": ["Select an answer", "print()", "echo()", "output()", "println()"], "answer": "print()"},
        {"question": "Which of the following is not a valid data type in Python?", "options": ["Select an answer", "int", "char", "float", "str"], "answer": "char"},
        {"question": "How do you declare a variable in Python?", "options": ["Select an answer", "var x = 10", "int x = 10", "x = 10", "declare x = 10"], "answer": "x = 10"},
        {"question": "What is the output of the following Python code: 'print(2 ** 3)'?", "options": ["Select an answer", "5", "6", "8", "16"], "answer": "8"},
        {"question": "What is the result of the expression '5 / 2' in Python?", "options": ["Select an answer", "2", "2.0", "2.5", "3"], "answer": "2.5"},
        {"question": "Which function is used to find the length of a list in Python?", "options": ["Select an answer", "len()", "length()", "size()", "count()"], "answer": "len()"},
        {"question": "What is the correct syntax for a for loop in Python?", "options": ["Select an answer", "for i in range(0, 10):", "for i = 0 to 10:", "for i in 10:", "None of the above"], "answer": "for i in range(0, 10):"},
        {"question": "Which of the following is used to handle exceptions in Python?", "options": ["Select an answer", "try-catch", "try-except", "throw-catch", "catch-finally"], "answer": "try-except"},
        {"question": "Which of the following is a mutable data type in Python?", "options": ["Select an answer", "list", "tuple", "string", "None"], "answer": "list"},
        {"question": "What is the output of the following Python code: 'print(type(3.14))'?", "options": ["Select an answer", "<class 'int'>", "<class 'float'>", "<class 'str'>", "<class 'None'>"], "answer": "<class 'float'>"},
        {"question": "Which keyword is used to define a function in Python?", "options": ["Select an answer", "def", "function", "func", "defn"], "answer": "def"},
        {"question": "Which of the following is used to return a value from a function in Python?", "options": ["Select an answer", "return", "output", "yield", "exit"], "answer": "return"},
        {"question": "Which of these statements is used to break out of a loop in Python?", "options": ["Select an answer", "stop", "exit", "break", "end"], "answer": "break"},
        {"question": "How do you add an element to a list in Python?", "options": ["Select an answer", "list.append(element)", "list.add(element)", "list.push(element)", "list.insert(element)"], "answer": "list.append(element)"},
        {"question": "Which of the following is not a valid Python operator?", "options": ["Select an answer", "&&", "and", "&", "|"], "answer": "&&"},
        {"question": "Which of the following is used to create a class in Python?", "options": ["Select an answer", "class MyClass:", "create MyClass:", "new class MyClass:", "function MyClass:"], "answer": "class MyClass:"},
        {"question": "How do you create a dictionary in Python?", "options": ["Select an answer", "dict = {}", "dict = []", "dict =()", "dict = set()"], "answer": "dict = {}"},
        {"question": "Which of the following is used to convert a string to lowercase in Python?", "options": ["Select an answer", "string.lower()", "string.toLower()", "string.convert()", "string.lowercase()"], "answer": "string.lower()"},
        {"question": "Which of the following is a valid loop structure in Python?", "options": ["Select an answer", "for", "while", "do-while", "All of the above"], "answer": "All of the above"},
        {"question": "What is the result of the expression '3 == 3' in Python?", "options": ["Select an answer", "True", "False", "None", "Error"], "answer": "True"},
        {"question": "What is the default value of a variable in Python?", "options": ["Select an answer", "None", "0", "undefined", "false"], "answer": "None"},
        {"question": "Which of the following is not a Python built-in function?", "options": ["Select an answer", "abs()", "sqrt()", "len()", "append()"], "answer": "append()"},
        {"question": "How do you remove an element from a list in Python?", "options": ["Select an answer", "list.remove(element)", "list.delete(element)", "list.pop(element)", "list.erase(element)"], "answer": "list.remove(element)"},
        {"question": "Which of these is used to access a specific element in a list by index?", "options": ["Select an answer", "[]", "()", "{}", "None"], "answer": "[]"},
        {"question": "Which of the following is used to define an empty set in Python?", "options": ["Select an answer", "set()", "[]", "{}", "()"], "answer": "set()"},
        {"question": "What is the result of '5 + 5 + '5'' in Python?", "options": ["Select an answer", "55", "15", "10", "Error"], "answer": "55"},
        {"question": "Which operator is used to calculate the remainder of a division in Python?", "options": ["Select an answer", "%", "//", "^", "/"], "answer": "%"},
        {"question": "Which of the following is not a valid way to format strings in Python?", "options": ["Select an answer", "f-string", "format()", "concatenation", "printf()"], "answer": "printf()"},
        {"question": "Which of the following statements is used to exit from a function in Python?", "options": ["Select an answer", "return", "exit", "break", "None"], "answer": "return"},
        {"question": "What is the correct way to define a tuple in Python?", "options": ["Select an answer", "(1, 2, 3)", "[1, 2, 3]", "{1, 2, 3}", "None of the above"], "answer": "(1, 2, 3)"},
        {"question": "What is the purpose of the 'yield' keyword in Python?", "options": ["Select an answer", "To return a value from a function", "To create a generator function", "To raise an exception", "None of the above"], "answer": "To create a generator function"},
        {"question": "What does 'len()' function return when used with an empty list?", "options": ["Select an answer", "0", "None", "Error", "False"], "answer": "0"},
        {"question": "Which method is used to remove whitespace from the beginning and end of a string in Python?", "options": ["Select an answer", "strip()", "trim()", "cut()", "none"], "answer": "strip()"},
        {"question": "How do you import a module in Python?", "options": ["Select an answer", "import module", "include module", "using module", "from module import"], "answer": "import module"}
    ]
}

# Define time limits for different levels
level_time_limits = {
    "Easy": 10 * 60,      # 10 minutes
    "Moderate": 7 * 60,   # 7 minutes
    "Hard": 4 * 60        # 4 minutes
}

# Mapping for branch IDs
branch_ids = {
    "CSE": "105", 
    "DS": "104", 
    "AIML": "103", 
    "ECE": "101", 
    "EEE": "100", 
    "CIVIL": "106", 
    "CSE-DS": "107", 
    "CSE-AI": "108", 
    "IT": "109"
}

def generate_user_id(branch, section, roll_no):
    """Generate user ID by combining branch ID, section, and roll number."""
    branch_id = branch_ids.get(branch.upper(), "")
    section = section.upper()
    return f"{branch_id}{section}{roll_no}"

def initialize_quiz(selected_language, selected_level):
    """Initialize the quiz state variables."""
    # Ensure 'answers' is initialized before starting the quiz
    if 'answers' not in st.session_state:
        st.session_state.answers = {}

    # Sample questions for the quiz
    st.session_state.remaining_questions = random.sample(question_bank[selected_language], min(10, len(question_bank[selected_language])))
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.start_time = time.time()
    st.session_state.time_limit = level_time_limits[selected_level]
    st.session_state.quiz_completed = False
    st.session_state.selected_level = selected_level

# Initialize session state variables for quiz flow
if 'quiz_started' not in st.session_state:
    st.session_state.quiz_started = False
if 'quiz_completed' not in st.session_state:
    st.session_state.quiz_completed = False

# Main title
st.title("Multi-Language Quiz Application")

def show_results():
    """Show the quiz results."""
    if 'answers' not in st.session_state:  # Ensure 'answers' is initialized
        st.session_state.answers = {}

    total_questions = len(st.session_state.answers)
    score = sum(1 for ans in st.session_state.answers.values() if ans['selected'] == ans['correct'])
    total_time = time.time() - st.session_state.start_time
    
    st.success(f"Final Score: {score}/{total_questions}")
    st.write(f"Time Taken: {int(total_time // 60)}:{int(total_time % 60):02d}")
    st.write(f"Level: {st.session_state.selected_level}")
    st.write(f"User ID: {st.session_state.user_id}")
    
    # Check if name exists in session state and display it
    if 'user_name' in st.session_state:
        st.write(f"Name: {st.session_state.user_name}")
    else:
        st.write("Name not available.")
    
    st.subheader("Review your answers:")
    for idx, answer in st.session_state.answers.items():
        st.write(f"\nQuestion {idx + 1}: {answer['question']}")
        if answer['selected'] == "Select an answer":
            st.write("Your answer: No answer selected ❌")
        else:
            st.write(f"Your answer: {answer['selected']}")
        st.write(f"Correct answer: {answer['correct']}")
        correct = "✅" if answer['selected'] == answer['correct'] else "❌"
        st.write(f"Result: {correct}")
        st.write("---")

    if st.button("Restart Quiz"):
        st.session_state.quiz_started = False
        st.session_state.quiz_completed = False
        st.session_state.current_question = 0
        st.session_state.answers = {}
        st.rerun()

# Page: Create or Login
option = st.radio("Do you want to create a new account or login?", ("Create Account", "Login"))

# --- Create Account Page ---
if option == "Create Account":
    st.subheader("Create a New User ID")

    # Step 1: Ask for name first
    user_name = st.text_input("Enter your Name:")
    
    if user_name:
        branch = st.selectbox("Select your Branch", list(branch_ids.keys()))
        section = st.text_input("Enter your Section (single letter only, e.g., A, B, K):")
        roll_no = st.text_input("Enter your Roll Number (maximum 66):")
        
        if branch and section and roll_no:
            # Validate section input
            if (len(section) != 1 or not section.isalpha()) and (not roll_no.isdigit() or int(roll_no) > 66):
                st.error("Section must be a single letter (A-Z, a-z) and Roll Number must be a number and cannot exceed 66.")
            elif len(section) != 1 or not section.isalpha():
                st.error("Section must be a single letter (A-Z, a-z).")
            # Validate roll number input
            elif not roll_no.isdigit() or int(roll_no) > 66:
                st.error("Roll Number must be a number and cannot exceed 66.")
            
            else:
                user_id = generate_user_id(branch, section, roll_no)
                
                if user_id not in st.session_state.user_data:
                    # Create user account with ID and Name
                    st.session_state.user_data[user_id] = {"name": user_name, "section": section, "roll_no": roll_no}
                    st.write(f"Your User ID is: {user_id}")
                    
                    # Store name in session state
                    st.session_state.user_name = user_name
                    st.session_state.user_id = user_id
                    
                    # Show success message
                    st.success("Account successfully created! Please go to the Login page to log in.")
                    st.session_state.quiz_started = False
                    st.session_state.quiz_completed = False
                else:
                    st.warning("This User ID already exists. Please log in.")

    # After successful creation, guide to Login page
    st.write("Once you have created an account, please go to the Login page to log in.")
    
# --- Login Page ---
elif option == "Login":
    st.subheader("Login")

    user_id = st.text_input("Enter your User ID:")
    
    if user_id:
        if user_id in st.session_state.user_data:
            user_name = st.session_state.user_data[user_id]["name"]
            st.session_state.user_id = user_id
            st.session_state.user_name = user_name
            st.write(f"Welcome back, {user_name}!")
            
            # Now show the quiz options
            selected_language = st.selectbox("Select a programming language", ["Select"] + list(question_bank.keys()))
            selected_level = st.selectbox("Select Difficulty Level", ["Select", "Easy", "Moderate", "Hard"])
            
            if st.button("Start Quiz"):
                if selected_language != "Select" and selected_level != "Select":
                    initialize_quiz(selected_language, selected_level)
                    st.session_state.quiz_started = True
                    st.rerun()  # Use st.rerun() here to refresh and start the quiz
                else:
                    st.warning("Please select both language and difficulty level.")
        else:
            st.warning("User ID does not exist. Please create a new one.")
            
    st.write("Don't have an account? Please go to the Create Account page to create a new one.")

# --- Quiz ---
if st.session_state.quiz_started and not st.session_state.quiz_completed:
    if 'remaining_questions' in st.session_state:
        remaining_questions = st.session_state.remaining_questions
        current_question = st.session_state.current_question
        total_questions = len(remaining_questions)
        
        elapsed_time = time.time() - st.session_state.start_time
        time_left = max(0, st.session_state.time_limit - elapsed_time)
        
        if time_left <= 0:
            st.warning("Time's up!")
            st.session_state.quiz_completed = True
            show_results()
        else:
            st.write(f"Time Left: {int(time_left // 60):02d}:{int(time_left % 60):02d}")
            
            st.subheader(f"Question {current_question + 1}/{total_questions}")
            question = remaining_questions[current_question]
            st.write(question['question'])
            
            # Default selected answer
            default_index = 0
            if current_question in st.session_state.answers:
                try:
                    default_index = question['options'].index(st.session_state.answers[current_question]['selected'])
                except ValueError:
                    default_index = 0
            
            user_answer = st.radio("Select your answer:", question['options'], index=default_index, key=f"q_{current_question}")
            
            col1, col2 = st.columns(2)
            
            if current_question > 0:
                if col1.button("Previous"):
                    # Save the current answer before going to the previous question
                    st.session_state.answers[current_question] = {
                        "question": question["question"],
                        "selected": user_answer,
                        "correct": question["answer"]
                    }
                    st.session_state.current_question -= 1
                    st.rerun()  # Use st.rerun() here to go to the previous question
            
            if col2.button("Next"):
                # Save the current answer when moving to the next question
                st.session_state.answers[current_question] = {
                    "question": question["question"],
                    "selected": user_answer,
                    "correct": question["answer"]
                }
                if current_question < total_questions - 1:
                    st.session_state.current_question += 1
                else:
                    st.session_state.quiz_completed = True
                st.rerun()  # Use st.rerun() here to go to the next question
            
            progress = (current_question + 1) / total_questions
            st.progress(progress)

# If quiz is completed, show the results
if st.session_state.quiz_completed:
    show_results()
