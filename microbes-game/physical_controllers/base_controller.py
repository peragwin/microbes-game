# This script is intended for MicroPython on an ESP32.
# It requires the 'umqtt.simple' library for MQTT communication.

# from umqtt.simple import MQTTClient
import time

class BaseController:
    def __init__(self, microbe_id, mqtt_server, client_id_prefix="microbe_controller"):
        self.microbe_id = microbe_id
        self.mqtt_server = mqtt_server
        self.client_id = f"{client_id_prefix}_{microbe_id}"
        self.command_topic = f"microbes/{self.microbe_id}/command"
        self.status_topic = f"microbes/{self.microbe_id}/status"

        # Placeholder for the MQTT client
        self.mqtt_client = None
        # self.mqtt_client = MQTTClient(self.client_id, self.mqtt_server)
        # self.mqtt_client.set_callback(self.on_message_received)

        print(f"Controller for microbe {self.microbe_id} initialized.")

    def connect(self):
        """Connect to the MQTT broker and subscribe to the command topic."""
        try:
            # print(f"Connecting to MQTT broker at {self.mqtt_server}...")
            # self.mqtt_client.connect()
            # print("Connected successfully.")
            # self.mqtt_client.subscribe(self.command_topic)
            # print(f"Subscribed to topic: {self.command_topic}")
            # self.publish_status("online")
            print("Placeholder: Would connect to MQTT and subscribe.")
            return True
        except Exception as e:
            print(f"Failed to connect to MQTT broker: {e}")
            return False

    def on_message_received(self, topic, msg):
        """Callback function to handle incoming MQTT messages."""
        command = msg.decode('utf-8')
        print(f"Received command on topic {topic.decode('utf-8')}: {command}")
        self.handle_command(command)

    def handle_command(self, command):
        """Parse the command and call the appropriate action method."""
        # This is a simple parser. A more robust implementation might use JSON.
        parts = command.split('(')
        action = parts[0]
        params = parts[1][:-1] if len(parts) > 1 else ""

        if hasattr(self, action):
            method = getattr(self, action)
            print(f"Executing action: {action} with params: {params}")
            try:
                method(params)
                self.publish_status(f"executed_{action}")
            except Exception as e:
                print(f"Error executing action '{action}': {e}")
                self.publish_status(f"error_{action}")
        else:
            print(f"Unknown command: {action}")
            self.publish_status(f"unknown_command_{action}")

    def publish_status(self, status):
        """Publish a status message to the status topic."""
        # print(f"Publishing status '{status}' to {self.status_topic}")
        # self.mqtt_client.publish(self.status_topic, status)
        print(f"Placeholder: Would publish status '{status}'.")

    def listen(self):
        """Listen for incoming messages in a loop."""
        print("Starting to listen for commands...")
        while True:
            try:
                # self.mqtt_client.check_msg()
                print("Placeholder: Checking for MQTT messages...")
                time.sleep(1) # Prevent busy-waiting
            except Exception as e:
                print(f"An error occurred in the listening loop: {e}")
                self.connect() # Attempt to reconnect

    # --- Placeholder Action Methods ---
    # These would be implemented to control hardware (motors, lights, etc.)

    def move(self, params):
        """Placeholder for moving the animatronic."""
        print(f"ACTION: Moving with parameters: {params}")

    def emote(self, params):
        """Placeholder for making the animatronic emote."""
        print(f"ACTION: Emoting with parameters: {params}")
