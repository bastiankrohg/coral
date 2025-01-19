from components.coral_vision import Vision
from components.coral_telemetry import Telemetry
from components.mission_ctrl import MissionControl

# Define the Coral class
class Coral:
    def __init__(self):
        self.telemetry = Telemetry()
        self.vision = Vision()
        self.mission_control = MissionControl()
