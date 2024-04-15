input.onLogoEvent(TouchButtonEvent.Pressed, function () {
    for (let index = 0; index < 9; index++) {
        contador += -1
        basic.showNumber(contador)
        music.play(music.tonePlayable(698, music.beat(BeatFraction.Whole)), music.PlaybackMode.UntilDone)
        basic.pause(1000)
    }
    basic.showNumber(0)
    music.play(music.builtinPlayableSoundEffect(soundExpression.soaring), music.PlaybackMode.UntilDone)
})
input.onButtonPressed(Button.A, function () {
    contador = 10
    tempo = 10
    while (contador >= 10) {
        basic.showNumber(tempo)
    }
})
input.onButtonPressed(Button.B, function () {
    contador = 10
    tempo = 10
    while (contador >= 10) {
        basic.showNumber(tempo)
    }
})
let tempo = 0
let contador = 0
contador = 10
tempo = 10
while (contador >= 10) {
    basic.showNumber(tempo)
}
