Geography Quiz Program - README
===============================

Description:
----------------
This Geography Quiz Program is an interactive console-based quiz game designed to test the user's knowledge of geography.
Users can specify the number of questions they want to answer, choose from multiple-choice options, and receive a score at the end of the quiz.
The program supports multiple participants in a single session and keeps track of each user's score.

----------------
Features:
----------------
Users can enter their names and track their progress throughout the quiz.
The quiz consists of a predefined set of geography questions, which are randomly shuffled for each session.
The application keeps track of the user's score, the number of correct and incorrect answers, and calculates the percentage score.
After completing the quiz, users can view their results, and the application can display final results for all users who participated.

----------------
Structure:
----------------
The application is structured into several classes:
User Class: Represents a quiz taker, storing their name, score, and counts of correct and incorrect answers.
Question Class: Represents individual quiz questions, including the question text, possible choices, and the correct answer.
Quiz Class: Manages the quiz process, including loading questions and tracking user progress.
QuizManager Class: Handles user interactions and manages the overall flow of the quiz.

----------------
Usage:
----------------
1. Run the program using Python.

2. When prompted, enter your name to personalize the quiz experience. Names must be between 2 and 50 characters.

3. Specify the number of questions you would like to attempt (1-15).

4. Answer each question by typing the letter corresponding to your chosen answer (A, B, C, or D).

5. At the end of the quiz, your score will be displayed, showing the number of correct answers out of the total attempted questions, along with the percentage score.

6. If multiple users want to take the quiz in the same session, the program will prompt for a new user to enter their name and repeat the process.

7. When no additional participants wish to take the quiz, the program displays a summary of results, including:
- The highest score achieved.
- A list of all scores.
- The average score of all users.

----------------
Example Session:
----------------
Here is an example output from a session with two participants:

Welcome to the Quiz! Let's get started!

Enter your name: Alex

How many questions would you like to answer (1-15)? 1

Question 1: What is the largest desert in the world?
A) Sahara
B) Arabian
C) Gobi
D) Kalahari
Your answer: A
Correct!

Alex's Results:
Score: 1/1 (100%)

Would anyone else like to take the quiz? (yes/no): yes

Welcome to the Quiz! Let's get started!

Enter your name: Sam

How many questions would you like to answer (1-15)? 1

Question 1: What is the capital of Brazil?
A) São Paulo
B) Rio de Janeiro
C) Brasilia
D) Salvador
Your answer: A
Incorrect. The correct answer was: C) Brasilia

Sam's Results:
Score: 0/1 (0%)

Would anyone else like to take the quiz? (yes/no): no

Final Results:
Highest Score: Alex - 1/1
Alex: 1/1
Sam: 0/1
Average Score: 0.50

----------------
Requirements:
----------------
Ensure Python 3.x is installed on your system.
Basic knowledge of running scripts in a command-line environment.

Future Enhancements
Potential improvements to expand functionality:

Adding difficulty levels for questions.
Implementing a timer for each question.
Storing user data and questions in a database for scalability.
Developing a graphical user interface (GUI).

----------------
Credits:
----------------
Questions sourced from publicly available geography question banks.
Uses Python’s random module for shuffling questions.
Includes Python’s re module for validating user input.
