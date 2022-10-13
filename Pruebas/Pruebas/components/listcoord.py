from kivy.properties import StringProperty

from kivymd.uix.list import OneLineAvatarIconListItem, IRightBodyTouch
from kivymd.uix.selectioncontrol import MDCheckbox


class Item(OneLineAvatarIconListItem):
    name = StringProperty()

class RightCheckbox(IRightBodyTouch, MDCheckbox):
    pass
    


