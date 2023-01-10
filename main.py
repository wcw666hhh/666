currfreq = 0
lastfreq = 0

def on_forever():
    global currfreq, lastfreq
    currfreq = 0
    lastfreq = currfreq
basic.forever(on_forever)def on_forever():
    pass
basic.forever(on_forever)
currfreq = 0
lastfreq = 0

def on_forever():
    global currfreq, lastfreq
    currfreq = Math.map(input.acceleration(Dimension.X), -1024, 1023, 1, 5000)
    lastfreq = currfreq
basic.forever(on_forever)
currFreq = 0
lastFreq = 0

def on_forever():
    global currFreq, lastFreq
    currFreq = Math.map(input.acceleration(Dimension.X), -1024, 1023, 0, 5000)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            5000,
            0,
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    lastFreq = currFreq
basic.forever(on_forever)
currFreq = 0
lastFreq = 0

def on_forever():
    global currFreq, lastFreq
    currFreq = Math.map(input.acceleration(Dimension.X), -1024, 1023, 0, 5000)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            Math.map(input.acceleration(Dimension.X), -1024, 1023, 0, 5000),
            Math.map(input.acceleration(Dimension.Y), -1024, 1023, 0, 5000),
            255,
            0,
            500,
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    lastFreq = currFreq
basic.forever(on_forever)
currFreq = 0
lastFreq = 0

def on_forever():
    global currFreq, lastFreq
    currFreq = Math.map(input.acceleration(Dimension.X), -1024, 1023, 0, 5000)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            Math.map(input.acceleration(Dimension.X), -1024, 1023, 0, 5000),
            Math.map(input.acceleration(Dimension.Y), -1024, 1023, 0, 5000),
            randint(0, 1024),
            randint(0, 1024),
            randint(40, 100),
            SoundExpressionEffect.NONE,
            InterpolationCurve.LINEAR),
        SoundExpressionPlayMode.UNTIL_DONE)
    lastFreq = currFreq
basic.forever(on_forever)
currfreq = 0
lastfreq = 0

def on_forever():
    global currfreq, lastfreq
    currfreq = Math.map(input.acceleration(Dimension.X), -1024, 1023, 1, 5000)
    music.play_sound_effect(music.create_sound_effect(WaveShape.SINE,
            Math.map(input.acceleration(Dimension.X), -1024, 1023, 1, 5000),
            Math.map(input.acceleration(Dimension.Y), -1024, 1023, 1, 5000),
            randint(0, 1024),
            randint(0, 1024),
            randint(40, 100),
            SoundExpressionEffect.VIBRATO,
            InterpolationCurve.CURVE),
        SoundExpressionPlayMode.UNTIL_DONE)
    lastfreq = currfreq
basic.forever(on_forever)