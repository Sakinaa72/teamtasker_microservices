# teamtasker_microservices

TeamTasker is a scalable, microservices-driven task and project management system built using React (frontend) and Django microservices (backend) It supports authentication, task assignments, real-time notifications, role-based access, and more — designed to be extensible with AI and deployable using Docker.

🚀 Features

🧩 Microservices Architecture (Django)

🛡️ JWT Authentication with API Gateway

📁 Projects and Task Management

👥 User Profiles, Roles, and Permissions

🔔 Notifications (Email & In-App)

💬 Real-time Chat (WebSocket)

📈 Activity Logs & Commenting

🚀 Dockerized with Docker Compose

🔧 Redis, RabbitMQ, Celery integration

✨ Designed for future AI integrations

🛠️ Tech Stack

Frontend:

React
Axios, React Router
Plain CSS
Redux Toolkit

Backend:

Django + Django REST Framework
PostgreSQL (per service)
Celery + Redis + RabbitMQ
JWT + Role-based Access
Django Channels (for chat)

Architecture:

API Gateway (Django or FastAPI-based)

6+ Django Microservices: Auth, User, Project, Task, Comment, Notification, Chat

Async communication via RabbitMQ

Caching & sessions via Redis

Dockerized microservices + docker-compose.yml

Optional: Nginx as reverse proxy
