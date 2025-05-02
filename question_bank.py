#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
    ("What planet is known as the Red Planet?", "Mars"),
    ("What gas do plants absorb from the atmosphere?", "Carbon Dioxode"),
    ("What is the boiling point of water in Celsius?", "100")
    ("What organ pumps blood through the body?", "Heart"),
    ("What gas do humans exhale?", "Carbon Dioxide"),
    ("What part of the atom has a positive charge?", "Proton"),
    ("What is the chemical symbol for water?", "H2O"),
    ("What galaxy is Earth located in?", "Milky Way"),
    ("What force keeps us on the ground?", "Gravity"),
    ("What planet is closest to the Sun?" "Mercury")
],

}


hints = {
    "Science": [
    "It's named after a Roman god of war.",
    "It's what we exhale.",
    "It’s a round number.",
    "It beats regularly.",
    "Also a greenhouse gas.",
    "It starts with 'P'.",
    "Two hydrogen atoms, one oxygen.",
    "We live in it.",
    "It starts with 'G'.",
    "Not Venus, but..."
]

# Same pattern for history_hints and movie_hints

    
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
    # Add your code here
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
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
def check_answer(player_answer, correct_answer):
    return player_answer.strip().lower() == correct_answer.strip().lower()

    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
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
def remove_question(index, questions_list, answers_list, hints_list):
    del questions_list[index]
    del answers_list[index]
    del hints_list[index]

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
def ask_question(category_name, questions_list, answers_list, hints_list):
    if not questions_list:
        print(f"No more questions in {category_name}.")
        return None, None, None
    
    index = random.randint(0, len(questions_list) - 1)
    print(f"\nCategory: {category_name}")
    print(f"Question: {questions_list[index]}")
    
    
    player_answer = input("Your Answer: ")
    correct = check_answer(player_answer, answers_list[index])


    # Remove used question
    remove_question(index, questions_list, answers_list, hints_list)

    return correct

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
    use_hint = input("Need a hint? (yes/no): ").strip().lower()
    if use_hint == 'yes':
        print(f"Hint: {hints_list[index]}")
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
    if correct:
        print("✅ Correct!")
    else:
        print(f"❌ Incorrect! The correct answer was: {answers_list[index]}")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




