
#xd
from asyncio.windows_events import NULL
from cProfile import label
import json

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from select import select

#Video Player
import os
os.environ["KIVY_VIDEO"] = "ffpyplayer"

#Sql
import mysql.connector

#Cloudinary
import cloudinary
import cloudinary.uploader
import cloudinary.api

#File Picker
from plyer import filechooser

#Request Api
import requests

#Regex
import re

#Kivy UIX
from kivy.utils import rgba
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.pickers import MDDatePicker
from components.comments import ListComments
from components.post_card import PostCard
from components.stardialog import Estrellas
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog


#Window
import sys
from win32api import GetSystemMetrics

#Tamaño de la ventana
#Default Mac 412,892
Window.size = (412,892)
imagenP = "https://fotografias.antena3.com/clipping/cmsimages01/2021/09/30/0F7B0DA6-1E5E-4F1A-8421-86443596D1DE/98.jpg?crop=1024,576,x0,y10&width=1900&height=1069&optimize=high&format=webply"
screenx = GetSystemMetrics(0)
screeny = GetSystemMetrics(1)

def center_window(sizex,sizey):
    Window.size = (sizex, sizey)
    Window.left = (screenx - sizex)/2
    Window.top = (screeny - sizey)/2

class LoginWindow(Screen):
    
    #Mostrar/Esconder contraseña
    passwdinput = ObjectProperty(None)
    def visibilidad(self):
        if self.passwdinput.password == True:
            self.passwdinput.password = False

        elif self.passwdinput.password == False:
            self.passwdinput.password = True
            
class RegisterWindow(Screen):
    
    #Calendario
    def abrircalendario(self):
        ventanadate = MDDatePicker(year = 2003, month=4, day= 23)
        ventanadate.bind(on_save = self.on_save)
        ventanadate.primary_color = rgba("#6200EE")
        ventanadate.selector_color = rgba("#6200EE")
        ventanadate.text_color = rgba("#23036A")
        ventanadate.accent_color = rgba("#F2E7FE")
        ventanadate.open()
    
    calendarior = ObjectProperty(None)
    def on_save(self, instance, value, date_range):
        self.calendarior.text = str(value)

    def buscar_tipo_usuario(self, correo):
        self.cursor.execute("select * from usuario")
        correo_list = []
        for i in self.cursor.fetchall():
            correo_list.append(i[1])
        if correo.text in correo_list and correo_list != "":
            self.cursor.execute(f"select u_tipo from usuario where u_correo='{correo.text}'")
            for j in self.cursor:
                if "Usuario" == j[0]:
                    return "Usuario"
                elif "Administrador" == j[0]:
                    return "Administrador"
                elif "Coordinador" == j[0]:
                    return "Coordinador"
                elif "Estudiante" == j[0]:
                    return "Estudiante"
                
    dialog = None

    def show_error_register(self, contra1,contra2):
        contra1.text = ""
        contra2.text = ""

        if not self.dialog:
            self.dialog = MDDialog(
                md_bg_color= rgba("#FFFFFF"),
                title="[color=6200EE]Datos Invalidos[/color]",
                text="[color=6200EE]Las contraseña no coinciden o no son validas, vuelve a digitarlas.[/color]",
                type="custom",
                buttons=[
                    MDFlatButton(text="OK", theme_text_color="Custom", text_color=rgba("#6200EE"), on_release= self.submit),
                ],
            )
        self.dialog.open()
        
    def submit(self, *args):
        self.dialog.dismiss(force = True)

class StudentWindow(Screen):
    pass

class RegisterStudentWindow(Screen):
    pass

class HomeWindow(Screen):
    profile_picture = imagenP
    
    def on_enter(self):
        self.list_posts()
        self.list_notification()

    def list_posts(self):

        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.timeline.add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                    iden = data[username]['id']
                ))
                
    def list_notification(self):
        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.listnotification.add_widget(ListComments(
                    username = username,
                    avatar = data[username]['avatar'],
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                ))        
    

class AjustesUsuarioWindow(Screen):
    usuario = "Usuario"
    pass

class AjustesEstudiantesWindow(Screen):
    pass

class AjustesLider(Screen):
    pass

            
class CommentsWindow(Screen):
    
    def on_enter(self):
        self.list_comments()


    def list_comments(self):
        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.ids.listcomment.add_widget(ListComments(
                    username = username,
                    avatar = data[username]['avatar'],
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    comments = data[username]['comments'],
                    posted_ago = data[username]['posted_ago'],
                ))

    dialog = None

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
                        on_release= self.dialog_close
                    ),
                ],
            )
        self.dialog.open()
        
    def dialog_close(self, *args):
        self.dialog.dismiss(force= True)

class NotificacionesWindow(Screen):
    pass

class LiderWindow(Screen):
    pass 
      
class IniciativaWindow(Screen):
    
    
    def file_chooser(self):
        filechooser.open_file(on_selection= self.selected)
        
    def selected(self, selection):
        result = cloudinary.uploader.upload(selection[0], folder= "iniciativas")
        url = result.get("url")
    
class CoordinadorWindow(Screen):
    pass

class AdministradorWindow(Screen):
    pass

class FormularioWindow(Screen):
    pass

class KivyApp(MDApp):
    profile_picture = imagenP

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    #database = mysql.connector.Connect(host= '192.168.1.10', user= 'jmeza', password = '123', database = 'RELACIONALDB')
    #cursor = database.cursor()

    
    
    valor = True
    gris = "#7C8085"
    blancop = "#F2E7FE"
    purpura = "#6200EE"
    purpuraOscuro = "#23036A"
     
    def build(self):
        center_window(412,892)
        #Tema del App
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Dark"
        
        #Load

        Builder.load_file("my.kv")
        Builder.load_file('components/appbar.kv')
        Builder.load_file('components/post_card.kv')
        Builder.load_file('components/bottom_nav.kv')
        Builder.load_file('components/stardialog.kv')
        Builder.load_file('components/comments.kv')
        Builder.load_file('components/options.kv')


        sm = ScreenManager()
        sm.add_widget(LoginWindow(name='login'))
        sm.add_widget(RegisterWindow(name='register'))
        sm.add_widget(StudentWindow(name='student'))
        sm.add_widget(RegisterStudentWindow(name='registerstudent'))
        sm.add_widget(HomeWindow(name='home'))
        sm.add_widget(AjustesUsuarioWindow(name='ajustes_usuario'))
        sm.add_widget(AjustesEstudiantesWindow(name='ajustes_estudiantes'))
        sm.add_widget(AjustesLider(name='ajustes_lider'))
        sm.add_widget(CommentsWindow(name='comments'))
        sm.add_widget(LiderWindow(name='lider'))
        sm.add_widget(NotificacionesWindow(name='notifications'))
        sm.add_widget(CoordinadorWindow(name='coordinador'))
        sm.add_widget(AdministradorWindow(name='administrador'))
        sm.add_widget(IniciativaWindow(name='iniciativa'))
        sm.add_widget(FormularioWindow(name='formulario'))

        sm.current = "lider"
        
        return sm
    
                
    def registar_datos(self, correo, passwd):
        
        xd = "Usuario"
        try:
            if re.fullmatch(self.regex, correo.text):
                self.cursor.execute(f"insert into usuario values('{NULL}','{correo.text}', '{passwd.text}','{xd}')")
                self.database.commit()
                return True
        except Exception as e: print(e)
            
    # response = requests.get('http://25.66.109.205:8080/users/login/prueba@gmail.com/12345')
    # x = response.json()
    # print(x)
    # print(response.content)
    
    def recibir_datos(self, correo, passwd):
        try:
            response = requests.get(f'http://25.66.109.205:8080/users/login/{correo.text}/{passwd.text}')
            x = response.json()
            if x['tipo_usuario'] == 'Usuario':
                return 1
            else:
                return 0
        except Exception as e: print(e)
        
    def limpiar_datos_login(self, correo, passwd):
        correo.text = ""
        passwd.text = ""

    
    
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.manager = None
        
    def file_manager_open(self):
        if not self.manager:
            self.file_manager = MDFileManager(
                exit_manager=self.exit_manager, select_path=self.select_path)
            # self.manager.add_widget(self.file_manager)
            self.file_manager.show('/')  # output manager to the screen
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        toast(path)
        print(path)
        
        self.exit_manager()

    def exit_manager(self, *args):
        self.manager_open = False

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device..'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True  
  
  
  
  
    
    # def __init__(self, **kwargs):
    #     super().__init__(**kwargs)
    #     self.file_manager_obj = MDFileManager(
    #         select_path= self.select_path,
    #         exit_manager= self.exit_maganer(),
    #         preview= True
    #     )
    # def select_path(self, path):
    #     print(path)
    #     self.exit_manager()
        
    # def open_file_manager(self):
    #     self.file.show('/')
        
    # def exit_maganer(self):
    #     self.file.close()
    
    


LabelBase.register(name='Cambria', 
                   fn_regular='assets/font/cambria.ttc')

KivyApp().run()