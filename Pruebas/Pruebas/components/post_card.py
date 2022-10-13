from kivy.uix.screenmanager import ScreenManager
from kivy.utils import rgba
from kivymd.uix.card import MDCard
from kivy.properties import StringProperty
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from sympy import content
from components.stardialog import Estrellas
from components.options import Opciones
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.list import OneLineAvatarListItem

class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()
    
class PostCard(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    posted_ago = StringProperty()
    comments = StringProperty()
    iden = StringProperty()

    dialog = None
    dialog2 = None

    def show_estrellas(self):
        if not self.dialog:
            self.dialog = MDDialog(
                md_bg_color= rgba("#FFFFFF"),
                title="[color=6200EE]Disfrutaste la iniciativa?[/color]",
                type="custom",
                content_cls = Estrellas(),
                buttons=[
                    MDFlatButton(
                        text="",
                        theme_text_color="Custom",
                        text_color= rgba("#6200EE"),

                    ),
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=rgba("#6200EE"),
                        on_release=self.dialog_close
                    ),
                ],
            )
        self.dialog.open()
           
    def dialog_close(self, *args):
        self.dialog.dismiss(force= True)
        
    def show_opciones(self):
        if not self.dialog2:
            self.dialog2 = MDDialog(
                md_bg_color= rgba("#FFFFFF"),
                radius=[20, 7, 20, 7],
                type="custom",
                content_cls = Opciones()
            )
        self.dialog2.open()
        
    def dialog_closer(self, *args):
        self.dialog2.dismiss(force= True)

        
