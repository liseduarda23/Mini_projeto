import PySimpleGUI as sg
import math

sg.theme('Black')

def calcular_velocidade(altura, aceleracao_gravidade):
    velocidade = math.sqrt(2 * aceleracao_gravidade * altura)
    return velocidade

def calcular_altura(velocidade, aceleracao_gravidade):
    altura = (velocidade ** 2) / (2 * aceleracao_gravidade)
    return altura

layout = [
    [sg.Text('Utilize para Aceleração da gravidade: 9.81')],
    [sg.Text('Altura da queda (metros):'), sg.InputText(key='altura')],
    [sg.Text('Velocidade da queda (m/s):'), sg.InputText(key='velocidade')],
    [sg.Text('Aceleração da gravidade (m/s²):'), sg.InputText(key='aceleracao_gravidade')],
    [sg.Button('Calcular Velocidade'), sg.Button('Calcular Altura')],
    [sg.Text('', size=(30, 1), key='resultado')]
]

window = sg.Window('Calculadora de Queda Livre', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Sair':
        break
    elif event == 'Calcular Velocidade':
        try:
            altura = float(values['altura'])
            aceleracao_gravidade = float(values['aceleracao_gravidade'])
            velocidade = calcular_velocidade(altura, aceleracao_gravidade)
            window['resultado'].update(f'Velocidade: {velocidade:.2f} m/s')
        except ValueError:
            window['resultado'].update('Valores inválidos!')
    elif event == 'Calcular Altura':
        try:
            velocidade = float(values['velocidade'])
            aceleracao_gravidade = float(values['aceleracao_gravidade'])
            altura = calcular_altura(velocidade, aceleracao_gravidade)
            window['resultado'].update(f'Altura: {altura:.2f} metros')
        except ValueError:
            window['resultado'].update('Valores inválidos!')

window.close()
