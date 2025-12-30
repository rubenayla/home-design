# Water
Take the water from the rain, filter it, and store it clean. This allows us to add water with a truck in case of drought.

Drinking water, grey water, and dirty water will be separate.

Make some hump at the lower part of the property to keep rainwater and make it filter into the ground.

## Heating

The house will have no gas, so there must be a system to heat the water with electricity (or solar energy).

!!! note "Rant: point-of-use water heating"
    In Europe we spend lots of money to build huge systems to heat buildings with gas, all those radiators, pipes, the labor to install it, then spend over 2k for the boiler which is going to break and cause more costs, to then have a higher energy bill every month while emitting CO2 and paying Russia for the gas. That only solves half the problem, since in places like Spain you could argue that cooling is even more important than heating. On top of that, we wait while several liters of water go down the drain until the boiler water arrives at the tap.

    What we could be doing is just warm the water in the taps themselves with small electric heaters (commonly used in Brazil), powered by the sun with solar panels that are cheap now. You get instant hot water, you don't waste water, it's renewable, it's cheaper to operate, and the cost of installation is about 10x lower, while requiring less maintenance too.

1. Investigate taps that can warm water instantly, without a boiler. This would provide hot water instantly, without wasting water.
2. Investigate an electric boiler with heat pump. This lets the use of electricity when it is cheapest and most abundant.


# HVAC - Temp of air
The system will use first all the natural resources available, opening and closing windows, curtains, etc. Then, it will use the heat pump to get the perfect temperature.

```python
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
```

The workshop needs good air circulation, so it will use electric radiant or infrared panel heaters.

Ventilation from window at west to the attic (chimney effect), kitchen and bathroom.

!!! note "Discarded"
    - Heated floor
        - A simple heat pump (split) should be more than enough

!!! info "Heat exchanger"
    A heat exchanger (or recuperator) will continuously keep the air fresh, and eliminates the need to ventilate the house and then warm it up again. This saves energy while improving air quality.

    Can be done with rotary heat exchangers, or ducted plate.

!!! tip "Actuated windows"
    To ventilate faster and automatically, for example in summer nights, to keep the house cool with 0 energy, at least 2 windows in opposite sides of the house will have an actuator to open and close automatically.

!!! warning "Insulation and thermal mass"
    **Big thermal mass inside. The house and hot water of the tank can be heated/cooled when power is cheapest or more abundant, and the heat stored for later.**

    - The thermal mass will shift the warm part of the day towards the afternoon.
    - If you ventilate the house when it's cold, thermal mass will bake it more expensive to warm up again. The house should remain sealed if undesired temps.
    - Methods to increase thermal mass: slabs, water, water wall…
    - In summer, you could ventilate at night and keep the house cool all day
    - In winter, you could heat at noon, when the solar panels are at full power and the outside air is warmest (so the heat pump takes less energy)
