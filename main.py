
import logging
from kivymd.app import MDApp
from kivy.uix.widget import Widget
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton
from ml_util import MLUtil
import logging


class UI(Screen, MDBoxLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        self.label = MDLabel(
            text='Lorem Ipsum Dolor',
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )

        self.word = MDTextField(
            hint_text='word',
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )

        self.temp = MDTextField(
            hint_text='temp',
            pos_hint={'center_x': 0.5, 'center_y': 0.7}
        )

        self.num = MDTextField(
            hint_text='num',
            pos_hint={'center_x': 0.5, 'center_y': 0.6}
        )

        self.generate = MDRectangleFlatButton(
            text='generate lyrics',
            pos_hint={'center_x': 0.5, 'center_y': 0.5}
        )
        self.generate.bind(on_press=self.on_generate_press)

        self.res_label = MDLabel(
            text='Lorem Ipsum Dolor',
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            size_hint=[1.0, None],
        )

        self.add_widget(self.label)
        self.add_widget(self.word)
        self.add_widget(self.temp)
        self.add_widget(self.num)
        self.add_widget(self.generate)
        self.add_widget(self.res_label)

    def on_generate_press(self, instance):
        num_generate = self.num.text
        temperature = self.temp.text
        start_string = self.word.text

        ml_util = MLUtil()
        logging.info("ML Gen res:")
        gen_res = ml_util.generate_text(
            num_generate, temperature, start_string)

        self.res_label.text = gen_res


class MyApp(MDApp):

    def build(self):
        self.sm = ScreenManager()
        self.ui_screen = UI(
            name='first', orientation='vertical'
        )
        self.sm.add_widget(self.ui_screen)
        return self.sm


MyApp().run()
