# 🚀 Train-project

A **RESTful API** for managing projects and tasks with user authentication and role-based permissions using **FastAPI** and **PostgreSQL**.

## 📚 **Overview**

**Train-project** is a powerful backend API designed to handle:
- **Authentication:** Secure user authentication using JWT tokens.
- **User Management:** Registration, login, and role-based permissions.
- **Project Management:** Create, update, and delete projects.
- **Task Management:** Assign tasks, update statuses, and track progress.

---

## 🛠️ **Tech Stack**

- **Backend:** FastAPI  
- **Database:** PostgreSQL  
- **Containerization:** Docker  
- **Authentication:** JWT Tokens  

---

## 🚀 **Installation**

### 📦 **Clone the Repository**
```bash
git clone https://github.com/Ivan2330/Train-project.git
cd Train-project
```

---

## ⚙️ Setup Environment

1. **Create a .env file with necessary environment variables**:
   ```bash
   DATABASE_URL=postgresql://user:password@localhost/db_name
   SECRET_KEY=your_secret_key
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **🐳 Run with Docker**:
   ```bash
   docker-compose up --build
   ```
4. **▶️ Run Locally**:
   ```bash
   uvicorn main:app --reload
   ```

---

## 📑 API Endpoints

| **Method** | **Endpoint**       | **Description**          |
|------------|---------------------|--------------------------|
| `POST`     | `/auth/register`    | Register a new user      |
| `POST`     | `/auth/login`       | Login user               |
| `GET`      | `/projects`         | List all projects        |
| `POST`     | `/projects`         | Create a project         |
| `PUT`      | `/tasks/{id}`       | Update a task by ID      |

---

## 📂 Project Structure
```bash
.
├── app/
│   ├── auth.py        # Authentication logic
│   ├── db.py          # Database connection
│   ├── models.py      # Database models
│   ├── projects.py    # Project-related endpoints
│   ├── tasks.py       # Task-related endpoints
├── main.py           # Application entry point
├── requirements.txt  # Dependencies
├── .gitignore        # Ignored files
├── LICENSE           # MIT License
└── README.md         # Documentation
```

---

## 📝 License

This project is licensed under the MIT License.

---

## 📞 Contact

**Author:** Ivan Kozhevnyk
**Email:** ivankozhevnyk@gmail.com
**GitHub:** Ivan2330










