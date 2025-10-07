'''insert text into gui console'''

class Console:
    '''console class, use to export text into console widget'''
    def __init__(self, main_window):
        self.main_window = main_window

    def console_writing(self, text):
        current_text = self.main_window.console.text()
        new_text = current_text + str(text) + '\n'
        self.main_window.console.setText(new_text)