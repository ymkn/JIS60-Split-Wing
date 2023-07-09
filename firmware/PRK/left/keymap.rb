kbd = Keyboard.new

kbd.init_pins(
  [ 4, 3, 2, 1, 0 ], # row
  [ 7, 8, 9, 10, 11, 12 ]  # col
)

kbd.add_layer :default, %i(
  KC_ESC      KC_1    KC_2    KC_3    KC_4  KC_5
  KC_TAB      KC_Q    KC_W    KC_E    KC_R  KC_T
  KC_CAPSLOCK KC_A    KC_S    KC_D    KC_F  KC_G
  KC_LSFT     KC_Z    KC_X    KC_C    KC_V  KC_B
  KC_LCTL     KC_LGUI KC_LALT KC_MHEN KC_SPACE
)

kbd.start!
