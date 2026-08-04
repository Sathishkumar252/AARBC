
### Autonomous AI Agent for Reducing Case Backlogs in Indian Courts

**Theme:** AUTONOMOUS AI AGENTS FOR REAL-WORLD IMPACT  
**Team:** APEX ZENITH

---

## 🚀 Quick Start

```bash
# 1. Clone and enter directory
cd docketclear

# 2. Start all services
docker-compose up --build

# 3. Access the app
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

## 🏗️ Architecture

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Frontend** | React + Tailwind + Vite | Judicial dashboard for judges/clerks |
| **Backend** | FastAPI + PostgreSQL | REST API, RBAC, case management |
| **AI Agent** | Python + LLM + Rules Engine | Detect, Draft, Schedule, Prioritize |
| **Queue** | Celery + Redis | Async OCR, batch analysis |
| **Storage** | MinIO | Document storage |
| **Data** | eCourts API + NJDG | Live case data ingestion |

## 🤖 AI Capabilities

1. **DETECT** — Identifies delayed cases using filing dates, adjournments, custody status
2. **DRAFT** — Auto-generates case summaries and legal recommendations
3. **SCHEDULE** — Recommends optimal hearing dates based on priority and court load
4. **PRIORITIZE** — Scores cases 0-100; flags statutory limit breaches (CrPC/BNSS)

## 🔐 Human-in-the-Loop

Every AI recommendation requires judicial approval:
- ✅ Approve | ✏️ Edit | ❌ Reject | 🔄 Override

## 🧪 Running Tests

```bash
cd backend
pytest tests/ -v
```

## 📊 Key Features for Hackathon Demo

- **Shadow Mode** support: AI recommends without auto-acting
- **Statutory Compliance**: CrPC 167, 309 / BNSS 187, 258 rules engine
- **Undertrial Protection**: Auto-alerts when detention exceeds 90 days
- **OCR Pipeline**: Extracts text from scanned case files
- **Role-Based Access**: Judge, Clerk, Registrar, Admin
- **Real-time Analytics**: Backlog trends, clearance rates

## 📁 Project Structure

```
docketclear/
├── backend/              # FastAPI backend
│   ├── app/
│   │   ├── api/v1/       # REST API routes
│   │   ├── core/         # Config, security, Celery
│   │   ├── models/       # SQLAlchemy models
│   │   ├── schemas/      # Pydantic schemas
│   │   ├── services/     # AI Agent, Scheduler
│   │   ├── utils/        # OCR, helpers
│   │   └── tasks/        # Celery background jobs
│   ├── tests/            # Pytest suite
│   ├── alembic/          # DB migrations
│   ├── Dockerfile
│   └── requirements.txt
├── frontend/             # React + Vite + Tailwind
│   ├── src/
│   │   ├── components/   # Layout, ProtectedRoute
│   │   ├── context/      # AuthContext
│   │   ├── pages/        # Dashboard, Cases, etc.
│   │   ├── App.tsx
│   │   └── main.tsx
│   ├── Dockerfile
│   └── package.json
├── ai_agent/             # Standalone AI agent core
│   ├── core/             # Agent, Reasoning Engine
│   ├── rules/            # CrPC/BNSS rules
│   ├── prompts/          # LLM prompts
│   └── pipelines/        # Batch processing
├── docker-compose.yml
└── README.md
```
