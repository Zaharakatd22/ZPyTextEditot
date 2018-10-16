from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.codeinput import CodeInput
from pygments.lexers.html import HtmlLexer
class TextEditorApp(App):
    def build(self):
    	codeinput = CodeInput(lexer=HtmlLexer())
        return codeinput
if __name__ == '__main__':
    TextEditorApp().run()
