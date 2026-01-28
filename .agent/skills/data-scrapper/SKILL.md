---
name: data-scraper
description: Skill for designing scrapers for listings (Bayut, Property Finder) and government registries. Focuses on anti-bot bypass and data integrity.
---
# Data Scraper Skill

## Technical Stack
- **Engine**: Playwright / Puppeteer (for SPA rendering).
- **Proxy**: Rotating Residential Proxies (mandatory for high-frequency targets like DXB Interact).
- **Fingerprinting**: Emulation of real Canvas/WebRTC parameters.

## Extraction Protocol
1. **Schema Matching**: Map raw data into the unified Nexus RE JSON schema.
2. **De-duplication**: Hash records by [Price + Floor + Layout + Building] to identify duplicate listings from different agencies.
3. **Change Data Capture (CDC)**: Track Price History as a primary investor trigger.

## Error Handling
- On 403/429 errors: Auto-rotate proxy nodes and implement exponential backoff.
- Validation: Drop records missing SQFT or Price fields.