# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.0] - 2026-01-28

### 🚀 Added
- **AI Agent Core**: Implemented LangGraph-based agent with OpenAI GPT-4o integration.
- **Agent Tools**:
  - `ScraperService`: Headless browser automation using Playwright for real-time data.
  - `ROICalculator`: Financial modeling tool for Gross/Net ROI and Cap Rate.
- **Frontend UI**:
  - Premium Chat Interface (`Chat.tsx`) with "Consultant" aesthetic.
  - Interactive features: Suggestions, Markdown rendering, Mobile-first layout.
- **Backend Infrastructure**:
  - FastAPI service structure with Pydantic v2 validation.
  - PostgreSQL database configuration with `pgvector` extension.
  - Async SQLAlchemy session management.
- **DevOps**:
  - Docker support: `Dockerfile` for both services and `docker-compose.yml` orchestration.
  - Environment configuration templates.
- **Documentation**:
  - Comprehensive `README.md`.
  - Agent Skills library (`product-designer`, `ux-writer`, `real-estate-expert`).

### 🐛 Fixed
- Resolved Next.js `missing root layout` error by implementing `layout.tsx`.
- Fixed React Client Manifest cache collisions in Turbopack.
- Corrected import paths for LangChain `AgentExecutor` (migrated to `create_react_agent`).

### 💅 Styled
- Applied "Premium Real Estate" design system (Slate/Indigo palette).
- Enhanced typography and spacing in Chat components via CSS Modules.
