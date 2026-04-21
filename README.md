# 🧠 NutriMind AI – Smart Food &amp; Health Companion🚀 “NutriMind AI doesn’t just track your diet — it predicts your future health and helps you improve it.”## 🌟 OverviewNutriMind AI is a next-generation food and health application powered by a multi-agent AI system. It helps users make better food choices, track their health dynamically, and build sustainable eating habits using real-world nutrition data, contextual awareness, and predictive intelligence.## 🎯 Key Features🧠 Multi-Agent AI SystemNutrition ExpertHealth AnalyzerMeal PlannerGrocery PlannerHabit Coach🔮 Future Prediction Agent (Killer Feature)📊 Dynamic Health Score (0–100)📸 Food Image Scanner (AI-powered)🍽️ Personalized Meal Planning🛒 Smart Grocery List Generator🔁 Habit Tracking &amp; Streak System⚡ Context-Aware Recommendations (time, mood, activity)🔮 Future Health Simulator (What-if Engine)## 🏗️ Tech Stack### 🎨 Frontend⚛️ React (Vite)🎨 Tailwind CSS📊 Recharts (Data Visualization)### ⚙️ Backend🐍 FastAPI🔗 REST APIs (MCP-style tools)🗄️ SQLite (Persistent Storage)

          
            
          
        
  
        
    

🧠 AI / ML🤖 Google Gemini (via google-genai)📸 Gemini Vision (Image Analysis)### 🌐 APIs🥗 Edamam API🍎 USDA API (fallback)## 🏛️ ArchitectureFrontend (React + Tailwind)
        ↓
FastAPI Backend (API Layer)
        ↓
Multi-Agent System (Orchestrator)
        ↓
MCP Tools Layer (APIs &amp; Services)
        ↓
Database (SQLite)
### 📁 Project StructureNutriMind-AI/
│
├── frontend/              # React + Tailwind UI
│   ├── src/pages/
│   ├── src/components/
│   └── src/services/
│
├── backend/
│   ├── api/               # REST endpoints
│   ├── agents/            # AI agents
│   ├── tools/             # MCP tools
│   ├── database/          # SQLite models
│   ├── workflow.py        # Orchestrator
│   └── main.py            # FastAPI entry
│
└── README.md
## 🔁 Workflowgraph TD
A[User Input: Text/Image] --&gt; B[Food Recognition]
B --&gt; C[Nutrition Data Tool]
C --&gt; D[Health Analyzer Agent]
D --&gt; E[Context Awareness]
E --&gt; F[Recommendation Engine]
F --&gt; G[Meal Planner]
G --&gt; H[Grocery Planner]
H --&gt; I[Habit Coach]
I --&gt; J[Future Prediction Agent]
J --&gt; K[Final Response + UI]
## ⚙️ Setup Instructions

          
            
          
        
  
        
    

🔧 PrerequisitesNode.js (v18+)Python (3.9+)pip / virtualenv## 🖥️ Backend Setup (FastAPI)cd backend
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
### 📁 Create .env fileGEMINI_API_KEY=your_google_gemini_key
EDAMAM_APP_ID=your_edamam_id
EDAMAM_APP_KEY=your_edamam_key
### ▶️ Run backenduvicorn main:app --reload
## 🎨 Frontend Setup (React)cd frontend
npm install
npm run dev
## 🌐 Access AppFrontend: http://localhost:5173Backend: http://localhost:8000## 🧠 Multi-Agent SystemAgentResponsibility🥗 Nutrition ExpertAnalyze food &amp; suggest improvements📊 Health AnalyzerCompute health score🍽️ Meal PlannerGenerate personalized meals🛒 Grocery PlannerCreate shopping lists🧠 Habit CoachTrack habits &amp; give nudges🔮 Future PredictorSimulate future health## 🔧 MCP Tools/api/tools/nutrition → Fetch nutrition data/api/tools/meal-generation → Generate meal plans/api/tools/user-profile → Manage user data/api/tools/image-analysis → Food detection/api/tools/context → Capture user context## 🔮 Killer Feature: Future Health SimulatorPredicts how your current eating habits will impact your future health.📉 Shows declining/improving health trends⚠️ Detects risks (e.g., high sugar intake)✅ Provides “what-if” improvements## 🧪 Verification &amp; Testing

          
            
          
        
  
        
    

✅ AutomatedAPI endpoint validationHealth score unit tests### ✅ ManualUpload food image → full pipelineChat with AI assistantCheck database persistence## 🏆 Why This Project Stands Out🔥 Multi-Agent AI Architecture📊 Real Data + Context Awareness🔮 Predictive Intelligence (Future Simulation)🎨 Production-Level UI/UX🧠 Explainable AI Decisions## 🚀 Future EnhancementsWearable device integrationReal-time calorie trackingVoice-based assistantSocial &amp; community challenges## 🤝 ContributionPull requests are welcome! For major changes, please open an issue first.## 📜 LicenseMIT License## 🙌 AcknowledgementsGoogle (Gemini AI)EdamamUSDA# 🎯 Final Note💡 NutriMind AI transforms food tracking into intelligent health prediction — empowering users to make better decisions before it’s too late.
