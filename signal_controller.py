import time
import threading

GREEN_TIME = 10
YELLOW_TIME = 5

class TrafficSignalController:
    def __init__(self):
        self.lanes = ["LANE_1", "LANE_2", "LANE_3", "LANE_4"]

        self.current_index = 0
        self.current_green = self.lanes[0]
        self.current_phase = "GREEN"  # GREEN / YELLOW

        self.mode = "NORMAL"          # NORMAL / EMERGENCY
        self.emergency_lane = None

        self.priority_enabled = True
        self.priority_duration = 15

        self.lock = threading.Lock()
        threading.Thread(target=self._normal_cycle, daemon=True).start()

    # --------------------------------------------------
    # NORMAL SIGNAL CYCLE
    # --------------------------------------------------
    def _normal_cycle(self):
        while True:
            with self.lock:
                if self.mode != "NORMAL":
                    # ⛔ Pause normal cycle completely during emergency
                    pass
                else:
                    self.current_green = self.lanes[self.current_index]
                    self.current_phase = "GREEN"

            time.sleep(GREEN_TIME)

            with self.lock:
                if self.mode != "NORMAL":
                    continue
                self.current_phase = "YELLOW"

            time.sleep(YELLOW_TIME)

            with self.lock:
                if self.mode == "NORMAL":
                    self.current_index = (self.current_index + 1) % len(self.lanes)

    # --------------------------------------------------
    # EMERGENCY MODE (SAFE + DETERMINISTIC)
    # --------------------------------------------------
    def trigger_emergency(self, lane):
        if not self.priority_enabled:
            return

        def emergency_flow():
            with self.lock:
                # 🟡 Transition current lane safely
                self.mode = "EMERGENCY"
                self.current_phase = "YELLOW"

            time.sleep(YELLOW_TIME)

            with self.lock:
                # 🟢 Give GREEN to EMERGENCY lane
                self.emergency_lane = lane
                self.current_green = lane
                self.current_phase = "GREEN"

            time.sleep(self.priority_duration)

            with self.lock:
                # 🟡 Emergency lane yellow before exit
                self.current_phase = "YELLOW"

            time.sleep(YELLOW_TIME)

            with self.lock:
                # 🔁 Resume normal cycle from NEXT lane
                self.mode = "NORMAL"
                self.emergency_lane = None
                self.current_index = (self.lanes.index(lane) + 1) % len(self.lanes)
                self.current_green = self.lanes[self.current_index]
                self.current_phase = "GREEN"

        threading.Thread(target=emergency_flow, daemon=True).start()

    # --------------------------------------------------
    # ADMIN CONTROLS
    # --------------------------------------------------
    def reset(self):
        with self.lock:
            self.mode = "NORMAL"
            self.emergency_lane = None
            self.current_index = 0
            self.current_green = self.lanes[0]
            self.current_phase = "GREEN"

    def set_duration(self, seconds):
        with self.lock:
            self.priority_duration = seconds

    def toggle_priority(self, enabled):
        with self.lock:
            self.priority_enabled = enabled
            if not enabled:
                self.reset()

    # --------------------------------------------------
    # STATUS API
    # --------------------------------------------------
    def get_status(self):
        with self.lock:
            signals = {}
            for lane in self.lanes:
                if lane == self.current_green:
                    signals[lane] = self.current_phase
                else:
                    signals[lane] = "RED"

            return {
                "mode": self.mode,
                "signals": signals,
                "emergency_lane": self.emergency_lane,
                "priority_enabled": self.priority_enabled,
                "priority_duration": self.priority_duration
            }

# ✅ SINGLE GLOBAL INSTANCE
controller = TrafficSignalController()
