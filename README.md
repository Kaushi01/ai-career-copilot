# AI Career Copilot

### Your Career, Mapped.

An AI-powered career guidance web application that analyzes resumes against a user's target career role, identifies skill gaps, and generates personalized learning roadmaps and interview questions.

**[Live Demo](https://ai-career-copilot-rce5.onrender.com)** · **[GitHub Repository](https://github.com/Kaushi01/ai-career-copilot)**

---

## Overview

AI Career Copilot helps users understand how well their existing skills align with their desired career path.

Users can upload their resume, specify their career goal, and receive AI-generated insights covering relevant skills, missing skills, a personalized learning roadmap, and role-specific interview questions.

The application also includes user authentication and report history, allowing users to revisit their previous analyses.

## Features

- **Resume Analysis:** Upload a resume in PDF or DOCX format or provide resume text.
- **Career-Based Skill Extraction:** Identifies skills relevant to the user's selected career goal.
- **Skill Gap Analysis:** Highlights missing skills based on the desired role.
- **Personalized Learning Roadmap:** Generates a roadmap focused on identified skill gaps.
- **Interview Preparation:** Generates interview questions tailored to the selected career goal.
- **User Authentication:** Signup, login, and logout functionality.
- **Report History:** Stores previous resume analyses for individual users.
- **Cloud Deployment:** Hosted using Render with a cloud-hosted MySQL-compatible database.

## Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Flask |
| AI Integration | Groq API, OpenAI Python SDK |
| AI Model | openai/gpt-oss-120b |
| Database | TiDB Cloud (MySQL) |
| ORM | SQLAlchemy |
| Frontend | HTML, CSS, Jinja2 |
| Document Processing | PyPDF2, python-docx |
| Deployment | Render, Gunicorn |
| Environment Management | python-dotenv |

## How It Works

1. User creates an account or logs in.
2. User uploads a resume or enters resume text.
3. User specifies their desired career goal.
4. The application extracts the resume content.
5. The Groq API processes the resume using an AI-powered prompt.
6. Structured JSON results are generated.
7. Results are saved in the database.
8. Users can revisit previous reports through the history section.

## AI Analysis Output

Each analysis generates four key outputs:

| Output | Description |
|---|---|
| Relevant Skills | Skills matching the selected career goal |
| Missing Skills | Skills that need improvement or development |
| Learning Roadmap | Personalized roadmap covering identified gaps |
| Interview Questions | Role-specific interview preparation questions |

## Project Structure

```text
ai-career-copilot/
│
├── app.py
├── ai.py
├── db.py
├── models.py
├── requirements.txt
├── .gitignore
│
├── static/
│   └── style.css
│
└── templates/
    ├── base.html
    ├── login.html
    ├── signup.html
    ├── dashboard.html
    └── history.html
```

## Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/Kaushi01/ai-career-copilot.git
cd ai-career-copilot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
DATABASE_URL=your_tidb_database_url
FLASK_SECRET_KEY=your_secret_key
```

Never commit your `.env` file or expose API credentials.

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

## Future Improvements

- Password hashing and enhanced authentication security.
- Downloadable PDF reports.
- Resume scoring and job-description matching.
- Integration with job search platforms.
- More detailed career progression insights.
- Improved dashboard analytics.

## Deployment

The application is deployed on **Render**, with TiDB Cloud used for database hosting and Groq powering AI-based resume analysis.

**Live Application:** https://ai-career-copilot-rce5.onrender.com

---


## 📸 Application Preview

![Screenshot 1](screenshots/Screenshot%20(1366).png)

![Screenshot 2](screenshots/Screenshot%20(1367).png)

![Screenshot 3](screenshots/Screenshot%20(1368).png)

![Screenshot 4](screenshots/Screenshot%20(1369).png)


### Built With Python & AI

Developed as a project exploring AI integration, web application development, database management, and personalized career guidance.
