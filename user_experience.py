#---------------------------------------
#  User Experience
#    Student C
#---------------------------------------


#---------------------------------------
import random
def choose_difficulty():
    """
    Allows players to choose the difficulty level of the questionsThe user is going to input their choice.

    Parameters: None
    Returns:
    - str: Valid difficulty levels are ('easy', 'medium', 'hard').
    """
    #------------------------
    # Add your code here
    #------------------------
    print("select difficulty level:")
    print("1.easy")
    print("2.medium")
    print("3.hard")
    while True:
        choice = input("enter 1, 2 or 3:")
        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("invalid choice!")

selected_difficulty = choose_difficulty()
print("you have chosen", selected_difficulty, "!")
    #------------------------

#---------------------------------------

def display_leaderboard(leaderboard):
    """
    Displays the leaderboard, showing top scores in descending order.

    Parameters:
    - leaderboard (dict): A dictionary containing player names as keys and their scores as values.

    Returns: None

    The function sorts the leaderboard by scores in descending order and prints the names and scores of the top players. If the leaderboard is empty, it prints a message indicating that there are no scores to display.
    """
    #------------------------
    # Add your code here
    #------------------------
    if not leaderboard:
        print("no scores to display!")
        return
    sorted_leaderboard = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)
    print("leaderboard:")
    for rank, (player, score) in enumerate(sorted_leaderboard, start=1):
        print(f"{rank}. {player}: {score}")

leaderboard = {
    "qasim": 69,
    "ahad": 34,
    "raza": 71,
    "mir": 42,
    "zain": 87
}
display_leaderboard(leaderboard)
    #------------------------

#---------------------------------------

def save_score(player_name, score, file_path='scores.txt'):
    """
    Saves the player's score to a file.

    Parameters:
    - player_name (str): The name of the player.
    - score (int): The score achieved by the player.
    - file_path (str): The file path to save the score.

    Returns: None
    """
    #------------------------
    # Add your code here
    #------------------------
    with open(file_path, 'a') as file:
        file.write(f'{player_name}: {score}\n')

save_score('ahmed', 99)
save_score('kamal', 65, 'high_scores.txt')
    #------------------------

#---------------------------------------

def load_top_scores(file_path='scores.txt'):
    """
    Loads the top scores from a file into a leaderboard dictionary.

    Parameters:
    - file_path (str): The file path from which to load the scores.

    Returns:
    - dict: The leaderboard dictionary with player names as keys and scores as values.
    """
    #------------------------
    # Add your code here
    #------------------------
    leaderboard = {}
    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split(':')
                if len(parts) == 2:
                    player_name = parts[0].strip()
                    score = int(parts[1].strip())
                    leaderboard[player_name] = score
    except FileNotFoundError:
        print(f"File '{file_path}' not found. Returning an empty leaderboard.")
    return leaderboard

top_scores = load_top_scores('high_scores.txt')
print(top_scores)
    #------------------------

#---------------------------------------

def provide_feedback(is_correct):
    """
    Provides feedback to the player after each round.

    Parameters:
    - is_correct (bool): Indicates whether the player's answer was correct.

    Returns: None

    Example:
    - is it correct?   "Well done!"
    - is it incorrect? "Sorry, that's incorrect."
    """
    #------------------------
    # Add your code here
    #------------------------
    if is_correct:
        print("Well done!")
    else:
        print("Sorry, that's incorrect.")

provide_feedback(True)
provide_feedback(False)
    #------------------------

#---------------------------------------

def fifty_fifty_lifeline(correct_answer, options):
    """
    Provides a 50/50 lifeline by removing two incorrect answers, leaving the correct answer and one other incorrect answer.

    Parameters:
    - correct_answer (str): The correct answer to the current question.
    - options (list): A list containing all possible answers including the correct answer.

    Returns:
    - list: A reduced list of answers containing only the correct answer and one randomly selected incorrect answer.

    This function is designed to be used once per game session by a player who chooses to use the 50/50 lifeline. It randomly selects one incorrect answer to keep along with the correct answer and removes the other options.
    """
    #------------------------
    # Add your code here
    #------------------------
    remaining_options = options.copy()
    remaining_options.remove(correct_answer)
    incorrect_to_keep = random.choice(remaining_options)
    remaining_options.remove(incorrect_to_keep)
    remaining_options.append(correct_answer)
    random.shuffle(remaining_options)
    return remaining_options

correct_answer = "B"
options = ["A", "B", "C", "D"]
reduced_options = fifty_fifty_lifeline(correct_answer, options)
print(reduced_options)
    #------------------------

#---------------------------------------

def skip_question(allowed_skips):
    """
    Allows the player to skip a question during the game.

    Parameters:
    - allowed_skips (int): The number of skips available to the player.

    Returns:
    - bool: True if the skip was successful (and a skip was available), False otherwise.

    This function checks if the player has any skips available. If so, it decrements the allowed_skips counter and returns True, indicating the question can be skipped. If no skips are available, it returns False. This function should be called before presenting a new question to the player.
    """
    #------------------------
    # Add your code here
    #------------------------
    if allowed_skips > 0:
        allowed_skips -= 1
        print(f"You have used a skip. {allowed_skips} skip(s) remaining.")
        return True
    else:
        print("Sorry, no skips remaining.")
        return False

skips_remaining_example = 2
skip_successful = skip_question(skips_remaining_example)
print("Question skipped:", skip_successful)
    #------------------------

#---------------------------------------