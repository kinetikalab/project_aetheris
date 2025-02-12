# Description

Design of a high-voltage resonant transformer (L1-L2). See the equivalent circuit diagram in [equivalent_circuit](/power_electronics/equivalent_circuit).

The current coupling coefficient achieved is **k = 0.99**.

- **Secondary winding parasitic capacitance:** 11 pF  
- **Interwinding parasitic capacitance:** 10 pF  

## Design

### Materials Needed

1. Nanocrystal core: [T60006-L2090-W518 Vacuumschmelze](https://eu.mouser.com/ProductDetail/Vacuumschmelze/T60006-L2090-W518?qs=ePbE9GiMmvUhadR4ky1MIg%3D%3D)
2. Coated copper wire: [0.3 mm](https://www.amazon.de/-/en/dp/B09VP9QQGW?ref=ppx_yo2ov_dt_b_fed_asin_title)
3. Housing: [CAD model](/power_electronics/transformer/High-Voltage_Transformer.f3d)
4. Potting compound 
5. Litz wire for primary windings (I used 3x20x0.2 mm wire)

### Process
See transformer design [CAD Model](/power_electronics/transformer/High-Voltage_Transformer.f3d)
**Insulation of the core**
1. Put core intto filling form (do no forget add silcon overaly)
2. Fill the form with potting compound and wait until it cure. 
It is important to avoid core breakdown.
**Secondary windings**
3. Wind the secondary winding using 0.3 mm coated wire, approximately 130 turns.  
   **IMPORTANT:** Maintain a spacing of ~0.2–0.3 mm between turns to minimize parasitic capacitance.
4. Fill the seondary winding with potting compound and wait until it cure.
**Primary windings**
5. Wind 3 primary windings. Refer to the provided 3D model for detailed instructions.

## Comments

1. The T60006-L2090-W518 core is used because it has very low losses and ensures exceptional magnetic permeability. This allows for **fewer turns**, which reduces parasitic capacitance.
2. Litz wire, or even a bundle of Litz wires, is essential due to the high current in the primary windings. It minimizes the skin effect and improves efficiency.
3. Potting compound is critical for insulation to prevent breakdowns between the secondary and primary windings or core breakdown.