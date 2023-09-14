# API Documentation

## Overview

This is the documentation for a simple Flask API for managing persons. This API allows you to perform basic CRUD (Create, Read, Update, Delete) operations on a "person" resource.

## Base URL

The base URL for all API endpoints is:

```
http://127.0.0.1:5000/api
```

## Running Locally

To run the API locally on your machine, follow these steps:

1. **Clone the Repository:**

   Clone the API repository to your local machine using Git:

   ```bash
   git clone https://github.com/Resa200/HNGX-Internship-Tasks.git
   ```

2. **Navigate to the API Directory:**

   Change your working directory to the API directory:

   ```bash
   cd TASK2
   ```

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install requirements.txt
   ```

4. **Run the API:**

   Start the API by running the following command:

   ```bash
   flask --app api.py run
   ```

   The API will start locally and be accessible at `http://127.0.0.1:5000/api`.

5. **Test the API:**

    Test the API by running the following command:

    ```
    python test_api.py
    ```

## Using the Deployed Endpoint

The API is deployed and hosted on a server, you can use the following URL to access it:

```
https://task2-api.onrender.com/api
```

## API Endpoints

### Create a Person (POST)

- **Endpoint**: `/api`
- **Description**: Create a new person.
- **Request Format**:
  - Method: POST
  - Content-Type: application/json
  - Body:
    ```json
    {
        "name": "John Doe"
    }
    ```
- **Response Format**:
  - Status Code: 201 (Created)
  - Body:
    ```json
    {
        "message": "Person created successfully"
    }
    ```

### Retrieve a Person (GET)

- **Endpoint**: `/api/{user_id}`
- **Description**: Retrieve details of a person by their `user_id`.
- **Request Format**:
  - Method: GET
  - URL: `/api/{user_id}`
- **Response Format**:
  - Status Code: 200 (OK)
  - Body:
    ```json
    {
        "id": 1,
        "name": "John Doe"
    }
    ```

### Update a Person (PUT)

- **Endpoint**: `/api/{user_id}`
- **Description**: Update details of an existing person by their `user_id`.
- **Request Format**:
  - Method: PUT
  - Content-Type: application/json
  - Body:
    ```json
    {
        "name": "Jane Doe"
    }
    ```
- **Response Format**:
  - Status Code: 200 (OK)
  - Body:
    ```json
    {
        "message": "Person updated successfully"
    }
    ```

### Delete a Person (DELETE)

- **Endpoint**: `/api/{user_id}`
- **Description**: Delete a person by their `user_id`.
- **Request Format**:
  - Method: DELETE
  - URL: `/api/{user_id}`
- **Response Format**:
  - Status Code: 200 (OK)
  - Body:
    ```json
    {
        "message": "Person deleted successfully"
    }
    ```

## Error Handling

- If a request is malformed or missing required fields, the API will respond with a 400 (Bad Request) status code and an error message.
- If a requested person does not exist (e.g., when retrieving or updating), the API will respond with a 404 (Not Found) status code and an error message.
