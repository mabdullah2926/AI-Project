# 🔄 Autonomous E-commerce Returns Optimizer

<div align="center">

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.111+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-18+-61DAFB?style=for-the-badge&logo=react&logoColor=black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-Multi--Agent-FF6B6B?style=for-the-badge)
![Groq](https://img.shields.io/badge/Groq-AI%20Inference-F55036?style=for-the-badge)

![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active%20Development-brightgreen?style=flat-square)
![University](https://img.shields.io/badge/Project-Final%20Year%20AI-blueviolet?style=flat-square)

**A fully autonomous, multi-agent AI system that intelligently manages e-commerce product returns — from classification and fraud detection to smart routing, customer communication, and analytics.**

[Overview](#-overview) • [Features](#-key-features) • [Architecture](#-system-architecture) • [AI Agents](#-ai-agents) • [Installation](#-installation) • [API Docs](#-api-endpoints) • [Deployment](#-deployment)

</div>

---

## 📌 Overview

The **Autonomous E-commerce Returns Optimizer** is an AI-powered backend system built as a Final Year Project to solve one of the most operationally expensive challenges in online retail: **product returns management**.

Every year, e-commerce businesses lose billions in revenue due to inefficient return processes — slow approvals, missed fraud, poor routing, and customer dissatisfaction. This system deploys a **crew of five specialized AI agents** (powered by CrewAI and Groq LLMs) that collaborate autonomously to handle the entire return lifecycle end-to-end.

### What it does:

- Automatically **classifies** incoming return requests by reason, condition, and policy eligibility
- Detects **fraudulent** return patterns using behavioral and historical analysis
- **Routes** approved returns to the optimal resolution path (refund, replacement, store credit, or repair)
- Sends real-time **personalized communications** to customers via email and SMS
- Generates **business analytics** and actionable insights for merchants

The system integrates with **Shopify** for order data, **Stripe** for refund processing, **Resend** for emails, **Twilio** for SMS, and **Supabase/PostgreSQL** for persistence — forming a production-ready, plug-and-play returns infrastructure.

---

## ✨ Key Features

- 🤖 **Multi-Agent Orchestration** — Five CrewAI agents work in a sequential pipeline with shared context and memory
- 🔍 **Intelligent Classification** — LLM-based categorization of return reasons using Groq's ultra-fast inference
- 🛡️ **Fraud Detection** — Pattern analysis across customer history, return velocity, and order anomalies
- 🔀 **Smart Routing Engine** — Decision logic to select optimal resolution (refund, replace, store credit, repair)
- 📬 **Automated Customer Communication** — Personalized email + SMS notifications at every return stage
- 📊 **Real-time Analytics Dashboard** — Return trends, fraud rates, resolution metrics, and cost savings
- ⚡ **Async FastAPI Backend** — High-performance REST API with background task processing
- 🗄️ **Structured Database Layer** — PostgreSQL via Supabase with full audit trail
- 🔗 **Deep Shopify Integration** — Pulls live order and product data for context-aware decisions
- 💳 **Automated Refunds** — Stripe API integration for instant, programmatic payment reversals
- 🔒 **Secure by Design** — JWT authentication, rate limiting, and environment-based secret management
- 🚀 **Deployment Ready** — Configured for Vercel (frontend) + Render (backend)

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                        CLIENT LAYER                                      │
│                                                                         │
│   ┌──────────────────┐          ┌──────────────────────────────────┐   │
│   │   React Frontend  │          │     Shopify Webhook / Merchant    │   │
│   │   (Vercel CDN)    │          │          Dashboard               │   │
│   └────────┬─────────┘          └───────────────┬──────────────────┘   │
└────────────│───────────────────────────────────│────────────────────────┘
             │  HTTPS                             │  Webhook POST
             ▼                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        API GATEWAY LAYER                                 │
│                                                                         │
│              ┌──────────────────────────────────┐                      │
│              │     FastAPI Backend (Render)       │                      │
│              │  - JWT Auth Middleware             │                      │
│              │  - Rate Limiting                   │                      │
│              │  - Request Validation              │                      │
│              │  - Background Task Queue           │                      │
│              └──────────────┬───────────────────┘                      │
└─────────────────────────────│───────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    CREWAI MULTI-AGENT PIPELINE                          │
│                                                                         │
│   ┌─────────────┐   ┌─────────────┐   ┌─────────────┐                 │
│   │   Agent 1   │──▶│   Agent 2   │──▶│   Agent 3   │                 │
│   │Classification│   │    Fraud    │   │   Routing   │                 │
│   │   Agent     │   │    Agent    │   │    Agent    │                 │
│   └─────────────┘   └─────────────┘   └──────┬──────┘                 │
│                                               │                         │
│                              ┌────────────────▼──────────────┐         │
│                              │          Agent 4               │         │
│                              │    Communication Agent         │         │
│                              └────────────────┬──────────────┘         │
│                                               │                         │
│                              ┌────────────────▼──────────────┐         │
│                              │          Agent 5               │         │
│                              │      Analytics Agent           │         │
│                              └───────────────────────────────┘         │
│                                                                         │
│              All agents share: Groq LLM | Memory | Tools               │
└─────────────────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼────────────────────┐
            ▼                 ▼                    ▼
┌───────────────────┐  ┌──────────────┐   ┌───────────────────┐
│   EXTERNAL APIs   │  │   DATABASE   │   │  NOTIFICATION     │
│                   │  │              │   │  SERVICES         │
│  ┌─────────────┐  │  │  PostgreSQL  │   │                   │
│  │   Shopify   │  │  │  (Supabase)  │   │  ┌─────────────┐  │
│  │  Orders API │  │  │              │   │  │   Resend    │  │
│  └─────────────┘  │  │  - returns   │   │  │   Email     │  │
│  ┌─────────────┐  │  │  - customers │   │  └─────────────┘  │
│  │   Stripe    │  │  │  - analytics │   │  ┌─────────────┐  │
│  │  Refunds    │  │  │  - fraud_log │   │  │   Twilio    │  │
│  └─────────────┘  │  │              │   │  │    SMS      │  │
│  ┌─────────────┐  │  └──────────────┘   │  └─────────────┘  │
│  │  Groq LLM   │  │                     └───────────────────┘
│  │  Inference  │  │
│  └─────────────┘  │
└───────────────────┘
```

---

## 🤖 AI Agents

The system uses **CrewAI** to orchestrate five specialized agents. Each agent has a defined **role**, **goal**, **backstory**, and **tool set**, and they communicate through a shared crew context.

### 1. 🏷️ Classification Agent

**Role:** Return Request Classifier

**Goal:** Analyze incoming return requests and classify them by reason, product condition, policy eligibility, and urgency.

**How it works:**
The Classification Agent receives raw return request data (order ID, customer message, product metadata) and uses Groq's LLM to extract structured information. It determines the **return reason** (defective, wrong item, changed mind, sizing issue, etc.), assesses the **product condition** (new/opened/damaged), checks it against the merchant's **return policy window**, and assigns a **priority score**.

**Tools Used:**
- Shopify Orders API Tool — fetches order details, fulfillment date, and product info
- Policy Checker Tool — validates the request against configurable return window rules

**Output:** A structured `ClassificationResult` object passed to the Fraud Agent.

```python
# Example output
{
  "return_reason": "defective_product",
  "condition": "opened",
  "policy_eligible": True,
  "priority": "high",
  "confidence_score": 0.94
}
```

---

### 2. 🛡️ Fraud Detection Agent

**Role:** Return Fraud Investigator

**Goal:** Identify suspicious return patterns and flag potentially fraudulent requests before any refund or replacement is issued.

**How it works:**
The Fraud Agent receives the classification output alongside customer history data. It analyzes **return velocity** (how often the customer returns items), **pattern matching** (returns always claimed as defective near policy deadline, high-value item targeting), and **behavioral anomalies** (account age, first-time purchaser, mismatched shipping address). A fraud score between 0–100 is computed and a verdict is issued.

**Tools Used:**
- Customer History Tool — queries the PostgreSQL database for past return records
- Fraud Rules Engine Tool — applies configurable threshold-based rules
- Groq LLM — synthesizes unstructured signals into a holistic fraud assessment

**Output:** A `FraudAssessment` with a score, verdict (`approved` / `flagged` / `rejected`), and reasoning.

```python
# Example output
{
  "fraud_score": 72,
  "verdict": "flagged",
  "flags": ["high_return_velocity", "pattern_near_deadline"],
  "requires_manual_review": True
}
```

---

### 3. 🔀 Routing Agent

**Role:** Return Resolution Router

**Goal:** Determine the most optimal resolution path for each approved return — balancing customer satisfaction, business cost, and inventory impact.

**How it works:**
The Routing Agent receives the classification and fraud verdict. For approved cases, it weighs multiple factors: product resale value, restocking cost, customer lifetime value (CLV), warehouse inventory levels (via Shopify), and merchant preference settings. It then selects the best resolution:

| Resolution | Condition |
|---|---|
| **Full Refund** | High-CLV customer, valid defect, in policy window |
| **Replacement** | Defective item, stock available, customer prefers exchange |
| **Store Credit** | Changed mind returns, CLV-positive, incentivize retention |
| **Repair/Service** | High-value electronics, minor damage, cost-effective |
| **Manual Review** | Fraud-flagged, ambiguous condition, high order value |

**Tools Used:**
- Inventory Check Tool (Shopify) — checks replacement stock availability
- Customer Value Tool — fetches CLV and order history
- Cost Calculator Tool — estimates refund vs replacement vs store credit cost

**Output:** A `RoutingDecision` object with resolution type, justification, and next actions.

---

### 4. 📬 Communication Agent

**Role:** Customer Communication Specialist

**Goal:** Generate and dispatch personalized, empathetic, and on-brand customer communications at every stage of the return journey.

**How it works:**
The Communication Agent receives the routing decision and composes contextual messages. Using the Groq LLM with a persona-driven system prompt, it generates **email content** (via Resend) and **SMS updates** (via Twilio) that reflect the return outcome — whether it's an approval with refund ETA, a request for more information, a fraud-flag notice, or a replacement confirmation. Messages are dynamically tailored to customer tone and history.

**Tools Used:**
- Resend Email Tool — sends HTML/plain-text emails with tracking
- Twilio SMS Tool — sends short-form status updates
- Template Engine — merchant-customizable message templates

**Output:** Delivery receipts logged to the database; customer notified across channels.

```
📧 Email: "Hi Sarah, your return for Order #4521 has been approved.
           Your refund of $89.99 will appear within 3–5 business days."

📱 SMS:   "AERO STORE: Return #RT-882 approved! Refund of $89.99
           processing. Reply HELP for support."
```

---

### 5. 📊 Analytics Agent

**Role:** Returns Data Analyst

**Goal:** Continuously analyze return patterns, generate business insights, detect emerging trends, and produce actionable recommendations for merchants.

**How it works:**
The Analytics Agent runs after each return is processed. It aggregates return data from PostgreSQL, computes key metrics (return rate by SKU, fraud rate by region, resolution cost breakdown, agent decision accuracy), and identifies patterns. On a scheduled basis, it generates **weekly summary reports** and **alert notifications** when thresholds are breached (e.g., sudden spike in returns for a product SKU — possible quality issue).

**Tools Used:**
- Database Query Tool — aggregates returns, fraud, and resolution data
- Chart Data Formatter — prepares structured data for the React dashboard
- Report Generator — compiles Markdown/JSON summaries for merchant review

**Output:** Updated analytics records in PostgreSQL; dashboard data refreshed via API.

---

## 🛠️ Tech Stack

| Layer | Technology | Version | Purpose |
|---|---|---|---|
| **AI Orchestration** | CrewAI | 0.28+ | Multi-agent workflow management |
| **LLM Inference** | Groq (LLaMA 3) | Latest | Ultra-fast AI completions |
| **Backend** | FastAPI | 0.111+ | Async REST API framework |
| **Language** | Python | 3.11+ | Core backend language |
| **Frontend** | React | 18+ | Merchant dashboard UI |
| **Styling** | Tailwind CSS | 3.4+ | Utility-first CSS |
| **Database** | PostgreSQL | 15+ | Primary relational store |
| **BaaS** | Supabase | Latest | Managed Postgres + Auth |
| **Task Queue** | FastAPI BackgroundTasks | Built-in | Async agent execution |
| **Auth** | JWT (python-jose) | 3.3+ | API authentication |
| **Validation** | Pydantic | 2.x | Request/response schemas |
| **HTTP Client** | httpx | 0.27+ | Async API calls |
| **Deployment (FE)** | Vercel | Latest | Frontend hosting + CDN |
| **Deployment (BE)** | Render | Latest | Backend hosting |

---

## 🔌 APIs & Integrations

| API / Service | Purpose | Integration Point |
|---|---|---|
| **Groq AI** | LLM inference engine powering all 5 agents via LLaMA 3 70B | CrewAI LLM provider |
| **Shopify Admin API** | Fetch order data, product info, inventory levels, customer history | Classification & Routing Agents |
| **Stripe API** | Process refunds programmatically when resolution = full refund | Routing Agent + webhook |
| **Resend** | Send transactional HTML emails for return status updates | Communication Agent |
| **Twilio** | Send SMS notifications for real-time return updates | Communication Agent |
| **Supabase** | Managed PostgreSQL database + Row Level Security + REST API | All agents + FastAPI |

---

## 🗄️ Database Schema

All tables live in a **Supabase PostgreSQL** instance with Row Level Security (RLS) enabled.

### Table 1: `returns`

```sql
CREATE TABLE returns (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    order_id        VARCHAR(100) NOT NULL,
    customer_id     UUID NOT NULL REFERENCES customers(id),
    shopify_order_id VARCHAR(100),
    product_sku     VARCHAR(100) NOT NULL,
    product_name    VARCHAR(255) NOT NULL,
    return_reason   VARCHAR(100) NOT NULL,
    -- e.g. defective_product, wrong_item, changed_mind, sizing_issue
    condition       VARCHAR(50) NOT NULL,
    -- e.g. new, opened, damaged
    status          VARCHAR(50) NOT NULL DEFAULT 'pending',
    -- pending | approved | rejected | processing | completed | manual_review
    resolution      VARCHAR(50),
    -- refund | replacement | store_credit | repair | rejected
    priority        VARCHAR(20) DEFAULT 'normal',
    refund_amount   DECIMAL(10, 2),
    currency        CHAR(3) DEFAULT 'USD',
    policy_eligible BOOLEAN DEFAULT TRUE,
    agent_payload   JSONB,
    -- full CrewAI pipeline output stored for auditability
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at      TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    resolved_at     TIMESTAMPTZ
);

CREATE INDEX idx_returns_customer_id ON returns(customer_id);
CREATE INDEX idx_returns_status ON returns(status);
CREATE INDEX idx_returns_created_at ON returns(created_at);
```

---

### Table 2: `customers`

```sql
CREATE TABLE customers (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    shopify_customer_id VARCHAR(100) UNIQUE NOT NULL,
    email               VARCHAR(255) UNIQUE NOT NULL,
    phone               VARCHAR(30),
    full_name           VARCHAR(255),
    lifetime_value      DECIMAL(12, 2) DEFAULT 0.00,
    total_orders        INTEGER DEFAULT 0,
    total_returns       INTEGER DEFAULT 0,
    return_rate         DECIMAL(5, 4) DEFAULT 0.0000,
    -- Computed: total_returns / total_orders
    risk_tier           VARCHAR(20) DEFAULT 'standard',
    -- standard | elevated | high_risk | trusted
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_customers_email ON customers(email);
CREATE INDEX idx_customers_shopify_id ON customers(shopify_customer_id);
```

---

### Table 3: `fraud_log`

```sql
CREATE TABLE fraud_log (
    id              UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    return_id       UUID NOT NULL REFERENCES returns(id) ON DELETE CASCADE,
    customer_id     UUID NOT NULL REFERENCES customers(id),
    fraud_score     INTEGER NOT NULL CHECK (fraud_score BETWEEN 0 AND 100),
    verdict         VARCHAR(20) NOT NULL,
    -- approved | flagged | rejected
    flags           TEXT[],
    -- array of triggered rule names
    reasoning       TEXT,
    -- LLM-generated explanation
    requires_review BOOLEAN DEFAULT FALSE,
    reviewed_by     VARCHAR(100),
    reviewed_at     TIMESTAMPTZ,
    review_outcome  VARCHAR(20),
    created_at      TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_fraud_log_return_id ON fraud_log(return_id);
CREATE INDEX idx_fraud_log_verdict ON fraud_log(verdict);
CREATE INDEX idx_fraud_log_fraud_score ON fraud_log(fraud_score DESC);
```

---

### Table 4: `analytics`

```sql
CREATE TABLE analytics (
    id                  UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    period_start        DATE NOT NULL,
    period_end          DATE NOT NULL,
    period_type         VARCHAR(20) DEFAULT 'daily',
    -- daily | weekly | monthly
    total_returns       INTEGER DEFAULT 0,
    approved_returns    INTEGER DEFAULT 0,
    rejected_returns    INTEGER DEFAULT 0,
    fraud_flagged       INTEGER DEFAULT 0,
    fraud_rejected      INTEGER DEFAULT 0,
    refund_count        INTEGER DEFAULT 0,
    replacement_count   INTEGER DEFAULT 0,
    store_credit_count  INTEGER DEFAULT 0,
    manual_review_count INTEGER DEFAULT 0,
    total_refund_value  DECIMAL(14, 2) DEFAULT 0.00,
    avg_processing_time INTERVAL,
    top_return_reasons  JSONB,
    -- {"defective_product": 45, "wrong_item": 12, ...}
    top_return_skus     JSONB,
    -- {"SKU-001": 8, "SKU-045": 5, ...}
    fraud_rate          DECIMAL(5, 4),
    approval_rate       DECIMAL(5, 4),
    created_at          TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE UNIQUE INDEX idx_analytics_period ON analytics(period_start, period_end, period_type);
```

---

## 📁 Folder Structure

```
autonomous-returns-optimizer/
│
├── 📁 backend/                          # FastAPI Python backend
│   ├── 📁 agents/                       # CrewAI agent definitions
│   │   ├── __init__.py
│   │   ├── classification_agent.py      # Agent 1: Return classifier
│   │   ├── fraud_agent.py               # Agent 2: Fraud detector
│   │   ├── routing_agent.py             # Agent 3: Resolution router
│   │   ├── communication_agent.py       # Agent 4: Customer comms
│   │   ├── analytics_agent.py           # Agent 5: Data analyst
│   │   └── crew.py                      # CrewAI crew orchestrator
│   │
│   ├── 📁 api/                          # FastAPI route handlers
│   │   ├── __init__.py
│   │   ├── routes/
│   │   │   ├── returns.py               # POST /returns, GET /returns/{id}
│   │   │   ├── analytics.py             # GET /analytics/*
│   │   │   ├── webhooks.py              # POST /webhooks/shopify
│   │   │   └── auth.py                  # POST /auth/token
│   │   └── dependencies.py              # JWT auth, DB session deps
│   │
│   ├── 📁 core/                         # App configuration & setup
│   │   ├── config.py                    # Pydantic Settings (env vars)
│   │   ├── database.py                  # SQLAlchemy async engine
│   │   ├── security.py                  # JWT token utilities
│   │   └── logging.py                   # Structured logging setup
│   │
│   ├── 📁 models/                       # SQLAlchemy ORM models
│   │   ├── return_model.py
│   │   ├── customer_model.py
│   │   ├── fraud_log_model.py
│   │   └── analytics_model.py
│   │
│   ├── 📁 schemas/                      # Pydantic request/response schemas
│   │   ├── return_schema.py
│   │   ├── customer_schema.py
│   │   └── analytics_schema.py
│   │
│   ├── 📁 services/                     # Business logic & external APIs
│   │   ├── shopify_service.py           # Shopify Admin API client
│   │   ├── stripe_service.py            # Stripe refund processing
│   │   ├── resend_service.py            # Resend email sender
│   │   ├── twilio_service.py            # Twilio SMS sender
│   │   └── supabase_service.py          # Supabase direct client
│   │
│   ├── 📁 tools/                        # CrewAI custom tools
│   │   ├── shopify_tool.py
│   │   ├── stripe_tool.py
│   │   ├── database_tool.py
│   │   └── policy_tool.py
│   │
│   ├── 📁 migrations/                   # Alembic DB migrations
│   │   └── versions/
│   │
│   ├── main.py                          # FastAPI app entrypoint
│   ├── requirements.txt
│   └── Dockerfile
│
├── 📁 frontend/                         # React merchant dashboard
│   ├── 📁 src/
│   │   ├── 📁 components/
│   │   │   ├── Dashboard.jsx
│   │   │   ├── ReturnsList.jsx
│   │   │   ├── ReturnDetail.jsx
│   │   │   ├── AnalyticsChart.jsx
│   │   │   ├── FraudAlerts.jsx
│   │   │   └── AgentStatus.jsx
│   │   ├── 📁 pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Returns.jsx
│   │   │   ├── Analytics.jsx
│   │   │   └── Settings.jsx
│   │   ├── 📁 hooks/
│   │   │   └── useReturns.js
│   │   ├── 📁 services/
│   │   │   └── api.js                   # Axios API client
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
│   ├── tailwind.config.js
│   └── vite.config.js
│
├── 📁 docs/                             # Project documentation
│   ├── architecture.md
│   ├── agent-specs.md
│   └── api-reference.md
│
├── .env.example                         # Environment variable template
├── .gitignore
├── docker-compose.yml                   # Local dev environment
└── README.md
```

---

## ⚙️ Installation

### Prerequisites

Ensure the following are installed on your machine:

| Tool | Version | Check |
|---|---|---|
| Python | 3.11+ | `python --version` |
| Node.js | 18+ | `node --version` |
| npm | 9+ | `npm --version` |
| PostgreSQL | 15+ | `psql --version` |
| Git | Any | `git --version` |

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/yourusername/autonomous-returns-optimizer.git
cd autonomous-returns-optimizer
```

---

### Step 2 — Set Up Python Virtual Environment

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate (macOS/Linux)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate
```

---

### Step 3 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`:**

```txt
fastapi==0.111.0
uvicorn[standard]==0.29.0
crewai==0.28.0
groq==0.8.0
langchain-groq==0.1.6
sqlalchemy[asyncio]==2.0.30
asyncpg==0.29.0
alembic==1.13.1
pydantic==2.7.4
pydantic-settings==2.3.1
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
httpx==0.27.0
shopifyapi==12.6.0
stripe==9.9.0
resend==2.0.0
twilio==9.2.3
supabase==2.4.5
python-dotenv==1.0.1
python-multipart==0.0.9
```

---

### Step 4 — Install Frontend Dependencies

```bash
# From the project root
cd frontend
npm install
```

---

### Step 5 — Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env

# Open and fill in all values
nano .env   # or use VS Code: code .env
```

See the [Environment Variables](#-environment-variables) section for all required values.

---

### Step 6 — Set Up the Database

```bash
# From the backend directory with venv active
cd backend

# Run Alembic migrations to create all tables
alembic upgrade head
```

If using **Supabase**, paste the SQL from `docs/schema.sql` directly into the Supabase SQL Editor and execute.

---

### Step 7 — Verify Setup

```bash
# Backend check
cd backend
python -c "from core.config import settings; print('✅ Config loaded:', settings.app_name)"

# Frontend check
cd ../frontend
npm run build  # Should complete without errors
```

---

## 🔐 Environment Variables

Create a `.env` file in the `backend/` directory with the following variables:

```env
# ─────────────────────────────────────────────
# APPLICATION
# ─────────────────────────────────────────────
APP_NAME="Autonomous Returns Optimizer"
APP_ENV=development                        # development | production
DEBUG=True
SECRET_KEY=your-super-secret-jwt-key-here  # Generate: openssl rand -hex 32
ALLOWED_ORIGINS=http://localhost:5173,https://your-frontend.vercel.app

# ─────────────────────────────────────────────
# DATABASE (Supabase / PostgreSQL)
# ─────────────────────────────────────────────
DATABASE_URL=postgresql+asyncpg://postgres:[password]@db.[project-ref].supabase.co:5432/postgres
SUPABASE_URL=https://[project-ref].supabase.co
SUPABASE_ANON_KEY=your-supabase-anon-key
SUPABASE_SERVICE_ROLE_KEY=your-supabase-service-role-key

# ─────────────────────────────────────────────
# GROQ AI
# ─────────────────────────────────────────────
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
GROQ_MODEL=llama3-70b-8192                 # Recommended model

# ─────────────────────────────────────────────
# SHOPIFY
# ─────────────────────────────────────────────
SHOPIFY_SHOP_URL=your-store.myshopify.com
SHOPIFY_ACCESS_TOKEN=shpat_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
SHOPIFY_WEBHOOK_SECRET=your-webhook-secret

# ─────────────────────────────────────────────
# STRIPE
# ─────────────────────────────────────────────
STRIPE_SECRET_KEY=sk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
STRIPE_WEBHOOK_SECRET=whsec_xxxxxxxxxxxxxxxxxxxxxxxxxxxx
STRIPE_PUBLISHABLE_KEY=pk_test_xxxxxxxxxxxxxxxxxxxxxxxxxxxx

# ─────────────────────────────────────────────
# RESEND (Email)
# ─────────────────────────────────────────────
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
RESEND_FROM_EMAIL=returns@yourdomain.com
RESEND_FROM_NAME="Returns Team"

# ─────────────────────────────────────────────
# TWILIO (SMS)
# ─────────────────────────────────────────────
TWILIO_ACCOUNT_SID=ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
TWILIO_AUTH_TOKEN=your-twilio-auth-token
TWILIO_PHONE_NUMBER=+1234567890

# ─────────────────────────────────────────────
# RETURN POLICY SETTINGS
# ─────────────────────────────────────────────
RETURN_WINDOW_DAYS=30
FRAUD_SCORE_THRESHOLD=65                   # Score >= this triggers review
AUTO_APPROVE_THRESHOLD=25                  # Score <= this auto-approves
```

> ⚠️ **Never commit your `.env` file to Git.** It is already included in `.gitignore`.

---

## 🚀 How to Run Locally

### Start the Backend (FastAPI)

```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate

uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at:
- **API Base:** `http://localhost:8000`
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

### Start the Frontend (React)

```bash
cd frontend
npm run dev
```

The dashboard will be available at `http://localhost:5173`

---

### Start with Docker Compose (Recommended)

```bash
# From the project root
docker-compose up --build
```

**`docker-compose.yml`:**

```yaml
version: '3.9'

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"
    env_file:
      - ./backend/.env
    depends_on:
      - db
    volumes:
      - ./backend:/app

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
    environment:
      - VITE_API_URL=http://localhost:8000

  db:
    image: postgres:15
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
      POSTGRES_DB: returns_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

---

## 📡 API Endpoints

### Base URL
- **Local:** `http://localhost:8000/api/v1`
- **Production:** `https://your-backend.onrender.com/api/v1`

---

### Authentication

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/auth/token` | Get JWT access token |

```bash
curl -X POST http://localhost:8000/api/v1/auth/token \
  -H "Content-Type: application/json" \
  -d '{"username": "admin", "password": "yourpassword"}'
```

---

### Returns

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/returns` | Submit a new return request — triggers the full agent pipeline |
| `GET` | `/returns` | List all returns (paginated, filterable) |
| `GET` | `/returns/{return_id}` | Get full details of a specific return |
| `PATCH` | `/returns/{return_id}/status` | Manually update a return status |
| `GET` | `/returns/{return_id}/audit` | Full agent decision audit trail |

**Example: Submit Return Request**

```bash
curl -X POST http://localhost:8000/api/v1/returns \
  -H "Authorization: Bearer <your_jwt_token>" \
  -H "Content-Type: application/json" \
  -d '{
    "order_id": "ORD-10045",
    "shopify_order_id": "5678901234",
    "customer_email": "sarah@example.com",
    "product_sku": "SHOE-NKE-42-BLK",
    "return_reason": "The shoes have a visible stitching defect on the left sole.",
    "customer_message": "I noticed the issue after wearing them once."
  }'
```

**Example Response:**

```json
{
  "return_id": "3f9a2d1e-bc44-4a1e-b5f2-9c7e3a4d2f01",
  "status": "processing",
  "message": "Return request received. AI agents are processing your request.",
  "estimated_completion": "2–3 minutes"
}
```

---

### Analytics

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/analytics/summary` | Overall returns summary metrics |
| `GET` | `/analytics/daily` | Daily return volume & resolution breakdown |
| `GET` | `/analytics/fraud` | Fraud statistics and flagged patterns |
| `GET` | `/analytics/top-skus` | Products with highest return rates |
| `GET` | `/analytics/agents` | Per-agent performance metrics |

---

### Webhooks

| Method | Endpoint | Description |
|---|---|---|
| `POST` | `/webhooks/shopify` | Shopify order/refund event webhook |
| `POST` | `/webhooks/stripe` | Stripe refund completion webhook |

---

## 🌐 Deployment

### Frontend — Vercel

**Step 1:** Push your code to GitHub.

**Step 2:** Visit [vercel.com](https://vercel.com) → **New Project** → Import your GitHub repository.

**Step 3:** Configure build settings:

```
Framework Preset: Vite
Root Directory:   frontend/
Build Command:    npm run build
Output Directory: dist
```

**Step 4:** Add Environment Variables in the Vercel dashboard:

```
VITE_API_URL = https://your-backend.onrender.com/api/v1
```

**Step 5:** Click **Deploy**. Vercel handles CDN, HTTPS, and CI/CD automatically.

---

### Backend — Render

**Step 1:** Visit [render.com](https://render.com) → **New Web Service** → Connect your GitHub repo.

**Step 2:** Configure the service:

```
Name:             returns-optimizer-api
Root Directory:   backend/
Runtime:          Python 3
Build Command:    pip install -r requirements.txt
Start Command:    uvicorn main:app --host 0.0.0.0 --port $PORT
```

**Step 3:** Add all environment variables from your `.env` file under **Environment → Add Environment Variable**.

**Step 4:** Click **Create Web Service**. Render will deploy and provide a public URL.

**Step 5:** Set your Shopify and Stripe webhook URLs to your Render service URL:

```
Shopify Webhook:  https://your-service.onrender.com/api/v1/webhooks/shopify
Stripe Webhook:   https://your-service.onrender.com/api/v1/webhooks/stripe
```

---

### Database — Supabase

**Step 1:** Create a free project at [supabase.com](https://supabase.com).

**Step 2:** Navigate to **SQL Editor** and run the schema from `docs/schema.sql`.

**Step 3:** Copy the **Project URL** and **anon/service_role keys** from **Settings → API** into your environment variables.

**Step 4:** Enable Row Level Security (RLS) on all tables and configure policies as needed.

---

## 🔮 Future Improvements

- [ ] **Voice Return Initiation** — Allow customers to initiate returns via phone call using Twilio Voice + Whisper speech-to-text
- [ ] **Image-Based Condition Assessment** — Use a vision LLM (GPT-4o or LLaMA Vision) to automatically assess product condition from customer-uploaded photos
- [ ] **Predictive Return Forecasting** — Time-series ML model to predict return surges by SKU, enabling proactive inventory planning
- [ ] **Multi-Merchant SaaS Mode** — Tenant isolation, per-merchant policy configuration, and white-label dashboard
- [ ] **LangGraph Migration** — Replace CrewAI with LangGraph for finer-grained stateful agent control and branching workflows
- [ ] **A/B Testing for Communication Templates** — Test different message tones and formats to optimize customer satisfaction scores
- [ ] **Real-Time WebSocket Updates** — Push live return status updates to the dashboard without polling
- [ ] **Return Abuse Blacklist** — Maintain a cross-merchant shared fraud signal database (with consent and privacy compliance)
- [ ] **Carbon Footprint Calculator** — Estimate and display the environmental impact of return shipments; suggest greener alternatives
- [ ] **Mobile App** — React Native companion app for merchants to manage returns on-the-go
- [ ] **Multi-Language Support** — i18n for customer communications in the customer's preferred language

---

## 👤 Author

**[Your Full Name]**
Final Year BSc Computer Science / Artificial Intelligence
[Your University Name] — Class of [Year]

- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
- Email: your.email@university.edu

> *This project was developed as a Final Year Project in partial fulfillment of the requirements for the degree of Bachelor of Science in Computer Science / Artificial Intelligence.*

---

## 🙏 Acknowledgements

- [CrewAI](https://github.com/joaomdmoura/crewAI) — for the multi-agent orchestration framework
- [Groq](https://groq.com) — for the blazing-fast LLM inference API
- [FastAPI](https://fastapi.tiangolo.com) — for the elegant async Python API framework
- [Supabase](https://supabase.com) — for the open-source Firebase alternative
- My project supervisor, **[Supervisor Name]**, for guidance and feedback

---

## 📄 License

```
MIT License

Copyright (c) 2025 [Your Full Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
```

---

<div align="center">

Made with ❤️ and lots of ☕ for a Final Year AI Project

⭐ Star this repo if you found it useful!

</div>
