from kivy.app import App
from kivy.uix.button import Button



from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter

class myApp(App):
        def build(self):
                fl=FloatLayout(size=(400, 600))
                fl.add_widget(Button(
                        text="Кнопка-1",
                        font_size=25,
                        on_press=self.btn_press,
                        background_color=[1,5,0,1],
                        background_normal='',
                        size_hint=(.5, .25),
                        pos=(200, 120)));

                fl.add_widget(Button(
                        text="Кнопка-2",
                        font_size=22,
                        on_press=self.btn_press,
                        background_color=[1,0,3,1],
                        background_normal='',
                        size_hint=(.5, .25),
                        pos=(200, 320)));
                return fl
        def btn_press(self, instance):
                if instance.text=='Кнопка-1':
                        instance.text='Нажата кнопка-1'
                elif instance.text=='Кнопка-2':
                        instance.text='Нажата кнопка-2'


if __name__=="__main__":
        myApp().run()
