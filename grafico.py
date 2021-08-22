import PySimpleGUI as sg
import time

imagen = ["portada4.png","salir.png","Play.png","empezar.png"]
imagen1 = ["verbos.png","Sustantivos.png","Adjetivos.png"]
imagen2 = ["verbo.png","Sustantivo.png","adjetivo.png"]
imagen3 = ["facil.png","dificil"]

reset = False
user_in = 0
acierto = 0

layout = [[sg.Button(key="-USER_IN-", image_filename= imagen[0]), 
		   sg.Button(key="-PLAY-", image_filename= imagen[2]),
		   sg.Button(key="-CLOSE-", image_filename= imagen[1])],
		   [sg.Text(key="-TEXT-", size=(5,5)), 
		    sg.Button("OK", button_color=("white","green"), size=(3,1)),
		   	sg.Input(key="-INPUT-")]]

window = sg.Window("Sopa de Letras", layout=layout)

while True:

	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break
	# window["-TEXT-"].update("El Resultado es" * values["-INPUT-"])
	if event == "-CLOSE-":
		exit()
	elif event == "-USER_IN-":
		if not reset:
			user_in = (user_in + 1) % 3
			window["-USER_IN-"].update(image_filename=imagen2[user_in])

	elif event == "-PLAY-":
		if not reset:
			if user_in == 0:
				window["-USER_IN-"].update(image_filename=imagen1[0])
				window["-PLAY-"].update(image_filename=imagen[3])
				if event == "-PLAY-":
					window
					
				 


window.close()



