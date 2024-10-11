# Ejector model

Sipmle ejector model in based on Sokolov-Zinger model *Sokolov E.Ya. Jet-Stream Apparatuses. Sokolov E.Ya., Zinger N.M. Energoatomizdat, 1968*

Here is the dimentions
![Ejector dimentions](ejector.png)

## Python script
Use python `ejector_model.py` script for dimentions calculations

## Comments

**Designing an ejector (mixing) system involves optimizing two key parameters:**

1. **Air/Water volume ratio** – A higher ratio is better.
2. **Pressure in the discharge chamber** – Lower pressure improves discharge.

However, these two parameters contradict each other, so finding the right balance is the challenge.

**Current Setup:**
- Pressure in the discharge chamber: ~0.5 bar
- Pump: 7-8 bar / 10 L/min – It’s really not easy to find a high-quality pump that can meet these specifications.
- Air/Water volume ratio: 2-3
