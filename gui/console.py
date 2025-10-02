'''insert text into gui console'''

class Console:
    '''console class, use to export text into console widget'''
    def __init__(self, main_window):
        self.main_window = main_window

    def console_writing(self, text):
        original_text = self.main_window.console.text()
        self.main_window.console.setText(original_text + "\n" + str(text) + "\n")