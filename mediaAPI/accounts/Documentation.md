# **API Documentation**

## **Base URL**
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

### 5. **Follow a User**

- **Endpoint:** `POST accounts/follow/<user_id>/`
- **Description:** Follows another user and generates a notification for the followed user.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (200 OK):**
        ```json
        {
            "message": "You are now following this user"
        }
        ```
    - **Failure (400 Bad Request):**
        ```json
        {
            "error": "You cannot follow yourself"
        }
        ```
        ```json
        {
            "message": "You already follow this user"
        }
        ```
    - **Failure (404 Not Found):**
        ```json
        {
            "detail": "User not found."
        }
        ```

### **Example Request**
```bash
curl -X POST -H "Authorization: Token <your-token>" http://127.0.0.1:8000/accounts/follow/1/
```

---

### 6. **Unfollow a User**

- **Endpoint:** `POST accounts/unfollow/<user_id>/`
- **Description:** Unfollows a user.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (200 OK):**
        ```json
        {
            "message": "You have unfollowed this user"
        }
        ```
    - **Failure (400 Bad Request):**
        ```json
        {
            "error": "You cannot unfollow yourself"
        }
        ```
        ```json
        {
            "message": "You do not follow this user"
        }
        ```
    - **Failure (404 Not Found):**
        ```json
        {
            "detail": "User not found."
        }
        ```

### **Example Request**
```bash
curl -X POST -H "Authorization: Token <your-token>" http://127.0.0.1:8000/accounts/unfollow/1/
```

---

## **Notifications**
When a user follows another user, a **notification** is generated for the followed user with details:
- **Recipient**: The user who is followed.
- **Actor**: The user who followed.
- **Verb**: `"started following you"`.

---
