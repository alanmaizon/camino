# Database Design

```mermaid
erDiagram
    USERS {
        int id PK
        string username
        string email
        string password
        boolean is_active
        datetime created_at
        datetime updated_at
    }

    RETREATS {
        int id PK
        string name
        string description
        datetime start_date
        datetime end_date
    }

    MISSIONS {
        int id PK
        string name
        text description
        int retreat_id FK
        int order
    }

    MEDITATIONS {
        int id PK
        string name
        string description
        int mission_id FK
        string audio_url
        boolean is_locked
    }

    USERS ||--o| MISSIONS : completed
    MISSIONS ||--o| MEDITATIONS : includes
    USERS ||--o| RETREATS : participates
```

---

# Class Diagram

```mermaid
classDiagram
    class User {
        +int id
        +string username
        +string email
        +string password
        +DateTime created_at
        +DateTime updated_at
        +authenticate()
        +getProgress()
    }

    class Retreat {
        +int id
        +string name
        +string description
        +Date start_date
        +Date end_date
        +List~Mission~ missions
    }

    class Mission {
        +int id
        +string name
        +string description
        +int order
        +bool is_completed
        +List~Meditation~ meditations
        +complete()
    }

    class Meditation {
        +int id
        +string name
        +string description
        +string audio_url
        +bool is_locked
        +play()
        +unlock()
    }

    class UserMissionProgress {
        +int id
        +User user
        +Mission mission
        +bool completed
        +DateTime timestamp
    }

    User --> UserMissionProgress
    Mission --> Meditation
    Retreat --> Mission
    UserMissionProgress --> Mission
```

---

# State Diagram

### User Journey Through Retreats

```mermaid
stateDiagram-v2
    [*] --> LoggedOut
    LoggedOut --> LoggingIn
    LoggingIn --> Authenticated : Valid credentials
    LoggingIn --> LoggedOut : Failed login

    Authenticated --> InRetreatLobby
    InRetreatLobby --> ExploringMission
    ExploringMission --> ListeningToMeditation : Meditation unlocked
    ListeningToMeditation --> MissionCompleted
    MissionCompleted --> UnlockNextRetreat : All missions in retreat complete
    UnlockNextRetreat --> InRetreatLobby : Next retreat starts

    InRetreatLobby --> LoggedOut : User logs out
    ListeningToMeditation --> LoggedOut : User logs out
```

---

# Mind Map

### Conceptual Breakdown

```mermaid
mindmap
    root((CaminoXR))
        UserExperience(User Experience)
            Walk(Walk / Jump / Crouch)
            XRControls(XR Controls: touch + headset)
            Accessibility(Accessibility: bilingual, sound)
        Unlocking Progression(Unlocking Progression)
            Week1(Retreat 1: Awareness + Sin)
            Week2(Retreat 2: Life of Christ)
            Week3(Retreat 3: Passion)
            Week4(Retreat 4: Resurrection + Mission)
        GameplayElements(Gameplay Elements)
            Missions(Missions & Meditations)
                Audio(Audio)
                Symbols(Interactive symbols)
            Milestones(Milestones / Badges)
            Journal(Personal journal: optional)
        TechnologyStack(Technology Stack)
            Frontend(Frontend: React + Vite)
            XR(XR: WebXR + Three.js)
            Backend(Backend: Django + DRF)
            Database(Database: PostgreSQL)
        DevOpsHosting(DevOps / Hosting)
            CICD(CI/CD: GitHub Actions)
            Hosting(Hosting: Render)
            Testing(Testing: Jest + Pytest)
```

---

# Backend Logic

### 📊 **1. User Progress Tracking Flow**

```mermaid
flowchart TD
    A[User completes a meditation] --> B[Send completion request to backend]
    B --> C[Check if meditation already marked complete]
    C -- Yes --> D[Ignore / Return already completed]
    C -- No --> E[Mark meditation as completed in DB]
    E --> F[Check if all meditations in the mission are completed]
    F -- Yes --> G[Mark mission as completed for user]
    G --> H[Check if all missions in retreat completed]
    H -- Yes --> I[Unlock next retreat]
    H -- No --> J[Return success response]
    F -- No --> J
```

---

### 🧩 **2. Unlock Meditation Logic**

```mermaid
flowchart TD
    A[User requests meditation] --> B[Check if meditation is locked]
    B -- Yes --> C[Check if prerequisite meditation completed]
    C -- No --> D[Return error: Meditation Locked]
    C -- Yes --> E[Unlock meditation for user]
    E --> F[Return meditation data: audio URL, text]
    B -- No --> F
```

---

### 🗂️ **3. Save Mission Completion State**

```mermaid
flowchart TD
    A[User completes all meditations in mission] --> B[Request to mark mission complete]
    B --> C[Validate JWT/auth token]
    C -- Invalid --> D[Return 403 unauthorized]
    C -- Valid --> E[Check mission exists and belongs to retreat]
    E -- Not valid --> F[Return 404]
    E -- Valid --> G[Create or update UserMissionProgress]
    G --> H[Return success + progress %]
```

---
