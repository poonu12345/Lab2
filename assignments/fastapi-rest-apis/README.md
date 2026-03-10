# 📘 Assignment: 🕸️ REST APIs with FastAPI

## 🎯 Objective

Students will learn how to build and run RESTful web services using the FastAPI framework, gaining experience with routing, HTTP methods, and request/response handling.

## 📝 Tasks

### 🛠️  Set up a basic FastAPI application

#### Description
Create a FastAPI app with a few simple endpoints and run the server locally.

#### Requirements
Completed application should:

- Install and import FastAPI and `uvicorn`
- Define an app instance (`app = FastAPI()`)
- Add at least two GET endpoints returning JSON data
- Run the server using `uvicorn` on `localhost:8000`
- Confirm endpoints respond via browser or `curl`


### 🛠️  Implement CRUD endpoints for a resource

#### Description
Extend the application to support create, read, update, and delete operations for a sample resource (e.g., items or users).

#### Requirements
Completed application should:

- Use appropriate HTTP methods (`POST`, `GET`, `PUT`, `DELETE`)
- Accept and return JSON payloads
- Store data in an in-memory Python list or dictionary
- Validate input data using Pydantic models
- Include clear success and error responses


### 🛠️  Write basic tests using `requests` or `httpx`

#### Description
Write a short script or notebook to hit your API endpoints and verify their behavior.

#### Requirements
Tests should:

- Send requests to each CRUD endpoint
- Check for expected status codes and response bodies
- Report any failures or mismatches
