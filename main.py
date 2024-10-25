サイコロの目 = 0

def on_gesture_shake():
    global サイコロの目
    サイコロの目 = randint(1, 10)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_forever():
    if サイコロの目 == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif サイコロの目 == 2:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . . . .
            . . . . .
            . . . . #
            """)
    elif サイコロの目 == 3:
        basic.show_leds("""
            # . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . #
            """)
    elif サイコロの目 == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif サイコロの目 == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    else:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
basic.forever(on_forever)
