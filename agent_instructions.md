# Property Lens - AI Agent Instructions

## 1. Project Context
**Property Lens** is an AI-first real estate platform for Dubai.
- **Goal**: Help investors find liquid properties (Buy/Rent) with AI analysis.
- **Platform**: Web (PWA) Mobile-First.
- **Key Features**: AI Chat Consultant, ROI Calculator, Market Analytics.

## 2. Technology Stack

### Frontend
- **Framework**: **Next.js** (App Router).
- **Language**: **TypeScript**.
- **Styling**: 
    - **Primary**: **CSS Modules** (`*.module.css`) for custom designs.
    - **Secondary**: Tailwind CSS (Use ONLY if explicitly requested by the user).
- **State**: React Context / Hooks.
- **Data Fetching**: SWR or TanStack Query.

### Backend
- **Framework**: **FastAPI** (Python 3.10+).
- **ORM**: **SQLAlchemy** (Async).
- **Database**: **PostgreSQL 15+** (with `pgvector` for AI embeddings).
- **Validation**: Pydantic v2.
- **AI Integration**: OpenAI API (GPT-4), LangChain.

## 3. Architecture Overview

### Structure
1.  **Client (Next.js)**: Handles UI, User Interaction, and Chat Interface.
2.  **API Gateway (Nginx/FastAPI)**: Routes requests.
3.  **Core Service (FastAPI)**:
    -   `Properties Service`: CRUD for listings.
    -   `Market Service`: Analytics engine (ROI calculator).
    -   `AI Agent Service`: Chatbot logic and context management.
4.  **Database**: Stores structured property data and user history.

### Frontend Structure
```text
frontend/
  app/              # Next.js App Router pages
    (features)/     # Feature-based routing
  components/
    ui/             # Reusable UI components
    features/       # Feature-specific components
  lib/              # Utilities, hooks, API clients
  styles/           # Global styles, CSS modules
  types/            # TypeScript types
  __tests__/        # Test files
```

### Backend Structure
```text
backend/
  app/
    api/            # Route handlers
    core/           # Config, security, exceptions
    models/         # SQLAlchemy DB models
    schemas/        # Pydantic schemas (Request/Response)
    services/       # Business logic
    tests/          # Pytest tests
```

## 4. Development Methodology

### Core Principles
1.  **SOLID**: Adhere to SOLID principles for robust design.
2.  **DRY (Don't Repeat Yourself)**.
3.  **KISS (Keep It Simple, Stupid)**.
4.  **YAGNI (You Aren't Gonna Need It)**.

### Process: Feature Driven Development (FDD)
1.  **Model**: Understand the domain.
2.  **Feature List**: Break down requirements.
3.  **Plan**: Select features.
4.  **Design**: Create technical design.
5.  **Build**: Implement using TDD.

## 5. Security & Performance

### Security
-   **Authentication**: JWT tokens (15min access, 7day refresh in httpOnly cookies).
-   **Validation**: Server-side Pydantic validation is mandatory. Sanitize all inputs.
-   **Rate Limiting**: 100 req/min per IP.
-   **Secrets**: Never commit `.env`. Use `.env.example`.

### Performance
-   **Frontend**: 
    -   LCP < 2.5s, FID < 100ms.
    -   Code splitting per route.
    -   Next/Image for all images.
-   **Backend**: 
    -   Response time < 200ms (GET), < 500ms (POST).
    -   Prevent N+1 queries in SQLAlchemy (use `selectinload`).
    -   Cache frequent data (Redis in future).

## 6. Coding Standards
-   **Naming**: PascalCase for React components, snake_case for Python.
-   **Comments**: Explain WHY, not WHAT. Docstrings for public methods.
-   **Typing**: Strict TypeScript (`noImplicitAny`) and Python Type Hints.
-   **Async**: All I/O must be async/await.

## 7. Testing Strategy
**TDD is MANDATORY.**
-   **Coverage**: Target 80% for critical paths.
-   **Frontend**: Jest + React Testing Library. Test user interactions (`screen.getByRole`).
-   **Backend**: Pytest + pytest-asyncio. Use fixtures for DB. Mock external APIs (OpenAI).

## 8. Error Handling
-   **Frontend**: Toast notifications for user errors. Error Boundaries for crashes.
-   **Backend**: 
    -   Use standard HTTP codes (400, 401, 404, 500).
    -   JSON Format: `{"detail": "Message", "error_code": "CODE", "timestamp": "..."}`.

## 9. AI Integration Guidelines
-   **Chat**: Use OpenAI GPT-4.
-   **Context**: Limit history (max 10 msgs). Inject property data into system prompt.
-   **Fallback**: Handle API failures gracefully.
-   **Cost**: Monitor token usage.

## 10. Documentation Standards
-   **Code**: Docstrings for all complex logic.
-   **API**: Ensure FastAPI Swagger (OpenAPI) description is populated via Pydantic.
-   **Modules**: `README.md` in major folders.

## 11. Git & Deployment
-   **Environment Variables**:
    ```env
    # Frontend
    NEXT_PUBLIC_API_URL=http://localhost:8000
    # Backend
    DATABASE_URL=postgresql+asyncpg://user:pass@localhost/db
    OPENAI_API_KEY=sk-...
    ```
-   **Verification**:
    -   **Backend**: `curl` check.
    -   **Frontend**: Browser check/screenshot.
    -   **Automated**: Test suite pass.
-   **Safety**: Never delete data without confirmation.

## 12. Workflow Constraints
1.  **Safety**: Never delete user data/config without confirmation.
2.  **Incremental**: Small, verified steps.
3.  **Verification**: Always verify (Test -> Curl/Browser -> Commit).
