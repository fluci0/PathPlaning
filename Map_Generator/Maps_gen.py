# -*- coding: utf-8 -*-
"""
Created on Wed May 25 13:57:34 2024
Title: Random map generator - jpg image
"""

import numpy as np
import cv2 
import os
import pathlib
import tkinter as tk
from tkinter import *
from datetime import datetime

N = 10
win_main = tk.Tk()
opcion = IntVar()
win_main.title("Generador de mapas - FR")
win_main.config(bg = 'gray')
win_main.geometry('250x300')

def mapas():
    global Mapa
    if opcion.get() == 0:
        n = 5
    if opcion.get() == 1:
        n = 25
    if opcion.get() == 2:
        n = 100
    if opcion.get() == 3:
        n = 250
    if opcion.get() == 4:
        n = 500
    if opcion.get() == 5:
        n = 1000
    
    hoy = datetime.now()
    año = hoy.strftime("%Y")
    mes = hoy.strftime("%m")
    dia = hoy.strftime("%d")
    hora = str(hoy.hour)
    minuto = str(hoy.minute)
    carpeta = 'MAPAS' + "_" + dia + mes + año + "_" + hora + "_" + minuto + "_" + str(n) + "x" + str(n) 
    pathlib.Path(carpeta).mkdir(parents = True, exist_ok = True)
    
    for j in range(N):
        #Mapa = np.random.randint(0, 255, size = (n, n))
        Mapa = np.random.choice([0, 255], size = (n, n), p = [.8, .2])
        MapaMax = np.max(Mapa)
        Mapa = MapaMax - Mapa
        nombre_mapa = str(n) + "x" + str(n) + "_" + str(j) + ".jpg" 
        
        print('nombre_mapa:', nombre_mapa)
        print('nombre_carpeta:', carpeta)
        cv2.imwrite(os.path.join(carpeta , nombre_mapa), Mapa)
        cv2.waitKey()

def cerrar():
        win_main.destroy()

#Layout
contenedor_layout = tk.LabelFrame(win_main, text = "Generador de mapas - FR")
contenedor_layout.grid(column = 0, row = 0, padx = 10, pady = 10)

######################################################Layout botones########################################################

botones_layout = tk.LabelFrame(contenedor_layout, text = "Opciones")
botones_layout.grid(column = 0, row = 0, padx = 10, pady = 10)
tk.Label(botones_layout, text = "Seleccione dimensiones de mapas:", foreground ='black', font = ('Candara', '10')).grid(column = 0, row = 1, stick = tk.W)
tk.Radiobutton(botones_layout, text = "5x5", variable = opcion, value = 0).grid(column = 0, row = 3, stick = tk.W)
tk.Radiobutton(botones_layout, text = "25x25", variable = opcion, value = 1).grid(column = 0, row = 6, stick = tk.W)
tk.Radiobutton(botones_layout, text = "100x100", variable = opcion, value = 2).grid(column = 0, row = 9, stick = tk.W)
tk.Radiobutton(botones_layout, text = "250x250", variable = opcion, value = 3).grid(column = 0, row = 12, stick = tk.W)
tk.Radiobutton(botones_layout, text = "500x500", variable = opcion, value = 4).grid(column = 0, row = 15, stick = tk.W)
tk.Radiobutton(botones_layout, text = "1000x1000", variable = opcion, value = 5).grid(column = 0, row = 18, stick = tk.W)
tk.Button(botones_layout, text = "GENERAR", command = mapas).grid(column = 0, row = 21, stick = tk.W)

win_main.protocol("WM_DELETE_WINDOW", cerrar)

win_main.mainloop()