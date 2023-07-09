# Adafruit CircuitPython 8.0.5 on 2023-03-31; Waveshare RP2040-Zero with rp2040
# >>> import board
# >>> print(dir(board))
# ['__class__', '__name__', 'A0', 'A1', 'A2', 'A3', 'GP0', 'GP1', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP2', 'GP20', 'GP21', 'GP22', 'GP23', 'GP24', 'GP25', 'GP26', 'GP26_A0', 'GP27', 'GP27_A1', 'GP28', 'GP28_A2', 'GP29', 'GP29_A3', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'NEOPIXEL', 'RX', 'TX', 'UART', 'board_id']

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide

keyboard = KMKKeyboard()

# keyboard.debug_enabled = True

keyboard.col_pins = (board.GP7,board.GP8,board.GP9,board.GP10,board.GP11,board.GP12,board.GP13,board.GP14)
keyboard.row_pins = (board.GP4,board.GP3,board.GP2,board.GP1,board.GP0)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())
MO_1 = KC.MO(1)
LT_1_MHEN = KC.LT(1, KC.MHEN)
LT_1_HENK = KC.LT(1, KC.HENK)
LT_1_PSCR = KC.LT(1, KC.PSCR)

keyboard.keymap = [
[
# L-GP7    L-GP8    L-GP9    L-GP10     L-GP11  L-GP12  L-GP13  L-GP14  R-GP7   R-GP8     R-GP9      R-GP10    R-GP11     R-GP12    R-GP13    R-GP14
	KC.ESC,  KC.N1,   KC.N2,   KC.N3,     KC.N4,  KC.N5,  KC.NO,  KC.NO,  KC.N6,  KC.N7,    KC.N8,     KC.N9,    KC.N0,     KC.MINS,  KC.EQL,   KC.JYEN,
	KC.TAB,  KC.Q,    KC.W,    KC.E,      KC.R,   KC.T,   KC.NO,  KC.NO,  KC.Y,   KC.U,     KC.I,      KC.O,     KC.P,      KC.LBRC,  KC.RBRC,  KC.BSPC,
	MO_1,    KC.A,    KC.S,    KC.D,      KC.F,   KC.G,   KC.NO,  KC.NO,  KC.H,   KC.J,     KC.K,      KC.L,     KC.SCLN,   KC.QUOT,  KC.BSLS,  KC.ENT,
	KC.LSFT, KC.Z,    KC.X,    KC.C,      KC.V,   KC.B,   KC.NO,  KC.NO,  KC.N,   KC.M,     KC.COMM,   KC.DOT,   KC.SLSH,   KC.RO,    KC.UP,    KC.RSFT,
	KC.LCTL, KC.LGUI, KC.LALT, LT_1_MHEN, KC.SPC, KC.NO,  KC.NO,  KC.NO,  KC.NO,  KC.MINS,  LT_1_HENK, KC.RALT,  LT_1_PSCR, KC.LEFT,  KC.DOWN,  KC.RIGHT
],
[
# L-GP7    L-GP8    L-GP9    L-GP10     L-GP11  L-GP12  L-GP13   L-GP14   R-GP7   R-GP8     R-GP9      R-GP10    R-GP11     R-GP12    R-GP13    R-GP14
  KC.TRNS, KC.F1,   KC.F2,   KC.F3,     KC.F4,  KC.F5,  KC.TRNS, KC.TRNS, KC.F6,  KC.F7,    KC.F8,     KC.F9,    KC.F10,    KC.F11,   KC.F12,   KC.TRNS, 
  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,KC.TRNS,KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.DEL,
  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,KC.TRNS,KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,  KC.TRNS,
  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,KC.TRNS,KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.PGUP,  KC.TRNS,
  KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,KC.TRNS,KC.TRNS, KC.TRNS, KC.TRNS,KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS,   KC.HOME,  KC.PGDN,  KC.END
]
]

split = Split(
	split_flip = False,
	uart_flip = True,
	use_pio = True,
	data_pin = board.GP26,
	data_pin2 = board.GP27
)
keyboard.modules.append(split)

if __name__ == '__main__':
	keyboard.go()
