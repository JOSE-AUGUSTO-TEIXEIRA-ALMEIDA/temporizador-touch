def on_logo_pressed():
    global contador
    for index in range(9):
        contador += -1
        basic.show_number(contador)
        music.play(music.tone_playable(698, music.beat(BeatFraction.WHOLE)),
            music.PlaybackMode.UNTIL_DONE)
        basic.pause(1000)
    basic.show_number(0)
    music.play(music.builtin_playable_sound_effect(soundExpression.soaring),
        music.PlaybackMode.UNTIL_DONE)
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

def on_button_pressed_a():
    global contador, tempo
    contador = 10
    tempo = 10
    while contador >= 10:
        basic.show_number(tempo)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    global contador, tempo
    contador = 10
    tempo = 10
    while contador >= 10:
        basic.show_number(tempo)
input.on_button_pressed(Button.B, on_button_pressed_b)

tempo = 0
contador = 0
contador = 10
tempo = 10
while contador >= 10:
    basic.show_number(tempo)