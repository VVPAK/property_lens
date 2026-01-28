---
name: real-estate-expert
description: Domain expert for the Dubai real estate market. Used for validating terminology, calculating ROI/LTV, and classifying transactions (Off-plan vs. Secondary).
---
# Real Estate Expert Skill

## Domain Logic
1. **Transaction Types**: Distinguish between Sales, Mortgages, and Gifts. Primary focus on Sales data.
2. **Property Status**:
   - Off-plan: Validate registrations via Oqood.
   - Ready/Secondary: Validate via Title Deed.
3. **District Mapping**: Knowledge of hierarchy (Community -> Sub-community). Example: Dubai Marina -> JBR.

## Financial Calculations (Strict)
- **Gross ROI** = (Annual Rent / Purchase Price) * 100
- **Net ROI** = ((Annual Rent - Service Charges) * 100) / Purchase Price
- **Service Charges**: Always utilize Mollak System rates for precision.

## Constraints
- Never confuse Freehold (full ownership) with Leasehold (99-year lease).
- Factor in the 4% DLD Fee in all entry-cost calculations.