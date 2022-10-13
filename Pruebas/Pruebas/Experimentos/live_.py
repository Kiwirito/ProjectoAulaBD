from kaki.app import App
from kivy.factory import Factory
import os

from kivy.uix.screenmanager import ScreenManager


class Live(App):
    
    DEBUG=1
    
    CLASSES = {
        "center_window":"main",
        "LoginWindow":"main",
        "RegisterWindow": "main",
        "StudentWindow": "main",
        "RegisterStudentWindow": "main",
        "HomeWindow": "main",
        "AjustesUsuarioWindow": "main",
        "AjustesEstudiantesWindow": "main",
        "AjustesLider": "main",
        "CommentsWindow": "main",
        "NotificacionesWindow": "main",
        "LiderWindow": "main",
        "CoordinadorWindow": "main",
        "AdministradorWindow": "main",

    }

    KV_FILES = {
        os.path.join(os.getcwd(), "Pruebas/my.kv"),
    }

    AUTORELOADER_PATHS = [
        (".",{"recursive": True})
    ]
    
    def build_app(self):
        return Factory.LoginWindow()
    
Live().run()
    