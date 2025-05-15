![Camino Preview](logo.png)

---

# Pilgrim - The Ignatian Journey

**CaminoXR** is an immersive spiritual retreat experience built using **React (Vite)**, **A-Frame**, and **Django**. Inspired by the *Ignatian Spiritual Exercises*, it invites users to walk, jump, crouch, and reflect through interactive 3D meditations — structured as missions that unfold across retreat stages.

---

## 🌿 Project Vision

This project combines spirituality, gamified logic, and accessible WebXR to offer:
- A retreat-like journey, broken into **missions** and **meditations**
- Progressive unlocking of content based on user movement and interaction
- Smartphone-compatible controls (buttons for walk, jump, crouch)
- Bilingual support (English & Spanish) for meditations and UI

---

## 🔧 Tech Stack

### Frontend
- **Vite + React**
- **A-Frame** (WebXR scenes)
- **TailwindCSS** (UI styling)
- State management for user progression

### Backend
- **Django + PostgreSQL**
- **JWT Authentication** (djoser & simplejwt)
- Models for Users, Retreats, Missions, Meditations, Progress
- Multilingual field support

---

## 🧠 Architecture

```

camino/
├── backend/
│   └── camino/
│       ├── core/       # Missions, progress, meditations
│       └── users/      # JWT auth, user profile
├── frontend/
│   └── camino/
│       ├── assets/     # Models, icons, textures
│       ├── components/ # UI elements
│       ├── layouts/    # Scene & XR page layouts
│       ├── pages/      # Retreat scenes
│       ├── xr/         # XR interactions (walk, jump, crouch)
│       ├── logic/      # State & progression logic
│       └── main.jsx, App.jsx, vite.config.js
├── docs/
│   └── planning.md     # Flowcharts, ER diagrams, UX plan
└── README.md

````

---

## 🧭 Progression Logic

- Users begin on the **Pilgrim: The Ignatian Way** retreat
- Each of the 4 missions includes 5 meditations
- Completing a mission unlocks the next
- Progress is tracked in the backend via `UserProgress` and synced to frontend state

---

## 🎮 User Experience

- Walk, jump, crouch via keyboard or smartphone buttons
- Visual and audio cues guide meditative focus
- Scene transitions symbolize inner transformation
- Unlocking content reinforces spiritual journey milestones

---

## 📄 Documentation

Check the `docs/planning.md` for:
- Class & state diagrams
- Flowcharts for backend logic
- ERD (Entity Relationship Diagram)
- Mindmap of the meditation journey
- UX sketches & retreat logic

---

## 🚀 Running the Project

1. **Backend**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # or .\venv\Scripts\activate on Windows
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```

2. **Frontend**

   ```bash
   cd frontend/camino
   npm install
   npm run dev
   ```

---

