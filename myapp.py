from kivy.app import App
from kivy.uix.button import Button


class TestApp(App):
    counter = 0

    def build(self):
        return Button(text='Hello World',
                      font_size=30,
                      on_press=self.btn_press,
                      background_color=[1, 0, 1, 1],
                      background_normal='')

    def btn_press(self, instance):
        self.counter += 1
        instance.text = 'Button pressed %s times' % self.counter


TestApp().run()
