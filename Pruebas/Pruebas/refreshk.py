import json
from kivymd.app import MDApp
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.properties import StringProperty

from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout

from kivymd.uix.button import MDIconButton
from kivymd.icon_definitions import md_icons
from kivymd.uix.list import ILeftBodyTouch, OneLineIconListItem, OneLineAvatarIconListItem
from kivymd.theming import ThemeManager
from kivymd.utils import asynckivy

Builder.load_string('''
<ItemForList>
    text: root.text

    IconLeftSampleWidget:
        icon: root.icon

    ImageRightWidget:
        source: root.avatar


<Example@FloatLayout>

    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: app.title
            md_bg_color: app.theme_cls.primary_color
            background_palette: 'Primary'
            left_action_items: [['menu', lambda x: x]]

        MDScrollViewRefreshLayout:
            id: refresh_layout
            refresh_callback: app.refresh_callback
            root_layout: root

            GridLayout:
                id: box
                size_hint_y: None
                height: self.minimum_height
                cols: 1
''')


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class ItemForList(OneLineAvatarIconListItem):
    icon = StringProperty()
    avatar = StringProperty()


class screenmanager(ScreenManager):
    pass

class Example(MDApp):
    title = 'Example Refresh Layout'
    screen = None
    x = 0
    y = 15

    def build(self):
        #sm = ScreenManager()
        Factory.register('ertt', cls=screenmanager)
        screr = Factory.ertt()
        self.screen = screr
        self.set_list()

        return self.screen

    def set_list(self):
        #async def set_list():
        #    names_icons_list = list(md_icons.keys())[self.x:self.y]
        #    for name_icon in md_icons:
        #        await asynckivy.sleep(0)
        #        self.screen.ids.box.add_widget(
        #            ItemForList(icon=name_icon, text=name_icon))
        #asynckivy.start(set_list())

        with open('Pruebas/assets/data/posts.json') as f_obj:
                    data = json.load(f_obj)
                    for username in data:
                        self.screen.ids.box.add_widget(ItemForList(
                            text = username,
                            icon = "account",
                            avatar = data[username]["avatar"]
                        ))

    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.screen.ids.box.clear_widgets()
            if self.x == 0:
                self.x, self.y = 15, 30
            else:
                self.x, self.y = 0, 15
            self.set_list()
            self.screen.ids.refresh_layout.refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)


Example().run()