# Property Lens

**AI-first Real Estate Platform for Dubai**

Property Lens is a modern web application designed to bring transparency and AI-driven insights to the Dubai real estate market. It features a Next.js frontend (PWA) and a Python FastAPI backend, integrated with OpenAI for intelligent property analysis.

## 🚀 Features

-   **AI Property Analysis**: Calculate ROI, Cash Flow, and generate investment summaries using GPT-4.
-   **Smart Search**: Semantic search powered by `pgvector` and OpenAI embeddings.
-   **Interactive Maps**: Visualize properties and market trends.
-   **Mobile-First Design**: Fully responsive PWA built with Next.js.
-   **Financial Metrics**: Transparent breakdown of costs, fees, and potential returns.

## 🛠 Technology Stack

-   **Frontend**: Next.js 15 (App Router), TypeScript, CSS Modules (features React Server Components).
-   **Backend**: Python 3.12, FastAPI, SQLAlchemy (Async), Pydantic.
-   **Database**: PostgreSQL 16 + `pgvector` extension.
-   **AI/ML**: OpenAI API (GPT-4, Embeddings).
-   **Infrastructure**: Docker, Docker Compose.

## 📋 Prerequisites

-   **Docker** & **Docker Compose** (Recommended)
-   *OR* Node.js v20+ and Python 3.12+ (for local development)

## 🏁 Getting Started

### Option 1: Docker (Recommended)

1.  **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd property_lens
    ```

2.  **Environment Setup**:
    Copy the example environment file for the backend:
    ```bash
    cp backend/.env.example backend/.env
    ```
    *Edit `backend/.env` and add your `OPENAI_API_KEY`.*

3.  **Run with Docker Compose**:
    ```bash
    docker-compose up --build
    ```
    
4.  **Access the App**:
    -   Frontend: [http://localhost:3000](http://localhost:3000)
    -   Backend API Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Option 2: Local Development

#### Database
You must have PostgreSQL installed or run it via Docker:
```bash
docker-compose up -d db
```

#### Backend (FastAPI)
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
alembic upgrade head      # Apply DB migrations
uvicorn app.main:app --reload
```

#### Frontend (Next.js)
```bash
cd frontend
npm install
npm run dev
```

## 📂 Project Structure

```
property_lens/
├── backend/                # FastAPI Application
│   ├── alembic/            # Database Migrations
│   ├── app/
│   │   ├── api/            # API Route Handlers
│   │   ├── core/           # Config & Database setup
│   │   ├── models/         # SQLAlchemy Models
│   │   ├── schemas/        # Pydantic Schemas
│   │   └── services/       # Business Logic
│   ├── requirements.txt
│   └── Dockerfile
│
├── frontend/               # Next.js Application
│   ├── app/                # App Router Pages
│   ├── components/         # React Components
│   ├── public/             # Static Assets
│   └── Dockerfile
│
├── docs/                   # Documentation
│   ├── technical_plan.md
│   └── business_plan.md
├── agent_instructions.md   # AI Agent Guidelines
└── docker-compose.yml      # Docker Orchestration
```

## 🤝 Contribution

Please verify all changes before pushing.
-   **Frontend**: Run `npm run build` to check for type errors.
-   **Backend**: Standardize with `flake8` or `black` (if configured).
-   **Commits**: Use Conventional Commits (e.g., `feat: login page`, `fix: api error`).

## 📄 License

Proprietary / Private.
