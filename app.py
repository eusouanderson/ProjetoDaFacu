from PySimpleGUI import *
import PySimpleGUI as sg

dados = []

Titulos = ['Lote', 'Produto', 'Fronecedor']

layout =[

    [sg.Text(Titulos[0]), sg.Input(size=5, key=Titulos[0])], 
    [sg.Text(Titulos[1]), sg.Input(size=20, key=Titulos[1])], 
    [sg.Text(Titulos[2]), sg.Combo(['Fornecedor 1', 'Fornecedor 2', 'Fornecedor 3'], key=Titulos[2])], 
    [sg.Button('Adicionar'), sg.Button('Editar'), sg.Button('Salvar', disabled=True), sg.Button('Excluir'), sg.Button('Sair')],
    [sg.Table(dados, Titulos, key='Tabela')]
]

window = sg.Window('Sistema de gereciamento de Suplementos', layout)
event = True
while event:

    event, values = window.read()

    if event == 'Adicionar':
        dados.append([values[Titulos[0]], values[Titulos[1]], values[Titulos[2]]])
        window['Tabela'].update(values=dados)
        for i in range(3):
            window[Titulos[i]].update(value='')

    if event == 'Editar':
        if values['Tabela'] ==[]:
            sg.popup('Nenhuma linha selecionada ')
        else:
            editarLinha=values['Tabela'][0]
            sg.popup('Editar linha selecionada')
            for i in range(3):
                window[Titulos[i]].update(value=dados[editarLinha][i])
            window['Salvar'].update(disabled=False)

    if event == 'Salvar':
        dados[editarLinha] = [values[Titulos[0]], values[Titulos[1]], values[Titulos[2]]]
        window['Tabela'].update(values=dados)
        for i in range(3):
            window[Titulos[i]].update(value='')
        window['Salvar'].update(disabled=True)

    if event == 'Sair':
        window.close()