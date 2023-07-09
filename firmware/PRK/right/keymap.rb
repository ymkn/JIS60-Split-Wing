kbd = Keyboard.new

kbd.init_pins(
  [ 4, 3, 2, 1, 0 ], # row
  [ 7, 8, 9, 10, 11, 12, 13, 14 ]  # col
)

kbd.add_layer :default, %i(
  KC_6      KC_7      KC_8      KC_9      KC_0        KC_MINUS    KC_EQUAL    KC_INT3
  KC_Y      KC_U      KC_I      KC_O      KC_P        KC_LBRACKET KC_RBRACKET KC_BSPACE
  KC_H      KC_J      KC_K      KC_L      KC_SCOLON   KC_QUOTE    KC_BSLASH   KC_ENTER
  KC_N      KC_M      KC_COMMA  KC_DOT    KC_SLASH    KC_INT1     KC_UP       KC_RSFT 
  KC_NO     KC_ENTER  KC_HENK   KC_RALT   KC_PSCREEN  KC_LEFT     KC_DOWN     KC_RIGHT
)

kbd.start!
