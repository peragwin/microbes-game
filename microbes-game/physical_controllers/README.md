# Physical Controllers

This directory contains the MicroPython code designed to run on ESP32 microcontrollers. Each controller corresponds to one of the physical microbe animatronics.

## Purpose

The code allows the animatronics to receive commands from the main Unity application via an MQTT message broker and act upon them. This enables the physical state of the animatronics to be synchronized with the digital state in the game.

## Files

-   `base_controller.py`: A generic base class that handles MQTT connection, subscription, and command parsing. It includes placeholder methods for common actions like `move()` and `emote()`.
-   `example_microbe.py`: An example of how to extend the `BaseController` for a specific microbe. It shows how to add unique abilities (e.g., `glow()`) and provides the main execution logic.

## Dependencies

This code is written for MicroPython and requires an MQTT client library. The recommended library is `umqtt.simple`. You will need to ensure this library is present on your MicroPython device.

You can install it using `upip` if your MicroPython build includes it:

```
import upip
upip.install('micropython-umqtt.simple')
```

Alternatively, you can manually copy the `umqtt/simple.py` file to your device's `lib` directory.

## Usage

1.  **Configure:** Edit `example_microbe.py` (or a copy of it) and set the `MQTT_BROKER` IP address to match your local broker.
2.  **Upload:** Upload the scripts (and the `umqtt` library) to your ESP32 device.
3.  **Run:** Execute the `example_microbe.py` script on the device. It will automatically connect to the broker and start listening for commands on its unique topic (`microbes/{microbe_id}/command`).
