# dialog_manager.py
from memory_manager import MemoryManager

class DialogManager:
    def __init__(self):
        self.memory_manager = MemoryManager()

    def handle_user_input(self, user_input):
        if "remind me" in user_input:
            return self.set_reminder(user_input)
        elif "how are you" in user_input:
            return "I'm here to help you, always!"
        else:
            return "Sorry, I didn't understand that."

    def set_reminder(self, user_input):
        # Simple reminder handling
        reminder_details = user_input.replace("remind me", "").strip()
        self.memory_manager.store_reminder(reminder_details)
        return f"Reminder set for: {reminder_details}"
