class HVACSystem:
    """
    I have no range parameter because the system will be at the right temp with the heat pump running to maintain the desired temperature, so it's useless.
    """
    def __init__(self, desired_temperature=22, tolerance=2, hysteresis=0.2):
        self.T_d = desired_temperature
        self.hysteresis = hysteresis
        # Assume initial states
        self.hvac_on = False
        self.curtains_open = False
        self.windows_open = False
        self.system_on = False
        self.daytime = True  # This should be dynamically determined
        self.exchanger = True

    def update_environment(self, T_o, T_i, T_d, daytime):
        """
        The blocking curtains and windows are controlled based on the temperatures, with hysteresis to prevent rapid constant switching.

        After the curtains and windows are controlled, the HVAC system is managed, only if the temperature is outside the desired range.
        """
        
        T_delta = T_d - T_i
        
        # Curtains (Control ignoring everything else)
        if daytime:
            if T_delta > self.hysteresis:
                self.open_curtains()
            elif -T_delta < self.hysteresis:
                self.close_curtains()
        else:
            # Close for privacy and darkness at night, we can ventilate for cold.
            # This may change if I want to wake up with sunlight
            self.close_curtains()
        
        # Windows and heat pump
        # Check that the signs are the same, and the difference is large enough to bother opening the windows.
        if (T_o - T_i) * (T_d - T_i) > self.hysteresis:
            self.open_windows()
            self.exchanger = False
            self.turn_heatpump_off()
        elif (T_o - T_i) * (T_d - T_i) < 0:
            self.close_windows()
            self.exchanger = True
            self.turn_heatpump_on(T_o, T_i, T_d)

    def open_curtains(self):
        self.curtains_open = True
        print("Curtains opened")

    def close_curtains(self):
        self.curtains_open = False
        print("Curtains closed")

    def open_windows(self):
        self.windows_open = True
        print("Windows opened")

    def close_windows(self):
        """Either to block sunlight, get darkness at night, or prevent heat from escaping at night
        """
        self.windows_open = False
        print("Windows closed")

    def turn_heatpump_on(self, T_o, T_i, T_d):
        self.hvac_on = True
        print("HVAC turned on")
        self.manage_pump(T_o, T_i, T_d)
    
    def turn_heatpump_off(self):
        self.hvac_on = False
        print("HVAC turned off")
    
    def manage_pump(self, T_o, T_i, T_d):
        # Control the heatpump...
        print("Heatpump updating data...")

    def turn_on_system(self):
        self.system_on = True
        print("System turned on")

    def turn_off_system(self):
        self.system_on = False
        print("System turned off")

if __name__ == "__main__":
    hvac = HVACSystem(desired_temperature=22)

    print(f"Cold outside, warm inside, I want warmer inside, it's daytime.")
    hvac.update_environment(T_o=10, T_i=22, T_d=23, daytime=True)

    print(f"\nCold inside, warm outside, I want very warm, it's daytime.")
    hvac.update_environment(T_o=22, T_i=19, T_d=23, daytime=True)

    print(f"\nToo hot summer, blazing hot outside, I want cooler inside, it's daytime.")
    hvac.update_environment(T_o=40, T_i=30, T_d=25, daytime=True)

    print(f"\nToo hot summer, finally cool at night")
    hvac.update_environment(T_o=20, T_i=30, T_d=25, daytime=False)

    print(f"\nToo hot summer, got the system to ventilate at night, now it's too cold.")
    hvac.update_environment(T_o=18, T_i=21, T_d=22, daytime=False)