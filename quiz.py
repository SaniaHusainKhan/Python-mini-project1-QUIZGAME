def play_quiz(subject, questions):
    score = 0
    print(f"\n Starting quiz on {subject}...\n")

    for question, correct_answer in questions.items():
        answer = input(question)
        if answer.lower().strip() == correct_answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f" Incorrect! The right answer was: {correct_answer}\n")

    print("You got " + str(score) + " questions correct!")
    print("Your score: " + str((score / len(questions)) * 100) + "%\n")


print(" WELCOME TO MY COMPUTER QUIZ GAME ")

playing = input("Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    quit()

quizzes = {
    "1": ("Software Project Development", {
        "What is the first phase of Software Development Life Cycle? ": "planning",
        "Which model is also known as the linear sequential model? ": "waterfall",
        "Which document defines functional and non-functional requirements? ": "srs",
        "Agile methodology is based on which type of development? ": "iterative",
        "Which tool is commonly used for version control? ": "git"
    }),
    "2": ("Internet Of Things", {
        "IoT stands for? ": "internet of things",
        "Which communication protocol is lightweight and used in IoT? ": "mqtt",
        "Which layer of IoT architecture handles data storage and analysis? ": "application layer",
        "A smart watch is an example of? ": "wearable technology",
        "Which cloud platform is widely used for IoT? (AWS, Azure, etc.) ": "aws"
    }),
    "3": ("Emerging Technologies", {
        "Blockchain is primarily associated with which digital currency? ": "bitcoin",
        "5G is the next generation of which technology? ": "wireless communication",
        "Which technology enables virtual try-on experiences in shopping apps? ": "augmented reality",
        "Quantum computing is based on units called? ": "qubits",
        "Which energy source is considered a major part of green technology? ": "solar"
    }),
    "4": ("Artificial Intelligence", {
        "AI stands for? ": "artificial intelligence",
        "Which algorithm is used in training neural networks? ": "backpropagation",
        "Siri and Alexa are examples of? ": "virtual assistants",
        "Which branch of AI focuses on enabling machines to see? ": "computer vision",
        "Which company created the AI model GPT? ": "openai"
    }),
    "5": ("AWD", {
        "HTML stands for? ": "hypertext markup language",
        "Which language is used to style web pages? ": "css",
        "Which scripting language runs in the browser? ": "javascript",
        "Which database is commonly used with PHP? ": "mysql",
        "Which protocol is used for secure data transfer over the web? ": "https"
    })
}

# Game loop
while True:
    print("\n Choose a subject for your quiz:")
    print("1. Software Project Development")
    print("2. Internet Of Things")
    print("3. Emerging Technologies")
    print("4. Artificial Intelligence")
    print("5. AWD")
    print("6. Exit Game\n")

    choice = input("Enter your choice (1-6): ")

    if choice in quizzes:
        subject, questions = quizzes[choice]
        play_quiz(subject, questions)
    elif choice == "6":
        print("\n Thanks for playing! Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
