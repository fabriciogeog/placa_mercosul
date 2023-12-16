"""Aplicação para ajustar modelo placas veiculares."""

import re
import pandas as pd


def confere_placa(placa_antiga):
    padrao = r'^[a-zA-Z]{3}[0-9]{4}$'
    if re.fullmatch(padrao, placa_antiga) is None:
        print('Formato da placa inválido!')

    else:
        print('Formato válido')
        print('Placa antiga:', placa_antiga.upper())
        lista = list(placa_antiga)
        print('Dígito que será substituído: ', lista[4])
        tabela = pd.read_csv('equivalencia_placa_mercosul.csv', delimiter=';')
        serie = pd.Series(tabela['ALG_NOVO'])
        equivalente = serie[int(lista[4])]
        lista[4] = equivalente
        placa_antiga = ''.join(lista)
        print('Placa atualizada: ', placa_antiga.upper())


if __name__ == '__main__':
    while True:
        placa_informada = input(str('Informe a placa (NÃO USAR TRAÇO): '))
        confere_placa(placa_informada)
        resposta = str.upper(input('Deseja ajustar outra placa (S/N): '))
        if resposta == 'S':
            continue
        elif resposta == 'N':
            break
        else:
            print('Opção inválida!')
            break