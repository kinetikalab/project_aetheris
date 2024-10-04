# Project Aetheris
Open source project for plasma water purification

# Water Purification Plasma Chemistry 101

Plasma water purification and activation is a well-known process based on the generation of Reactive Oxygen and Nitrogen Species (RONS) in a plasma discharge, which subsequently oxidize organic impurities and degrade pathogens in water.

## Key Reactions

The hydroxyl radical (OH) plays a critical role in this process. In the literature, the following reaction is often mentioned:

`e + H2O -> OH + H`

However, this reaction requires electron energies greater than **9 eV**, which are rare in atmospheric-pressure gas discharges in air. Additionally, this is a slow reaction. A more efficient way to generate OH is through the following reaction involving excited atomic oxygen:

`e + O2 -> O(1D) + O(3P)`
`H2O + O(1D) -> OH + OH`
`O2 + O(1D) -> O2 + O`
`N2 + O(1D) -> N2 + O`


The dissociation of O₂ is much faster than that of H₂O. After O(1D) is formed, it is a highly reactive species that most likely reacts with N₂, O₂, or H₂O. The balance between H₂O, O₂, and N₂ depends on their concentrations. In dry, cold air, about 90% of O(1D) is lost due to relaxation with N₂ and O₂, but in hot, humid air, around 20% of O(1D) is lost due to relaxation.


![Reactions cress sections - **Morgan (Kinema Research & Software)** database and **IST-Lisbon** database, www.lxcat.net, retrieved on Aug 3, 2024.](./images/cs_OH.png)

These reactions are well understood, but the importance of igniting plasma in warm, humid air is often not clearly emphasized in the literature.

## Ozone's Role in Plasma Chemistry

Another critical factor is the presence of ozone (O₃), as it prolongs the lifespan of OH through well-known atmospheric chemistry cycles involving ozone destruction:

`OH + O3 -> O2 + HO2`
`HO2 + O3 -> OH + 2O2`

While these reactions are not particularly fast, ozone is a stable molecule and can accumulate in the discharge chamber, reaching high concentrations. Furthermore, HO₂ is a reactive radical that easily dissolves in water, generating hydroxyl radicals in the liquid phase. It plays a significant role in Advanced Oxidation Processes (AOPs) in water.

## In Summary

An ozone-hydroxyl mixture in highly humid air is an excellent combination for mixing with contaminated water.

# Basic Design Principles

1. **Separation of Plasma and Water**  
   It is not necessary to treat contaminated water by directly applying plasma to its surface. This approach is inefficient and difficult to scale. Instead, we generate the ozone-hydroxyl mixture separately and mix it with the water.

2. **Discharge Chamber Design**  
   The most effective method is to feed the discharge chamber with humidified air, then mix the activated air-vapor mixture with the water. An ejector system seems to be the most efficient way to achieve this.

3. **Oxygen and Nitrogen Control**  
   Since ozone is required for higher efficiency, a circulation system during the treatment process is essential. Alternatively, nitrogen should be removed from the water tank at the beginning of the treatment process for better results.

# Overall Device Design

![Schematic Design](./images/design.jpg)

- **Power Electronics**: See the [power_electronics](./power_electronics/).
- **Discharge Chamber**: See the [discharge_chambers](./discharge_chambers/).
- **Ejector (E)**: For simple ejector models and mixing system dimensions, refer to the [ejector_model](./ejector_model/). Note: the ejector is often combined with the discharge chamber, but these models provide key inputs for the mixing system design.
- **O₂ Filter**: A standard O₂ concentrator with molecular sieves.

# Additional information
2-dimentional gas dicharge model (С parallel code) with plasma-fluid drift-diffusion approximation here [discharge_model](./discharge_model/)
