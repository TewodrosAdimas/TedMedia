# API Documentation

## Base URL
All endpoints are prefixed by the base URL:  
```
http://yourdomain.com/accounts/
```

---

### 1. **User Registration**

- **Endpoint:** `POST accounts/register/`
- **Description:** Registers a new user with the provided credentials and profile details.
- **Request Body:**
    ```json
    {
        "username": "string",
        "password": "string",
        "bio": "string (optional)",
        "profile_picture": "file (optional)"
    }
    ```
- **Response:**
    - **Success (201 Created):**
        ```json
        {
            "id": "user_id",
            "username": "string",
            "bio": "string",
            "profile_picture": "URL"
        }
        ```
    - **Failure (400 Bad Request):**  
        ```json
        {
            "error": "validation errors"
        }
        ```
---

### 2. **User Login**

- **Endpoint:** `POST accounts/login/`
- **Description:** Authenticates a user and returns an authorization token.
- **Request Body:**
    ```json
    {
        "username": "string",
        "password": "string"
    }
    ```
- **Response:**
    - **Success (200 OK):**
        ```json
        {
            "token": "auth_token",
            "username": "string"
        }
        ```
    - **Failure (400 Bad Request):**  
        ```json
        {
            "error": "Invalid credentials"
        }
        ```

---

### 3. **User Profile**

- **Endpoint:** `GET accounts/profile/`
- **Description:** Retrieves the profile information of the authenticated user.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (200 OK):**
        ```json
        {
            "id": "user_id",
            "username": "string",
            "bio": "string",
            "profile_picture": "URL"
        }
        ```
    - **Failure (401 Unauthorized):**
        ```json
        {
            "detail": "Authentication credentials were not provided."
        }
        ```
    
---

### 4. **Update User Profile**

- **Endpoint:** `PUT accounts/profile/`
- **Description:** Updates the authenticated user’s profile information.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Request Body:**
    ```json
    {
        "username": "string",
        "password": "string",
        "bio": "string (optional)",
        "profile_picture": "file (optional)"
    }
    ```
- **Response:**
    - **Success (200 OK):**
        ```json
        {
            "id": "user_id",
            "username": "string",
            "bio": "string",
            "profile_picture": "URL"
        }
        ```
    - **Failure (400 Bad Request):**
        ```json
        {
            "error": "validation errors"
        }
        ```
---

## Notes

- **Authentication:** `Token` authentication is required for accessing the profile endpoints (`GET /profile/` and `PUT /profile/`).
- **Error Handling:** The API returns appropriate error messages with status codes, such as `400` for validation issues and `401` for authentication errors.

