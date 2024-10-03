# Description

This is a simplified LTSPICE model of power electronics. 

The H-bridge is substituted by an AC power supply for simplicity (for the detailed design of the H-bridge, see the [power_electronics/h-bridge](power_electronics/h-bridge) folder).

### Key Components:

- **C1**: Main capacitor battery.
- **L1**: Primary winding inductance.
- **L2**: Secondary winding inductance (refer to the transformer design in the [power_electronics/transformer](power_electronics/transformer) folder).
- **k**: Coupling factor. Learn how to measure it [here](https://electronics.stackexchange.com/questions/596093/how-to-measure-coupling-coefficient).
- **R1**: Resistance of the secondary winding.
- **C2**: Capacity of the discharge chamber.
- **R2**: Resistance of the discharge chamber (theoretical infinity, but in discharge breakdown ~100 kΩ).

### Additional Information:

- For more information on the H-bridge design, please refer to the [power_electronics/h-bridge](power_electronics/h-bridge) folder.
- For detailed transformer design, check the [power_electronics/transformer](power_electronics/transformer) folder.
