class Command:
    def __init__(self, action, undo_action):
        self.action = action
        self.undo_action = undo_action

class CLI:
    def __init__(self):
        self.history = []
        self.redo_stack = []

    def execute_command(self, command):
        self.history.append(command)
        command.action()
        self.redo_stack = []

    def undo(self):
        if not self.history:
            print("No actions to undo.")
            return
        last_command = self.history.pop()
        last_command.undo_action()
        self.redo_stack.append(last_command)

    def redo(self):
        if not self.redo_stack:
            print("No actions to redo.")
            return
        last_command = self.redo_stack.pop()
        self.history.append(last_command)
        last_command.action()

    def list_history(self):
        for i, command in enumerate(self.history):
            print(f"{i+1}: {command.action.__name__}")