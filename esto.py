# -*- coding: utf-8 -*-
"""
Creado el Mié Mar 12 2025  19:57:06

Código en español para importar el módulo "this".

import this --> Muestra en inglés el "Zen de Python", creado por Tim Peters.

import esto --> Muestra en español el "Zen de Python", creado por Tim Peters.

Autor: @alpfa
"""

# esto.py

# Texto cifrado en ROT13
TEXTO_CIFRADO = """\nRy Mra qr Clguba, cbe Gvz Crgref

Oryyb rf zrwbe dhr srb.
Rkcyípvgb rf zrwbe dhr vzcyípvgb.
Fvzcyr rf zrwbe dhr pbzcyrwb.
Pbzcyrwb rf zrwbe dhr pbzcyvpnqb.
Cynab rf zrwbe dhr navqnqb.
Qvfcrefb rf zrwbe dhr qrafb.
Yn yrtvovyvqnq phragn.
Ybf pnfbf rfcrpvnyrf ab fba gna rfcrpvnyrf pbzb cnen ebzcre ynf ertynf.
Nhadhr yn cenpgvpvqnq yr tnan n yn chermn.
Ybf reeberf ahapn qroreína cnfne fvyrapvbfnzragr.
N zrabf dhr fr fvyrapvra rkcyípvgnzragr.
Seragr n yn nzovtürqnq, erpunmn yn gragnpvóa qr nqvivane.
Qroreín unore han, l cersrevoyrzragr fbyb han, znaren boivn qr unpreyb.
Nhadhr rfn znaren chrqr ab fre boivn ny cevapvcvb n zrabf dhr frnf ubynaqéf.
Nuben rf zrwbe dhr ahapn.
Nhadhr ahapn rf n zrahqb zrwbe dhr *nuben* zvfzb.
Fv yn vzcyrzragnpvóa rf qvsípvy qr rkcyvpne, rf han znyn vqrn.
Fv yn vzcyrzragnpvóa rf sápvy qr rkcyvpne, chrqr fre han ohran vqrn.
Ybf rfcnpvbf qr abzoerf fba han tena vqrn, ¡untnzbf záf qr rfbf!"""


# Crear el diccionario ROT13
def crear_diccionario_rot13():
    """
    Crea un diccionario para el cifrado ROT13.

    Returns:
        dict: Diccionario con las equivalencias de caracteres en ROT13.
    """
    diccionario = {}
    for codigo in (65, 97):  # 65 es 'A', 97 es 'a' en ASCII
        for i in range(26):
            diccionario[chr(i + codigo)] = chr((i + 13) % 26 + codigo)
    return diccionario


# Decodificar el texto
def decodificar_rot13(texto_cifrado, diccionario):
    """
    Decodifica un texto en español cifrado con ROT13.

    Args:
        texto_cifrado (str): Texto cifrado en ROT13.
        diccionario (dict): Diccionario con las equivalencias de caracteres.

    Returns:
        str: Texto decodificado.
    """
    return "".join([diccionario.get(c, c) for c in texto_cifrado])


# Mostrar el Zen de Python en español
def mostrar_zen():
    """
    Muestra el Zen de Python en español al importar este módulo.
    """
    diccionario = crear_diccionario_rot13()
    texto_decodificado = decodificar_rot13(TEXTO_CIFRADO, diccionario)
    print(texto_decodificado)


# Mostrar el Zen al importar el módulo
mostrar_zen()
