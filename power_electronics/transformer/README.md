# Description

Design of a high-voltage resonant transformer (L1-L2). See the equivalent circuit diagram in [equivalent_circuit](/power_electronics/equivalent_circuit).

The current coupling coefficient achieved is **k = 0.85**, but by increasing the number of secondary and therefore primary windings, a **k > 0.95** can be achieved.

## Design

### You Need
1. Two ferrite cores [MS-250026-2 MICROMETALS](https://www.tme.eu/en/details/ms-250026-2/ring-ferrites/micrometals/)
2. Coated copper wire [0.2-0.3 mm](https://www.amazon.de/-/en/dp/B09VP9QQGW?ref=ppx_yo2ov_dt_b_fed_asin_title)
3. [Polyimide tape Tape](https://www.amazon.de/-/en/dp/B0C1JF96MG?ref=ppx_yo2ov_dt_b_fed_asin_title&th=1)
4. Filling form. [Example](/power_electronics/equivalent_circuit/transformer/housing.stl)
5. Epoxy Resin or Liquid Silicone
6. Litz Wire for primary windings

### Process
1. Wind the secondary winding with 0.2-0.3 mm coated wire. Create two layers with approximately 200-300 turns each. **IMPORTANT:** Carefully isolate each layer with 2-3 layers of polyamide tape. Here is an [example](/power_electronics/equivalent_circuit/transformer/sw.jpg) of the secondary winding.
2. Insert the coil into the filling form and fill it with epoxy resin or silicone.
3. Wind 4-6 primary windings above the cast coil. Primary windings must be uniformly distributed around the coil.

## Comments
1. We use MS-250026-2 sendust material because sendust has a low and very stable magnetic permeability with low losses. Low magnetic permeability is important because if your primary inductance is large (for example, if you use ferrite 77 with μ~2000), you are not able to find a resonant frequency in the range of 100-1000 kHz.
2. Filling with epoxy resin or silicone is essential; otherwise, you will face transformer breakdown.
3. Use Litz wire or even a Litz wire bundle due to the high current in primary windings. Litz wire is required to minimize the skin effect.
4. A polyamide tape layer is essential; otherwise, you will face breakdown between the secondary winding layers.
