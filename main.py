from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.metrics import dp  # Importe dp para dimensionamento responsivo
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivy.uix.popup import Popup
import datetime
from kivymd.uix.pickers import MDDatePicker

# Carregue o arquivo KV que define a estrutura da interface do usuário
KV = "myapp.kv"

class MyApp(MDApp):
    def build(self):
        return Builder.load_file(KV)
    
    def login(self, username, password):
        # Coloque aqui a lógica de autenticação, por exemplo, verificar se o login é válido.
        # Se o login for bem-sucedido, mude para a tela de boas-vindas.
        if username == 'user' and password == 'pass':
            self.root.ids.screen_manager.current = 'menu'

    def menu(self):
        self.root.ids.screen_manager.current = 'menu'

    def logout(self):
        # Retorne à tela de login ao fazer logout
        self.root.ids.screen_manager.current = 'login'

    def entradas_barcos(self):
        self.root.ids.screen_manager.current = 'dados_entradas_barcos'

if __name__ == '__main__':
    MyApp().run()
