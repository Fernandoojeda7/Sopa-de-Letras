import PySimpleGUI as sg



portada= "portada.png"
salir= "salir.png"
imagen2 = ["verbos.png","sustantivos.png","adjetivos.png"]



reset = False
user_in = 0




layout = [[sg.Text("LAS PALABRAS QUE TENES QUE BUSCAR SON *12*")],
		   [sg.Button(key="-USER_IN-", image_filename= portada), 
		   sg.Button("JUGAR", size=(35, 10), key="-PLAY-"),
		   sg.Button(key="-CLOSE-", image_filename= salir)],
		   [sg.InputText(key="-TEXT-", size=(30, 10)), 
		   ]]

window = sg.Window("Sopa de Letras", layout=layout)

while True:

	event, values = window.read()

	if event == sg.WIN_CLOSED:
		break
		
	if event == "-CLOSE-":
			exit()
	elif event == "-USER_IN-":
		if not reset:
			user_in = (user_in + 1) % 3
			window["-USER_IN-"].update(image_filename=imagen2[user_in])
			window["-PLAY-"].update("ESCRIBE TU PALABRA Y DALE COMENZAR", button_color=("black", "yellow"))

	elif event == "-PLAY-":
		if user_in == 0 or user_in == 1 or user_in == 2:
			
			if event == "-PLAY-" and values["-TEXT-"] == "comer":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "bailar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "cantar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "saltar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "correr":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "buscar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "nadar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "tocar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "volar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "romper":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "subir":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "bajar":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "casa":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "arbol":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "pelota":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "muñeca":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "remera":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "plato":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "piso":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "carpeta":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "mesa":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "silla":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "campo":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "banco":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "grande":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "pequeña":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "ancho":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "peludo":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "pelado":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "flaco":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "fino":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "colorado":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "amable":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "alto":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "valiente":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			elif event == "-PLAY-" and values["-TEXT-"] == "brillante":
				window["-PLAY-"].update("CORRECTO", button_color=("black", "green"))
			else:
				window["-PLAY-"].update("INCORRECTO", button_color=("black", "red"))	


window.close()

		



