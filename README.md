# "SaaSMon"
## Site Version Checking and Tracking app built on [FastAPI](https://fastapi.tiangolo.com/)
## Public API example is live on <https://api.saasmon.xyz> . View documentation: <https://api.saasmon.xyz/docs> or <https://api.saasmon.xyz/redoc>
### The site may be down from time to time for maintenance or feature additions

This tool will be used in my day job to monitor and track changes we make to our SaaS environment to speed up my deployment/upgrade efforts and minimize delays due to dependency issues.  The public deployment is just there for review - this app would typically be deployed as an internal tool.

# Key Libraries
- FastAPI
- SQLAlchemy w/ Postgres
- Pydantic
- Jose (JWT)

# Roadmap
I do not have an explicit roadmap in mind. However, my goal is to commit to this repo daily as I learn more about FastAPI and SQLAlchemy.
My hope is to have a fully functional API and back-end ready before the end of March and begin to build out a front-end after that.

By the end of the project, this will be a fully-featured API with authentication (JWT), reverse proxy, containerized with Docker, use of Github Actions for CI/CD, CircleCI, Github Secrets, and ultimately deployed on AWS.

## Features to date:
### ✔ Hosted on DigitalOcean Ubuntu 20.04 LTS droplet
### ✔ Session authentication with JWT
### ✔ Reverse proxy with Nginx
### ✔ Served on gunicorn WSGI server
