import PySimpleGUI as sg
import math

def calcular_velocidade(altura):
    g = 10  # Aceleração da gravidade em m/s^2
    velocidade = math.sqrt(2 * g * altura)
    return velocidade

def mps_to_kmph(velocidade_mps):
    return velocidade_mps * 3.6  # Conversão de m/s para km/h

def calcular_altura(velocidade):
    g = 10  # Aceleração da gravidade em m/s^2
    altura = (velocidade ** 2) / (2 * g)
    return altura

def calcular_tempo(altura):
    g = 10  # Aceleração da gravidade em m/s^2
    tempo = math.sqrt((2 * altura) / g)
    return tempo

layout = [
    [sg.Text('')],
    [sg.Text('Preencha os campos abaixo de acordo com numeros,\n de acordo com a necessidade do seu problema:',)], #\n quebra de linha
    [sg.Text('')],
    [sg.Text('Altura na queda ( em metros):'), sg.InputText(key='altura', size=(15))],
    [sg.Text('')],
    [sg.Text('Velocidade  da queda (km/h):'), sg.InputText(key='velocidade', size=(15))],
    [sg.Text('')],
    [sg.Text('Tempo da queda (segundos):'), sg.InputText(key='tempo', size=(15))],
    [sg.Text('')],
    [sg.Button('Calcular Velocidade', font=('monospace', 10)),
     sg.Button('Calcular Altura', font=('monospace', 10)),
     sg.Button('Calcular Tempo', font=('monospace', 10))],
    [sg.Text('', size=(30, 1), key='resultado')]
]

window = sg.Window('Calculadora de Queda Livre', layout, font=('monospace', 12))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Calcular Velocidade':
        try:
            altura = float(values['altura'])
            velocidade = calcular_velocidade(altura)
            velocidade_kmph = mps_to_kmph(velocidade)
            window['resultado'].update(f'Velocidade: {velocidade_kmph:.2f} km/h')
        except ValueError:
            window['resultado'].update('Altura inválida!')
    elif event == 'Calcular Altura':
        try:
            velocidade = float(values['velocidade'])
            altura = calcular_altura(velocidade)
            window['resultado'].update(f'Altura: {altura:.2f} metros')
        except ValueError:
            window['resultado'].update('Velocidade inválida!')
    elif event == 'Calcular Tempo':
        try:
            altura = float(values['altura'])
            tempo = calcular_tempo(altura)
            window['resultado'].update(f'Tempo: {tempo:.2f} segundos')
        except ValueError:
            window['resultado'].update('Altura inválida!')

window.close()
