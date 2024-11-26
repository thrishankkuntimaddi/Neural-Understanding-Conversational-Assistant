# main.py
from dialog_manager import DialogManager
import speech

if __name__ == "__main__":
    dialog_manager = DialogManager()

    while True:
        user_input = speech.listen_to_user()  # Listen to user input
        response = dialog_manager.handle_user_input(user_input)
        speech.speak(response)  # Provide a response to the user
