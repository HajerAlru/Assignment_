# Geography Quiz Application

# Imports
import random # Import the random module for shuffling questions
import re # Import the re module for regular expression operations

# User Class
class User:
    # Represents a quiz taker and tracks their progress
    def __init__(self, name):  # Set up a new User object
        self.name = name  # Store the user's name for identification
        self.score = 0  # Start the user's score at zero
        self.correct_total = 0  # Count of questions answered correctly, starts at zero
        self.incorrect_total = 0  # Count of questions answered incorrectly, starts at zero

# Question Class
class Question:
    # Stores and manages individual quiz questions.
    def __init__(self, question_text, choices, answer): # Creates a new Question object.
        self.question_text = question_text  # Stores the text of the question.
        self.choices = choices  # Holds all answer choices for the question.
        self.answer = answer # Stores the correct answer key that matches one of the choices

# Quiz Class
class Quiz:
    # Manages the quiz questions including loading questions, tracking the current user, and managing the user's progress through the quiz.
    def __init__(self): # Creates a new Quiz object
        self.questions = self.load_questions()  # Load all available questions into the quiz
        self.current_user = None  # No user assigned yet; this will be set when the quiz starts

    def load_questions(self):
        # Load questions from a predefined list
        questions_data = [
        # Define the questions data as a list of dictionaries
        # Each dictionary contains the question text, possible choices, and the correct answer
            {
                "question": "What is the capital of Australia?",
                "choices": ["A) Sydney", "B) Canberra", "C) Melbourne", "D) Brisbane"],
                "answer": "B"
            },
            {
                "question": "Which river is the longest in the world?",
                "choices": ["A) Amazon", "B) Nile", "C) Yangtze", "D) Mississippi"],
                "answer": "B"
            },
            {
                "question": "What is the largest desert in the world?",
                "choices": ["A) Sahara", "B) Arabian", "C) Gobi", "D) Kalahari"],
                "answer": "A"
            },
            {
                "question": "Which country has the most natural lakes?",
                "choices": ["A) Canada", "B) Russia", "C) USA", "D) India"],
                "answer": "A"
            },
            {
                "question": "What mountain range separates Europe from Asia?",
                "choices": ["A) Andes", "B) Himalayas", "C) Ural Mountains", "D) Rockies"],
                "answer": "C"
            },
            {
                "question": "Which country is known for its pyramids?",
                "choices": ["A) Greece", "B) Egypt", "C) Mexico", "D) Italy"],
                "answer": "B"
            },
            {
                "question": "What is the smallest country in the world?",
                "choices": ["A) Monaco", "B) Vatican City", "C) Nauru", "D) San Marino"],
                "answer": "B"
            },
            {
                "question": "Which ocean is the largest?",
                "choices": ["A) Atlantic Ocean", "B) Indian Ocean", "C) Arctic Ocean", "D) Pacific Ocean"],
                "answer": "D"
            },
            {
                "question": "What is the capital of Japan?",
                "choices": ["A) Beijing", "B) Seoul", "C) Tokyo", "D) Bangkok"],
                "answer": "C"
            },
            {
                "question": "Which of these cities is not a capital?",
                "choices": ["A) Madrid", "B) Berlin", "C) New York", "D) Ottawa"],
                "answer": "C"
            },
            {
                "question": "Which city is known as the Big Apple?",
                "choices": ["A) Los Angeles", "B) Chicago", "C) New York City", "D) San Francisco"],
                "answer": "C"
            },
            {
                "question": "What is the largest island in the world?",
                "choices": ["A) Greenland", "B) New Guinea", "C) Borneo", "D) Madagascar"],
                "answer": "A"
            },
            {
                "question": "Which country has a maple leaf on its flag?",
                "choices": ["A) USA", "B) Canada", "C) Australia", "D) Mexico"],
                "answer": "B"
            },
            {
                "question": "What is the capital of Egypt?",
                "choices": ["A) Cairo", "B) Alexandria", "C) Giza", "D) Luxor"],
                "answer": "A"
            },
            {
                "question": "Which continent is the only one without any deserts?",
                "choices": ["A) Europe", "B) Antarctica", "C) South America", "D) North America"],
                "answer": "B"
            }
        ]
        # Convert each question dictionary into a Question object using list comprehension.
        return [Question(q["question"], q["choices"], q["answer"]) for q in questions_data]

    def start_quiz(self, num_questions):
        # Prepare a set of random questions for the quiz
        random.shuffle(self.questions)  # Shuffle all questions so they appear in random order each time the quiz is started
        return self.questions[:num_questions]  # Return the requested number of questions

    def check_answer(self, question, user_answer):
        # Check if the user's answer is correct and update their score.
        if user_answer.upper() == question.answer: # Convert the user's answer to uppercase for case-insensitive comparison
            # If the answer is correct:
            # Increment the user's score by 1
            self.current_user.score += 1

            # Increment the number of correct answers for the user
            self.current_user.correct_total += 1

            return True # Return True indicating the answer was correct
        else:
            # If the answer is incorrect:
            # Increment the number of incorrect answers for the user
            self.current_user.incorrect_total += 1

            return False # Return False indicating the answer was incorrect

# QuizManager Class
class QuizManager:
    # Manages the overall quiz process, including user interactions and quiz flow
    def __init__(self)# Set up the QuizManager
        self.quiz = Quiz()  # Create a new Quiz instance to manage all quiz-related logic
        self.users = []   # Create an empty list to store all users who participate in the quiz

    @staticmethod
    def get_valid_name():
        # Prompt for and validate the user's name
        while True: # Begins an infinite loop that will continuously prompt the user for a name until a valid one is entered.
            # Prompt the user to enter their name and strip any surrounding whitespace
            name = input("Enter your name: ").strip()
            # Check if the name is empty
            if not name:
                print("Name cannot be empty. Please enter your name.")
            # Check if the name contains only valid characters (letters, spaces, hyphens)
            elif not re.match(r'^[A-Za-z\s-]+$', name):
                print("Name should contain only letters, spaces, and hyphens.")
            # Check if the name length is between 2 and 50 characters
            elif len(name) < 2 or len(name) > 50:
                print("Name should be between 2 and 50 characters long.")
            else:
                # If all checks pass, return the valid name
                return name

    @staticmethod
    def get_valid_input(prompt, valid_options):
        # Prompt for and validate user input against a set of valid options
        while True:  # Begins an infinite loop that will continue until the user provides valid input.
            # Prompt the user for input, strip any surrounding whitespace, and convert to uppercase
            user_input = input(prompt).strip().upper()
            # Check if the input is one of the valid options
            if user_input in valid_options:
                return user_input  # Return the valid input
            # If input is invalid, print a message and repeat the prompt
            print(f"Invalid input. Please enter one of: {', '.join(valid_options)}")

    def run_quiz(self):
        # Main method to run the entire quiz process
        while True: # Begins an infinite loop that will keep the quiz running until the user chooses to stop
            # Display a welcome message at the start of each quiz session
            print("\nWelcome to the Quiz! Let's get started!")
            # Prompt the user for their name and validate the input
            name = self.get_valid_name()
            # Create a new User object for this quiz session and assign it to the quiz
            self.quiz.current_user = User(name)  # Create a new User for this quiz session

            # Ask the user how many questions they would like to answer in the quiz session
            num_questions = int(self.get_valid_input(
                f"This quiz has a total of 15 questions. How many would you like to answer (1-{len(self.quiz.questions)})? ",
                [str(i) for i in range(1, len(self.quiz.questions) + 1)] # List of valid options from 1 to total questions
            ))

            # Retrieve a random set of questions based on the number the user selected
            questions = self.quiz.start_quiz(num_questions)

            # Present each question to the user
            for i, question in enumerate(questions, 1):
                # Display the current question with its index
                print(f"\nQuestion {i}: {question.question_text}")
                # Loop through the choices (answers) for the current question and print each one
                for choice in question.choices:
                    print(choice)
                # Prompt the user to input their answer and validate it (ensure it's A, B, C, or D)
                answer = self.get_valid_input("Your answer (A/B/C/D): ", ['A', 'B', 'C', 'D'])

                # Check the user's answer and provide feedback
                if self.quiz.check_answer(question, answer):
                    print("Correct!") # If the answer is correct, inform the user
                else:
                    # If the answer is incorrect, find the correct answer from the choices
                    correct_answer = next(choice for choice in question.choices if choice.startswith(question.answer))
                    print(f"Incorrect. The correct answer was: {correct_answer}") # Provide feedback with the correct answer

            # After all questions have been answered, show the results for this user
            self.display_results()
            # Add the current user (with their score) to the list of all users who took the quiz
            self.users.append(self.quiz.current_user)

            # Ask if another user wants to take the quiz
            play_again = self.get_valid_input("Would anyone else like to take the quiz? (yes/no): ", ['YES', 'NO'])
            if play_again == 'NO':
                break

        self.display_final_results()  # Show the final results for all users

    def display_results(self):
        # Display the results for the current user
        user = self.quiz.current_user # Get the current user who is taking the quiz
        num_questions = user.correct_total + user.incorrect_total # Total number of questions answered
        percentage = (user.score / num_questions) * 100 # Calculate the percentage score
        print(f"\n{user.name}'s Results:")
        print(f"Score: {user.score}/{num_questions}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Correct Answers: {user.correct_total}")
        print(f"Incorrect Answers: {user.incorrect_total}")

    def display_final_results(self):
        # Display the final results for all users who took the quiz
        if self.users:  # Check if there are any users who have taken the quiz
            print("\nFinal Results:")
            highest_score = max(self.users, key=lambda x: x.score) # Find the user with the highest score
            # Print the highest score, showing the user's name, their score (correct answers), and total questions answered (correct + incorrect)
            print(f"Highest score: {highest_score.name} - {highest_score.score}/{highest_score.correct_total + highest_score.incorrect_total}")

            # Iterate through each user who took the quiz
            for user in self.users:
                total_questions = user.correct_total + user.incorrect_total # Calculate total questions answered by each user
                # Print the user's name, their score, and the total number of questions they answered
                print(f"{user.name}: {user.score}/{total_questions}")

            average_score = sum(user.score / (user.correct_total + user.incorrect_total) for user in self.users) / len(self.users)
            print(f"\nAverage score: {average_score:.2f}")  # Display the score of each user

# Main Execution
if __name__ == "__main__": # Check if this script is being run directly (not imported as a module)
    quiz_manager = QuizManager()  # Create an instance of the QuizManager class to handle the quiz logic
    quiz_manager.run_quiz()  # Start and mangage the quiz process
