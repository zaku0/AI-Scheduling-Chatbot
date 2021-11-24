from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen,ScreenManager
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.graphics.texture import Texture
from kivy.animation import Animation
from NEA.Database.AppDatabase import db

Window.size = [400,650]

class BackgroundLayer(Widget):
    def __init__(self, **args):
        super(BackgroundLayer, self).__init__(**args)
        self.texture = Texture.create(size=(2, 2), colorfmt='rgba')
        p1_color = [250, 255, 209,255]
        p2_color = [250, 255, 209,255]
        p3_color = [161, 255, 206, 255]
        p4_color = [161, 255, 206, 255]
        p = p1_color + p2_color + p3_color + p4_color
        buf = bytes(p)
        self.texture.blit_buffer(buf, colorfmt='rgba', bufferfmt='ubyte')
        with self.canvas:
            self.rect = Rectangle(pos=self.pos, size=self.size, texture=self.texture)

        self.bind(size=self.update_rect)
        self.bind(pos=self.update_rect)

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

from kivy.graphics import Color

class BackgroundYellow(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        print('Window.size: %s' % str(Window.size))
        with self.canvas.before:
            Color(50/51,1,209/255,1)
            self.rect = Rectangle(size=Window.size,
                                  pos=self.pos)

class BackgroundGreen(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'horizontal'
        print('Window.size: %s' % str(Window.size))
        with self.canvas.before:
            Color(220/255, 1, 206/255, 0.7)
            self.rect = Rectangle(size=Window.size,
                                  pos=self.pos)

class LoginScreen(Screen):
    def __init__(self,**kwargs):
        super(LoginScreen, self).__init__(**kwargs)

    def animate_card(self,widget):
        anim = Animation(pos_hint={'center_y':0.6})
        anim.start(widget)

    def sign_in(self,username,password):
        db.execute("SELECT Password FROM UserAccount WHERE Username='%s'"%username)
        database_password = db.fetchone()[0]
        if database_password == password:
            self.parent.current = "home"
        else:
            errormessage = MDLabel(text='[color=F27059]Login failed please try again[/color]',font_size=14,font_name='md/fonts/Roboto-Light.ttf',markup=True,pos_hint={'center_x':0.34,'center_y':0.5},size_hint=(0.5,0.6))
            self.add_widget(errormessage)
        #add hashing and linked list

class CreateUserScreen(Screen):
    def __init__(self,**kwargs):
        super(CreateUserScreen, self).__init__(**kwargs)
    def validate(self, TCsValue, username, password, securityquestion, securityanswer, firstname, age, commutepath):
        if TCsValue and username != '' and password != '' and securityquestion != '' and securityanswer != '' and firstname != '' and age != '' and commutepath != '':
            db.execute("SELECT Username FROM UserAccount WHERE Username='%s'"%username)
            account = db.fetchall()
            if not account:
                db.create_user((username,password,securityquestion,securityanswer,firstname,int(age),commutepath))
                db.commit()
                self.parent.current = "login"
                self.manager.transition.direction = "left"
            else:
                errormessageUsername = MDLabel(text='[color=F27059]This username is unavailable[/color]',font_size=9,font_name='md/fonts/Roboto-Light.ttf',markup=True,pos_hint={'center_x':0.51,'center_y':0.8},size_hint=(0.9,0.6))
                self.add_widget(errormessageUsername)
        else:
            errormessage = MDLabel(text='[color=F27059]Please make sure that no text fields are blank and T&Cs check box is ticked[/color]',font_size=12,font_name='md/fonts/Roboto-Light.ttf',markup=True,pos_hint={'center_x':0.51,'center_y':0.14},size_hint=(0.9,0.6))
            self.add_widget(errormessage)

class HomeScreen(Screen):
    def __init__(self,**kwargs):
        super(HomeScreen, self).__init__(**kwargs)

class WindowManager(ScreenManager):
    pass

class Chatbot(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Teal'
        kv = Builder.load_file("my.kv")
        return kv

if __name__ == "__main__":
    Chatbot().run()
