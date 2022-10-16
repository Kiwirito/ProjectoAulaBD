from kivy.properties import StringProperty
from kivymd.uix.fitimage import FitImage
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.card import MDCard


class ListComments(MDCard):
    profile_pic = StringProperty()
    avatar = StringProperty()
    username = StringProperty()
    post = StringProperty()
    caption = StringProperty()
    likes = StringProperty()
    posted_ago = StringProperty()
    comment = StringProperty()

class ImagenIniciativa(FitImage):
    posteo = StringProperty()