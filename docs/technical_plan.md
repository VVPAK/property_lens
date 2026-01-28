# Property Lens - Technical Implementation Plan

## Technology Stack

### Frontend (Mobile-First Web / PWA)
- **Framework**: **Next.js** (React)
    - Chosen for: SEO (Critical for organic traffic), Performance, Fast Development.
    - Strategy: Build as a PWA (Progressive Web App) to mimic mobile app feel initially.
- **Language**: TypeScript
- **Styling**: CSS Modules / Vanilla CSS (Modern, lightweight)
- **State Management**: React Hooks / Context

### Backend (API & AI)
- **Framework**: **FastAPI** (Python)
    - Chosen for: Native AI integration (PyTorch/OpenAI), Async performance, Data processing capabilities.
- **Database**: **PostgreSQL** (Relational data for users, properties, transactions).
- **AI Integration**: OpenAI API / Local LLMs query processing.

## Architecture Overview
1.  **Client (Next.js)**: Handles UI, User Interaction, and Chat Interface.
2.  **API Gateway (Nginx/FastAPI)**: Routes requests.
3.  **Core Service (FastAPI)**:
    -   `Properties Service`: CRUD for listings.
    -   `Market Service`: Analytics engine (ROI calculator).
    -   `AI Agent Service`: Chatbot logic and context management.
4.  **Database**: Stores structured property data and user history.

## Roadmap (Phase 1: MVP)
1.  **Environment Setup**:
    -   Initialize Git repo.
    -   Setup `frontend` (Next.js) folder.
    -   Setup `backend` (FastAPI) folder + venv.
2.  **Backend Core**:
    -   Define Pydantic models (Property, User).
    -   Create ROI calculation endpoint.
    -   Mock property data.
3.  **Frontend Core**:
    -   Mobile layout (bottom navigation).
    -   Property Feed (Card view).
    -   Chat Interface.
4.  **AI Integration**:
    -   Connect Chat UI to simple AI backend agent.
