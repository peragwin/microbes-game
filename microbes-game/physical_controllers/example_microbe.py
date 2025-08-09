# This script is an example of how to use the BaseController for a specific microbe.
# It's intended for MicroPython on an ESP32.

from base_controller import BaseController

# --- Configuration ---
MICROBE_ID = 1
MQTT_BROKER = "192.168.1.100" # <-- IMPORTANT: Change this to your MQTT broker's IP address

class UniqueMicrobeController(BaseController):
    def __init__(self, microbe_id, mqtt_server):
        # Call the parent class constructor
        super().__init__(microbe_id, mqtt_server)
        print(f"UniqueMicrobeController for microbe {self.microbe_id} is ready.")

    # --- Overriding Base Methods (Optional) ---
    def handle_command(self, command):
        """
        You can override the command handler to add custom logic or parsing
        before calling the parent's handler.
        """
        print("UniqueMicrobeController is handling the command.")
        # Call the original handler from the parent class
        super().handle_command(command)

    # --- Adding a Unique Ability ---
    def glow(self, params):
        """
        A unique action specific to this type of microbe.
        This would control an RGB LED or similar hardware.
        """
        # Params might be a string like "blue,100" for color and intensity
        color, intensity = params.split(',')
        print(f"ACTION: Glowing with color {color} at {intensity}% intensity.")
        # Add hardware control logic here
        # e.g., self.led.set_color(color, int(intensity))


# --- Main Execution Logic ---
if __name__ == "__main__":
    print("Setting up the example microbe controller...")

    # Create an instance of our unique controller
    microbe_controller = UniqueMicrobeController(MICROBE_ID, MQTT_BROKER)

    # Connect to the MQTT broker
    if microbe_controller.connect():
        # Start listening for commands
        # This will run forever.
        microbe_controller.listen()
    else:
        print("Could not connect to MQTT. Please check the configuration and network.")

    print("Script finished.") # This line will likely not be reached
