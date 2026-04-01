# QuizElite

A modern, robust Quiz Web Application built with Django.

## Features
- Multiple choice questions
- Categorized quizzes
- Time limits and automatic scoring
- User registration and authentication
- Review past quiz attempts and detailed performance
- Clean and responsive UI

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/debasistripathy400-web/quiz-app.git
   cd quiz-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

6. Open your web browser and navigate to `http://127.0.0.1:8000/`.
