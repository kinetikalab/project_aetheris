# Description

Design of a high-voltage resonant transformer (L1-L2). See the equivalent circuit diagram in [equivalent_circuit](/power_electronics/equivalent_circuit).

The current coupling coefficient achieved is **k = 0.99**, which is why, in the resonant circuit, we need an additional coil (I used 6 turns of 3x20x0.2 mm litz wire on an MS-250026-2 core, ~5 μH).

- **Secondary winding parasitic capacitance:** 11 pF  
- **Interwinding parasitic capacitance:** 10 pF  

## Design

### Materials Needed

1. Nanocrystal core: [T60006-L2090-W518 Vacuumschmelze](https://eu.mouser.com/ProductDetail/Vacuumschmelze/T60006-L2090-W518?qs=ePbE9GiMmvUhadR4ky1MIg%3D%3D)
2. Coated copper wire: [0.3 mm](https://www.amazon.de/-/en/dp/B09VP9QQGW?ref=ppx_yo2ov_dt_b_fed_asin_title)
3. Polyimide tape: [Example](https://www.amazon.de/-/en/dp/B0C1JF96MG?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
4. Housing: [Example](/power_electronics/transformer/Transformer.f3d)
5. Potting compound (optional)
6. Litz wire for primary windings (I used 3x20x0.2 mm wire)

### Process

1. Wind the secondary winding using 0.3 mm coated wire, approximately 130 turns.  
   **IMPORTANT:** Maintain a spacing of ~0.2–0.3 mm between turns to minimize parasitic capacitance.
2. Insulate the secondary winding with 3–4 layers of polyimide tape. Optionally, you can apply potting compound for additional protection.
3. Wind 3 primary windings. Refer to the provided 3D model for detailed instructions.

## Comments

1. The T60006-L2090-W518 core is used because it has very low losses and ensures exceptional magnetic permeability. This allows for **fewer turns**, which reduces parasitic capacitance.
2. Litz wire, or even a bundle of Litz wires, is essential due to the high current in the primary windings. It minimizes the skin effect and improves efficiency.
3. Polyimide tape or potting compound is critical for insulation to prevent breakdowns between the secondary and primary windings.