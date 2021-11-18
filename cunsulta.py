import requests
import json
import PySimpleGUI as sg


class TelaPython:
    def __init__(self):

        sg.theme('dark grey 5')

        layout = [
            [sg.Text('cep'), sg.Input(size=(30, 0)),sg.Button('Sair',size=(1))],
            [sg.Button('Buscar')],
            [sg.Output(size=(40, 10))]
        ]

        self.tela = sg.Window('Busca de CEP', layout)

    def consultacep(self, cep):
        url = requests.get(f'https://viacep.com.br/ws/{cep}/json')
        if url.status_code == 200:
            print('Sucesso')
            
        elif url.status_code == 400:
            print('Erro 400')

        endereco = url.json()

        return endereco

    def start_window(self):
        while True:
            self.button, self.values = self.tela.Read()
            
            if self.button == 'Sair' or self.button == sg.WINDOW_CLOSED:
                break

            try:
                valores = self.consultacep(self.values['CEP'])
                for k, v in valores.items():
                    print(k.upper(), ':', v)
                    
            except:
                print('Name Error, funcao não definida')


jn = TelaPython()
jn.start_window()

