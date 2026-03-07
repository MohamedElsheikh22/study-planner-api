# Study Planner API

A RESTful API that helps students organize their study schedule by managing subjects and study sessions.

## Live API
https://MohamedAdel65.pythonanywhere.com

## Technologies
- Django
- Django REST Framework
- JWT Authentication
- SQLite (development)

## Features
- User registration and login with JWT
- Subjects management (CRUD)
- Study Sessions management (CRUD)
- Mark study session as completed
- Filter sessions by subject
- Users can only access their own data

## API Endpoints

### Authentication
- POST /api/auth/register/
- POST /api/auth/login/

### Subjects
- GET /api/subjects/
- POST /api/subjects/
- GET /api/subjects/{id}/
- PUT /api/subjects/{id}/
- DELETE /api/subjects/{id}/

### Study Sessions
- GET /api/sessions/
- POST /api/sessions/
- GET /api/sessions/{id}/
- PUT /api/sessions/{id}/
- DELETE /api/sessions/{id}/
- PATCH /api/sessions/{id}/complete/