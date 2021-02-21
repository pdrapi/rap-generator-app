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
    ## Creates main screen along with the widgets
    
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)

        self.label = MDLabel(
            text='Rap Lyrics Generator',
            halign='center',
            font_style='H5',
            pos_hint={'center_x': 0.5, 'center_y': 0.95}
        )
        self.label_word = MDLabel(
            text='Type in one word for lyric generator',
            font_style='Overline',
            pos_hint={'center_x': 0.5, 'center_y': 0.9}
        )
        self.word = MDTextField(
            hint_text='Type the word here',
            helper_text="This will disappear when you click off",
            helper_text_mode="on_focus",
            pos_hint={'center_x': 0.5, 'center_y': 0.85}
        )
        self.label_temp = MDLabel(
            text='Type in a float between 0.1 and 2. This will determine how random the text will be. 0.1 = least random, 2 = most random.',
            font_style='Overline',
            pos_hint={'center_x': 0.5, 'center_y': 0.8}
        )
        self.temp = MDTextField(
            hint_text='temp',
            helper_text="This will disappear when you click off",
            helper_text_mode="on_focus",
            pos_hint={'center_x': 0.5, 'center_y': 0.75}
        )
        self.label_num = MDLabel(
            text='Type in a number of characters you want to generate. The limit is 1000.',
            font_style='Overline',
            pos_hint={'center_x': 0.5, 'center_y': 0.70}
        )
        self.num = MDTextField(
            hint_text='num',
            helper_text="This will disappear when you click off",
            helper_text_mode="on_focus",
            pos_hint={'center_x': 0.5, 'center_y': 0.65}
        )

        self.generate = MDRectangleFlatButton(
            text='Generate lyrics',
            pos_hint={'center_x': 0.5, 'center_y': 0.6}

        )
        self.generate.bind(on_press=self.on_generate_press)

        self.res_label = MDLabel(
            text='Here you will see your lyrics',
            font_style="Overline",
            halign="center",
            pos_hint={'center_x': 0.5, 'center_y': 0.25},
            size_hint=[1.0, None],
        )

        self.add_widget(self.label)
        self.add_widget(self.label_word)
        self.add_widget(self.word)
        self.add_widget(self.label_temp)
        self.add_widget(self.temp)
        self.add_widget(self.label_num)
        self.add_widget(self.num)
        self.add_widget(self.generate)
        self.add_widget(self.res_label)
    
    def on_generate_press(self, instance):
        # takes input from the user and calls generate_text()
       
        num_generate = self.num.text
        temperature = self.temp.text
        start_string = self.word.text

        ml_util = MLUtil()
        logging.info("ML Gen res:")
        gen_res = ml_util.generate_text(
            num_generate, temperature, start_string)

        self.res_label.text = gen_res


class MyApp(MDApp):
    #Builds the app

    def build(self):
        self.sm = ScreenManager()
        self.ui_screen = UI(
            name='first', orientation='vertical'
        )
        self.sm.add_widget(self.ui_screen)
        return self.sm


MyApp().run()
