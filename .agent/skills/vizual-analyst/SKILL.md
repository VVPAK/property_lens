---
name: vizual-analyst
description: Generation of data structures for UI visualization (Charts, Maps, Heatmaps). Formats analytics into frontend-ready JSON.
---
# Vizual Analyst Skill

## Visualization Logic
- **Price Trends**: Data aggregation by month (Median Price per SQFT).
- **Supply/Demand**: Ratio of active listings to closed transactions per period.
- **Heatmaps**: Map coordinates (Lat/Long) for Mapbox rendering.

## Quality Standards
1. **No Outliers**: Exclude extreme values (data entry errors) from mean/median calculations.
2. **Context**: All charts must include comparative metrics (MoM, YoY).
3. **B2B Focus**: Prioritize ROI, Rental Yield, and Capital Appreciation metrics.

## Output Format
- Strict JSON compatible with Chart.js or Recharts.