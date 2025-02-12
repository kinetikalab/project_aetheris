# Description

This is a simplified LTSPICE model of power electronics. 

The H-bridge is substituted by an AC power supply for simplicity (for the detailed design of the H-bridge, see the [h-bridge](/power_electronics/h-bridge) folder).

### Key Components:

- **C1**: Balance capacitor battery.
- **Ls1**: Primary leakage inductance.
- **Ls2**: Secondary leakage inductance.
- **Lm1**: Primary magnetizing inductance.
- **Lm2**: Secondary magnetizing inductance.
- **k**: Coupling factor. Learn how to measure it [here](https://electronics.stackexchange.com/questions/596093/how-to-measure-coupling-coefficient).
- **R1**: Resistance of the secondary winding.
- **Cd**: Capacity of the discharge chamber.
- **Rd**: Resistance of the discharge chamber (theoretical infinity, but in discharge breakdown ~100 kΩ).
- **Cp**: Parasitic capacity (secondary winding).
- **Cw**: Parasitic capacity (Inter-winding).


### Additional Information:

- For more information on the H-bridge design, please refer to the [h-bridge](/power_electronics/h-bridge) folder.
- For detailed transformer design, check the [transformer](/power_electronics/transformer) folder.
