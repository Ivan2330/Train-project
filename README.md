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
   # Database
   DATABASE_URL=postgresql://postgres:postgres@db:5432/train_db

   # App
   SECRET_KEY=your_secret_key
   DEBUG=True
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
   python main.py
   ```

---

## 📑 **API Endpoints**

### 🔑 **Authentication**

| **Method** | **Endpoint**                   | **Description**       | **Tag**          |
|------------|---------------------------------|-----------------------|------------------|
| `POST`     | `/auth/jwt/login`               | Login with JWT        | Auth:Jwt.Login   |
| `POST`     | `/auth/jwt/logout`              | Logout with JWT       | Auth:Jwt.Logout  |
| `POST`     | `/auth/register`                | User registration     | Register:Register|
| `POST`     | `/auth/forgot-password`         | Forgot password       | Reset:Forgot PW  |
| `POST`     | `/auth/reset-password`          | Reset password        | Reset:Reset PW   |
| `POST`     | `/auth/request-verify-token`    | Request verify token  | Verify:Request   |
| `POST`     | `/auth/verify`                  | Verify token          | Verify:Verify    |

---

### 👤 **Users**

| **Method** | **Endpoint**       | **Description**     | **Tag**               |
|------------|---------------------|---------------------|-----------------------|
| `GET`      | `/users/me`         | Get current user    | Users:Current User    |
| `PATCH`    | `/users/me`         | Update current user | Users:Patch Current   |
| `GET`      | `/users/{id}`       | Get user by ID      | Users:User            |
| `PATCH`    | `/users/{id}`       | Update user by ID   | Users:Patch User      |
| `DELETE`   | `/users/{id}`       | Delete user by ID   | Users:Delete User     |

---

### 📌 **Tasks**

| **Method** | **Endpoint**       | **Description**     | **Tag**       |
|------------|---------------------|---------------------|--------------|
| `POST`     | `/tasks/`           | Create task         | Create Task  |
| `GET`      | `/tasks/{task_id}`  | Get task by ID      | Get Task     |
| `PATCH`    | `/tasks/{task_id}`  | Update task by ID   | Update Task  |
| `DELETE`   | `/tasks/{task_id}`  | Delete task by ID   | Delete Task  |

---

### 🗂️ **Projects**

| **Method** | **Endpoint**           | **Description**     | **Tag**        |
|------------|-------------------------|---------------------|---------------|
| `POST`     | `/projects/`           | Create project      | Create Project|
| `GET`      | `/projects/{project_id}`| Get project by ID   | Get Project   |
| `PATCH`    | `/projects/{project_id}`| Update project by ID| Update Project|
| `DELETE`   | `/projects/{project_id}`| Delete project by ID| Delete Project|

---

### 🌐 **Default**

| **Method** | **Endpoint**             | **Description**       | **Tag**              |
|------------|---------------------------|-----------------------|----------------------|
| `GET`      | `/authenticated-route`   | Test authenticated route | Authenticated Route |

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

- **Author:** Ivan Kozhevnyk
- **Email:** ivankozhevnyk@gmail.com
- **GitHub:** Ivan2330










