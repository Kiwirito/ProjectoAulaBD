import json
from kivy.utils import rgba
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem

from components.post_card import PostCard


class ItemIniciativa(OneLineAvatarIconListItem):
    name = StringProperty()
    

        
class ContentList(BoxLayout):
    pass

class ItemIniciativaWindow(Screen):

    def on_enter(self):
        Mcontent = ContentList()

        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                items = ItemIniciativa(name=username)
                Mcontent.ids.Mcontainer.add_widget(items)

        self.listiniciative = MDDialog(
            md_bg_color= rgba("#FFFFFF"),
            title= "[color=6200EE]Solicitudes recientes:[/color]",
            auto_dismiss= False,
            type="custom", 
            content_cls=Mcontent,
            buttons=[
                    MDRaisedButton(
                        text="[size=14sp]Salir[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#FFFFFF"),
                        on_release= self.salir
                    ),
                ],
            )
        self.listiniciative.open()
    
    def on_leave(self, *args):
        self.listiniciative.dismiss(force = True)
        
    def salir(self, *args):
        self.listiniciative.dismiss(force = True)
        self.manager.transition.direction = "right"
        self.manager.current = "ajustes_coordinador"



