#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("formula of area of rectangle", "Length*width"),
        ("What is the color of chlorophyll","Green")
        # Add more questions as tuples (question, answer)
    ],
    "history":[
        ("When was Pakistan founded","1947"),
        ("When was bangladesh founded","1971"),
        ("When did WWII take place","1939"),
    ],
    "sports": [
        ("How many balls are played in one over of cricket","6"),
        ("Which sports does messi play","Football"),
        ("Kobe Bryant plays which sport","Basketball"),
    ],
}

hints = {
    "Science": [
        ("H"),
        ("Length"),
        ("The color of grass")
        # Pair each question with a corresponding hint.
    ],
    "history": [
        ("close to 1950"),
        ("close to 1970"),
        ("close to 1940"),
    ],
    "sports": [
        ("less than 7"),
        ("played with feet"),
        ("played with hands"),
    ]
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):

    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    random_question = random.choice(questions[category])
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    if player_answer == correct_answer:
        return True
    else :
        return False

    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    player_answer = input("Type your answer: ")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




