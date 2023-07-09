# KMK Firmware

## 動作確認済みバージョン

- CircuitPython 8.0.5 (RP2040-Zero用)
  - adafruit-circuitpython-waveshare_rp2040_zero-ja-8.0.5.uf2
- KMK Firmware ([db7dc74](https://github.com/KMKfw/kmk_firmware/commit/db7dc7475225109aded850c923b10d1800329230))

## boot.py

シリアル接続とUSBストレージは無効化されています。これらを有効化するには、キーボードとPCをUSBケーブルで接続する前からESCキー（＝キーボードの一番左上のキー）を押したままにしてください。しばらくするとOSがUSBストレージを認識します。

## code.py

本ファイルにはキーマップが直接書かれているほか、ピン定義や分割キーボード用のコードが書かれています。キーマップを編集する際はそれらの処理部分を触らないように注意してください。