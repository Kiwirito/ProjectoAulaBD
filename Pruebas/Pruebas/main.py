
#xd
from asyncio.windows_events import NULL
from cProfile import label
import json
from unicodedata import numeric
from urllib import response

from kivymd.icon_definitions import md_icons
from kivymd.uix.bottomnavigation import MDBottomNavigation
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.scrollview import MDScrollView
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
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty, StringProperty
from kivymd.uix.pickers import MDDatePicker
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout

#Components Import
from components.comments import ListComments, ImagenIniciativa
from components.post_card import PostCard, Enlance
from components.stardialog import Estrellas
from components.listcoord import Item
from components.listiniciativa import ItemIniciativaWindow

#Window
import sys
from win32api import GetSystemMetrics

#Tamaño de la ventana
#Default Mac 412,892
Window.size = (412,892)
imagenP = "https://fotografias.antena3.com/clipping/cmsimages01/2021/09/30/0F7B0DA6-1E5E-4F1A-8421-86443596D1DE/98.jpg?crop=1024,576,x0,y10&width=1900&height=1069&optimize=high&format=webply"
screenx = GetSystemMetrics(0)
screeny = GetSystemMetrics(1)


#Cargar archivos kv

Builder.load_file("my.kv")
Builder.load_file('components/appbar.kv')
Builder.load_file('components/post_card.kv')
Builder.load_file('components/bottom_nav.kv')
Builder.load_file('components/stardialog.kv')
Builder.load_file('components/comments.kv')
Builder.load_file('components/options.kv')
Builder.load_file('components/listcoord.kv')
Builder.load_file('components/listiniciativa.kv')




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

class HomeLiderWindow(Screen):
    profile_picture = imagenP

    
    def on_enter(self):
        #self.remove_list()
        
        #self.set_list()
        self.list_notification()
        # self.remove()
                
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
                    posted_ago = data[username]['posted_ago']
                ))   


    

class AjustesUsuarioWindow(Screen):
    usuario = "Usuario"
    pass

class AjustesEstudiantesWindow(Screen):
    pass

class AjustesLider(Screen):
    pass

class AjustesCoordinadorWindow(Screen):
    pass
            
class CommentsWindow(Screen):
    
    # def on_enter(self):
    #     self.list_comments()


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
    
    def list_users(self):
        Mcontent = Content()

        with open('Pruebas/assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                items = Item(name=username)
                Mcontent.ids.Mcontainer.add_widget(items)

        self.userseliminar = MDDialog(
            md_bg_color= rgba("#FFFFFF"),
            type="custom", 
            content_cls=Mcontent, 
            buttons=[
                    MDFlatButton(
                        text="[size=14sp]Cancelar[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#6200EE"),
                        on_release=self.cerrar_users
                    ),
                    MDRaisedButton(
                        text="[size=14sp]Eliminar[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#FFFFFF"),
                        on_release=self.cerrar_users
                    ),
                ],
            )
        self.userseliminar.open()
        
    def cerrar_users(self, *args):
        self.userseliminar.dismiss(force = True)
        
      
    def list_usersuspend(self):
        Mcontent = Content()

        with open('Pruebas/assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                items = Item(name=username)
                Mcontent.ids.Mcontainer.add_widget(items)

        self.usersuspend = MDDialog(
            md_bg_color= rgba("#FFFFFF"),
            type="custom", 
            content_cls=Mcontent, 
            buttons=[
                    MDFlatButton(
                        text="[size=14sp]Cancelar[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#6200EE"),
                        on_release=self.cerrar_usersuspend
                    ),
                    MDRaisedButton(
                        text="[size=14sp]Suspender[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#FFFFFF"),
                        on_release=self.cerrar_usersuspend
                    ),
                ],
            )
        self.usersuspend.open()
        
    def cerrar_usersuspend(self, *args):
        self.usersuspend.dismiss(force = True)
        


# class IniciativasList(Screen):
    
#     def on_enter(self):
#         Mcontent = Content()

#         with open('Pruebas/assets/data/posts.json') as f_obj:
#             data = json.load(f_obj)
#             for username in data:
#                 items = ItemIniciativa(name=username)
#                 Mcontent.ids.Mcontainer.add_widget(items)

#         self.listiniciative = MDDialog(
#             md_bg_color= rgba("#FFFFFF"),
#             title= "[color=6200EE]Solicitudes recientes:[/color]",
#             auto_dismiss= False,
#             type="custom", 
#             content_cls=Mcontent,
#             buttons=[
#                     MDRaisedButton(
#                         text="[size=14sp]Salir[/size]",
#                         size_hint=(3,1),
#                         theme_text_color="Custom",
#                         text_color=rgba("#FFFFFF"),
#                         on_release= self.salir
#                     ),
#                 ],
#             )
#         self.listiniciative.open()
        
#     def salir(self, *args):
#         self.listiniciative.dismiss(force = True)
#         self.manager.transition.direction = "right"
#         self.manager.current = "ajustes_coordinador"

class Content(BoxLayout):
    pass

class AdministradorWindow(Screen):
    
            
    def list_coord(self):
        Mcontent = Content()

        with open('Pruebas/assets/data/stories.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                items = Item(name=username)
                Mcontent.ids.Mcontainer.add_widget(items)

        self.MSetFileOptionsdialog = MDDialog(
            md_bg_color= rgba("#FFFFFF"),
            type="custom", 
            content_cls=Mcontent, 
            buttons=[
                    MDFlatButton(
                        text="[size=14sp]Cancelar[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#6200EE"),
                        on_release=self.cerrar_list
                    ),
                    MDRaisedButton(
                        text="[size=14sp]Guardar[/size]",
                        size_hint=(3,1),
                        theme_text_color="Custom",
                        text_color=rgba("#FFFFFF"),
                        on_release=self.cerrar_list
                    ),
                ],
            )
        self.MSetFileOptionsdialog.open()
        
    def cerrar_list(self, *args):
        self.MSetFileOptionsdialog.dismiss(force = True)
    
    # def list_coords(self):
    #     icons = list(md_icons.keys())
    #     for i in range(30):
    #         self.ids.scroll.add_widget(ItemCheckbox(
    #             text=f"Item {i}", 
    #             icon=icons[i]
    #             )
    #         )        

class FormularioWindow(Screen):
    pass

class AprobarIniciativa(Screen):
    pass

class WindowManager(ScreenManager):
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

    def on_start(self):
        self.set_list()


    def build(self):
        center_window(412,892)
        #Tema del App
        self.theme_cls.primary_palette = "DeepPurple"
        self.theme_cls.primary_hue = "600"
        self.theme_cls.theme_style = "Dark" 
        
        
        
        #Load
        self.sm = WindowManager()
        screens = [
            LoginWindow(name='login'),
            RegisterWindow(name='register'),
            StudentWindow(name='student'),
            RegisterStudentWindow(name='registerstudent'),
            HomeLiderWindow(name='home'),
            AjustesUsuarioWindow(name='ajustes_usuario'),
            AjustesEstudiantesWindow(name='ajustes_estudiantes'),
            AjustesLider(name='ajustes_lider'),
            AjustesCoordinadorWindow(name='ajustes_coordinador'),
            CommentsWindow(name='comments'),
            LiderWindow(name='lider'),
            NotificacionesWindow(name='notifications'),
            CoordinadorWindow(name='coordinador'),
            AdministradorWindow(name='administrador'),
            IniciativaWindow(name='iniciativa'),
            FormularioWindow(name='formulario'),
            ItemIniciativaWindow(name='lista_iniciativa'),
            AprobarIniciativa(name='aprobar_iniciativa')
            
        ]

        for screen in screens:
            self.sm.add_widget(screen)
        
        self.sm.current = "home"
    
        return self.sm
    
    def change_screen(self, screen):
        self.sm.current = screen
                
    def registar_datos(self, nombre,apellido,fecha,correo, passwd):

        idcombi = nombre.text + apellido.text + fecha.text
        try:
            if re.fullmatch(self.regex, correo.text):
                response = requests.post("http://25.66.109.205:8080/users/register", 
                json={"id_persona":f"{idcombi}", 
                      "nombre":f"{nombre.text}", 
                      "apellido":f"{apellido.text}", 
                      "correo":f"{correo.text}", 
                      "fecha_nacimiento":f"{fecha.text}", 
                      "contrasena":f"{passwd.text}"})
                json_response = response.json()
                
                #Clear
                nombre.text = ""
                apellido.text = ""
                fecha.text = ""
                correo.text = ""
                passwd.text = ""
                
                print(json_response["data"])
                
        except Exception as e: print(e)
            
    # response = requests.get('http://25.66.109.205:8080/users/login/prueba@gmail.com/12345')
    # x = response.json()
    # print(x)
    # print(response.content)
    
    def recibir_datos(self, correo, passwd):
        try:
            response = requests.get(f'http://25.66.109.205:8080/users/login/{correo.text}/{passwd.text}')
            x = response.json()
            if x['tipo_usuario'] == 'USUARIO':
                return 1
            elif x['tipo_usuario'] == 'ESTUDIANTE':
                return 2
            elif x['tipo_usuario'] == 'LIDER':
                return 3
            elif x['tipo_usuario'] == 'COORDINADOR':
                return 4
            elif x['tipo_usuario'] == 'ADMINISTRADOR':
                return 5
            else:
                return 0
        except Exception as e: print(e)
        
    def limpiar_datos_login(self, correo, passwd):
        correo.text = ""
        passwd.text = ""

    
    def set_list(self):
        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                self.sm.screens[4].ids['timeline'].add_widget(PostCard(
                    username = username,
                    avatar = data[username]['avatar'],
                    profile_pic = self.profile_picture,
                    post = data[username]['post'],
                    caption = data[username]['caption'],
                    likes = data[username]['likes'],
                    posted_ago = data[username]['posted_ago'],
                    link = data[username]['link'],
                    reaccion = 1,
                    sizecard = "420dp",
                ))
                # self.sm.screens[4].ids['timeline'].add_widget(Enlance(
                #     linker = data[username]['link']
                # ))


    def refresh_callback(self, *args):
        '''A method that updates the state of your application
        while the spinner remains on the screen.'''

        def refresh_callback(interval):
            self.sm.screens[4].ids['timeline'].clear_widgets()
            # if self.x == 0:
            #     self.x, self.y = 15, 30
            # else:
            #     self.x, self.y = 0, 15
            self.set_list()
            self.sm.screens[4].ids['refresh_layout'].refresh_done()
            self.tick = 0

        Clock.schedule_once(refresh_callback, 1)        
    
    
    def datos_solicitud(self, usuario):
        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                if usuario == username:
                    self.sm.screens[17].ids['solinicia'].add_widget(PostCard(
                        username = username,
                        avatar = data[username]['avatar'],
                        profile_pic = self.profile_picture,
                        post = data[username]['post'],
                        reaccion = 0,
                        sizecard = "350dp"
                    ))
                    
    def comentarios_datos(self, titulo):
        with open('Pruebas/assets/data/posts.json') as f_obj:
            data = json.load(f_obj)
            for username in data:
                if titulo == username:
                    self.sm.screens[9].ids['imagenComments'].add_widget(ImagenIniciativa(
                        posteo = data[username]['post']
                    ))
                    for comment in data[username]['comments']:
                        self.sm.screens[9].ids['listcomment'].add_widget(ListComments(
                            username = comment,
                            avatar = data[username]['comments'][comment]['imagen'],
                            comment = data[username]['comments'][comment]['comentario']
                        ))
        
    #  def list_comments(self):
    #     with open('Pruebas/assets/data/posts.json') as f_obj:
    #         data = json.load(f_obj)
    #         for username in data:
    #             self.ids.listcomment.add_widget(ListComments(
    #                 username = username,
    #                 avatar = data[username]['avatar'],
    #                 post = data[username]['post'],
    #                 caption = data[username]['caption'],
    #                 likes = data[username]['likes'],
    #                 comments = data[username]['comments'],
    #                 posted_ago = data[username]['posted_ago'],
                    
    #             ))                
                 
                    
    def limpiar_fotocomentario(self):
        self.sm.screens[9].ids['imagenComments'].clear_widgets()
        self.sm.screens[9].ids['listcomment'].clear_widgets()
        
    def limpiar_solicitud(self):
        self.sm.screens[17].ids['solinicia'].clear_widgets()
    
    
    
 
  
  
  
  
    
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