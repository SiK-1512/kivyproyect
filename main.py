from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.toast import toast
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton


def mostrar_info(imc, edad, altura, peso, estado):
    dialog = MDDialog(title="Tus resultados!",
                      text=f"La informacion que colocaste es:\n\nAltura: {altura}\n\nEdad: {edad}\n\nPeso: {peso}\n\nTu IMC es: {imc}\n\nPor lo que tienes {estado}",
                      buttons=[
                          MDRaisedButton(text="Aceptar",
                                         on_press=lambda *args: dialog.dismiss())
                      ])
    dialog.open()

class Calculadora(MDScreen):

    data_female = {
        '5': {
            'desnutricion severa': (0, 11.8),
            'desnutricion moderada': (11.8, 12.6),
            'peso normal': (12.7, 16.9),
            'sobrepeso': (17.0, 18.9),
            'obesidad': (19.0, 1000)
        },
        '6': {
            'desnutricion severa': (0, 11.7),
            'desnutricion moderada': (11.7, 12.6),
            'peso normal': (12.7, 17.0),
            'sobrepeso': (17.1, 19.2),
            'obesidad': (19.3, 1000)
        },
        '7': {
            'desnutricion severa': (0, 11.8),
            'desnutricion moderada': (11.8, 12.6),
            'peso normal': (12.7, 17.3),
            'sobrepeso': (17.4, 19.8),
            'obesidad': (19.9, 1000)
        },
        '8': {
            'desnutricion severa': (0, 11.9),
            'desnutricion moderada': (11.9, 12.8),
            'peso normal': (12.9, 17.7),
            'sobrepeso': (17.8, 20.6),
            'obesidad': (20.7, 1000)
        },
        '9': {
            'desnutricion severa': (0, 12.1),
            'desnutricion moderada': (12.1, 13.0),
            'peso normal': (13.1, 18.3),
            'sobrepeso': (18.4, 21.5),
            'obesidad': (21.6, 1000)
        },
        '10': {
            'desnutricion severa': (0, 12.4),
            'desnutricion moderada': (12.4, 13.4),
            'peso normal': (13.5, 19.0),
            'sobrepeso': (19.1, 22.6),
            'obesidad': (22.7, 1000)
        },
        '11': {
            'desnutricion severa': (0, 12.7),
            'desnutricion moderada': (12.7, 13.8),
            'peso normal': (13.9, 19.9),
            'sobrepeso': (20.0, 23.7),
            'obesidad': (23.8, 1000)
        },
        '12': {
            'desnutricion severa': (0, 13.2),
            'desnutricion moderada': (13.2, 14.3),
            'peso normal': (14.4, 20.8),
            'sobrepeso': (20.9, 25.0),
            'obesidad': (25.1, 1000)
        },
        '13': {
            'desnutricion severa': (0, 13.6),
            'desnutricion moderada': (13.6, 14.8),
            'peso normal': (14.9, 21.8),
            'sobrepeso': (21.9, 26.2),
            'obesidad': (26.3, 1000)
        },
        '14': {
            'desnutricion severa': (0, 14.0),
            'desnutricion moderada': (14.0, 15.3),
            'peso normal': (15.4, 22.7),
            'sobrepeso': (22.8, 27.3),
            'obesidad': (27.4, 1000)
        },
        '15': {
            'desnutricion severa': (0, 14.4),
            'desnutricion moderada': (14.4, 15.8),
            'peso normal': (15.9, 23.5),
            'sobrepeso': (23.6, 28.2),
            'obesidad': (28.3, 1000)
        },
        '16': {
            'desnutricion severa': (0, 14.6),
            'desnutricion moderada': (14.6, 16.1),
            'peso normal': (16.2, 24.1),
            'sobrepeso': (24.2, 28.9),
            'obesidad': (29.0, 1000)
        },
        '17': {
            'desnutricion severa': (0, 14.7),
            'desnutricion moderada': (14.7, 16.3),
            'peso normal': (16.4, 24.5),
            'sobrepeso': (24.6, 29.3),
            'obesidad': (29.4, 1000)
        },
        '18': {
            'desnutricion severa': (0, 14.7),
            'desnutricion moderada': (14.7, 16.3),
            'peso normal': (16.4, 24.8),
            'sobrepeso': (24.9, 29.5),
            'obesidad': (29.6, 1000)
        }
    }

    data_male = {
        '5': {
            'desnutricion severa': (0, 12.1),
            'desnutricion moderada': (12.1, 12.9),
            'peso normal': (13.0, 16.6),
            'sobrepeso': (16.7, 18.3),
            'obesidad': (18.4, 1000)
        },
        '6': {
            'desnutricion severa': (0, 12.1),
            'desnutricion moderada': (12.1, 12.9),
            'peso normal': (13.0, 16.8),
            'sobrepeso': (16.9, 18.5),
            'obesidad': (18.6, 1000)
        },
        '7': {
            'desnutricion severa': (0, 12.3),
            'desnutricion moderada': (12.3, 13.0),
            'peso normal': (13.1, 17.0),
            'sobrepeso': (17.1, 19.0),
            'obesidad': (19.1, 1000)
        },
        '8': {
            'desnutricion severa': (0, 12.4),
            'desnutricion moderada': (12.4, 13.2),
            'peso normal': (13.3, 17.4),
            'sobrepeso': (17.5, 19.7),
            'obesidad': (19.8, 1000)
        },
        '9': {
            'desnutricion severa': (0, 12.6),
            'desnutricion moderada': (12.6, 13.4),
            'peso normal': (13.5, 17.9),
            'sobrepeso': (18.0, 20.5),
            'obesidad': (20.6, 1000)
        },
        '10': {
            'desnutricion severa': (0, 12.8),
            'desnutricion moderada': (12.8, 13.6),
            'peso normal': (13.7, 18.5),
            'sobrepeso': (18.6, 21.4),
            'obesidad': (21.5, 1000)
        },
        '11': {
            'desnutricion severa': (0, 13.1),
            'desnutricion moderada': (13.1, 14.0),
            'normal': (14.1, 19.2),
            'sobrepeso': (19.3, 22.5),
            'obesidad': (22.6, 1000)
        },
        '12': {
            'desnutricion severa': (0, 13.4),
            'desnutricion moderada': (13.4, 14.4),
            'peso normal': (14.5, 19.9),
            'sobrepeso': (20.0, 23.6),
            'obesidad': (23.7, 1000)
        },
        '13': {
            'desnutricion severa': (0, 13.8),
            'desnutricion moderada': (13.8, 14.8),
            'peso normal': (14.9, 20.8),
            'sobrepeso': (20.9, 24.8),
            'obesidad': (24.8, 1000)
        },
        '14': {
            'desnutricion severa': (0, 14.3),
            'desnutricion moderada': (14.3, 15.4),
            'peso normal': (15.5, 21.8),
            'sobrepeso': (21.9, 25.9),
            'obesidad': (26.0, 1000)
        },
        '15': {
            'desnutricion severa': (0, 14.7),
            'desnutricion moderada': (14.7, 15.9),
            'peso normal': (16.0, 22.7),
            'sobrepeso': (22.8, 27.0),
            'obesidad': (27.1, 1000)
        },
        '16': {
            'desnutricion severa': (0, 15.1),
            'desnutricion moderada': (15.1, 16.4),
            'peso normal': (16.5, 23.5),
            'sobrepeso': (23.6, 27.9),
            'obesidad': (28.0, 1000)
        },
        '17': {
            'desnutricion severa': (0, 15.4),
            'desnutricion moderada': (15.4, 16.8),
            'peso normal': (16.9, 24.3),
            'sobrepeso': (24.4, 28.6),
            'obesidad': (28.7, 1000)
        },
        '18': {
            'desnutricion severa': (0, 15.7),
            'desnutricion moderada': (15.7, 17.2),
            'peso normal': (17.3, 24.9),
            'sobrepeso': (25.0, 29.2),
            'obesidad': (29.3, 1000)
        }
    }

    def bajar_altura(self):
        altura = self.ids.altura.text
        if int(altura) <= 0:
            r = 0
        else:
            r = int(altura) - 1
        self.ids.altura.text = str(r)

    def subir_altura(self):
        altura = self.ids.altura.text
        if 0 > int(altura) > 200:
            r = 0
        else:
            r = int(altura) + 1
        self.ids.altura.text = str(r)

    def bajar_peso(self):
        peso = self.ids.peso.text
        if int(peso) <= 0:
            r = 0
        else:
            r = int(peso) - 1
        self.ids.peso.text = str(r)

    def subir_peso(self):
        peso = self.ids.peso.text
        if 0 > int(peso) > 200:
            r = 0
        else:
            r = int(peso) + 1
        self.ids.peso.text = str(r)

    def calcular_imc(self):
        edad = self.ids.edad.value
        altura = self.ids.altura.text
        peso = self.ids.peso.text
        male = self.ids.male
        female = self.ids.female

        altura_m = int(altura) / 100
        # formula para imc
        imc = round(int(peso) / pow(altura_m, 2), 1)

        if male.active or female.active:
            if edad >= 19:
                if imc < 18.15:
                    estado = "bajo peso"
                elif 24.9 > imc > 18.5:
                    estado = "peso normal"
                elif 29.0 > imc > 25.0:
                    estado = "sobrepeso"
                elif imc > 30.0:
                    estado = "obesidad"
            else:
                if male.active:
                    sety = self.data_male.get(str(edad))
                elif female.active:
                    sety = self.data_female.get(str(edad))
                else:
                    estado = "ERROR"
                if sety:
                    for k, v in sety.items():
                        if v[1] > imc > v[0]:
                            estado = k

            mostrar_info(imc, edad, altura, peso, estado)
        else:
            toast("Seleccione un sexo")


class MainApp(MDApp):
    def build(self):
        
        """
        'Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan',
        'Teal', 'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange',
        'Brown', 'Gray', 'BlueGray'
        """

        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.material_style = "M3"
        self.theme_cls.primary_palette = "Cyan"
        return Calculadora()


if "__main__" == __name__:
    MainApp().run()
