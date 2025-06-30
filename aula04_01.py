# evento de teclado
import keyboard


def on_key_event(event):
    if event.event_type == keyboard.KEY_DOWN:  # verifica se a tecla foi pressionada
        print(f'Tecla pressionada: {event.name}')
        if event.name == 'a':
            print('a em especial')


# main
keyboard.on_press(on_key_event) # registra o hook para o evento de tecla pressionada

# Mantém o programa em execução para captura os eventos de tecla indefinidamente
try:
    while True:
        pass # aqui posso colocar resto do código
except keyboardInterrupt:
    print('Programa interrompido pelo usuário.')

