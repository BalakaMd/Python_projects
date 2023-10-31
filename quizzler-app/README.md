# Quizzler App

## Introduction

Welcome to Quizzer, a simple quiz application that uses questions fetched from the Open Trivia Database API. This Python project is built with a graphical user interface using the Tkinter library.

## Project Overview

Quizzer is a basic quiz application that allows users to answer multiple-choice questions and provides immediate feedback on their answers. Here's an overview of the key components of the project:

- **Question Fetching**: The application fetches questions from the Open Trivia Database API based on user-defined parameters (e.g., the number of questions and the question type, which can be changed by modifying the `params` dictionary in the `data.py` file).

- **User Interface**: The user interface is created with Tkinter, offering a simple and intuitive design. Users can answer questions by clicking on the "True" or "False" buttons.

- **Scoring**: Users receive instant feedback on whether their answer is correct or incorrect, and their score is updated accordingly. The score is displayed on the interface.

- **Question Parsing**: Questions and answers are parsed from HTML entities to ensure proper display on the interface.

## Screenshots

![Screenshot 1](/screenshots/quizzer.png)

## Getting Started

To run Quizzer on your local machine, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://BalakaMd/Python_projects/quizzler-app.git
   ```

2. Install the required dependencies:

   ```shell
   pip install requests
   ```

3. Run the application:

   ```shell
   python main.py
   ```

## Usage

1. Launch the application using the steps outlined in the "Getting Started" section.

2. A window will appear with the first question. Read the question carefully.

3. Click the "True" or "False" button to answer the question.

4. You will receive instant feedback on your answer, and your score will be updated.

5. Continue answering questions until you reach the end.

6. Once you've answered all the questions, your final score will be displayed.

## Customization

You can customize the quiz by modifying the parameters in the `params` dictionary in the `data.py` file.
You can change the number of questions and the question type (e.g., multiple-choice, true/false) based on your preferences.

```python
params = {
    "amount": 10,    # Change the number of questions here
    "type": "boolean"  # Change the question type here (e.g., "multiple" for multiple-choice)
}
```

## Acknowledgments

- This project uses questions from the [Open Trivia Database](https://opentdb.com/api_config.php) API.

## Feedback and Contributions

If you have any feedback or want to contribute to this project, please feel free to submit issues
or pull requests on the [GitHub repository](https://github.com/BalakaMd/Python_projects/quizzler-app).

---

Enjoy your quiz experience with Quizzer! If you have any questions or encounter issues, please don't hesitate to reach out.

Thank you for using Quizzler-App!
