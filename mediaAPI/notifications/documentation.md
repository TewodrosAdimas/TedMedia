# Notifications App API Documentation

## **Base URL**
```
http://yourdomain.com/notifications/
```

---

### 1. **Get All Notifications**

- **Endpoint:** `GET notifications/notifications/`
- **Description:** Retrieves all notifications for the authenticated user, ordered by timestamp (most recent first).
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (200 OK):**
        ```json
        [
            {
                "id": "notification_id",
                "actor": "actor_username",
                "verb": "string describing the action",
                "timestamp": "timestamp",
                "is_read": false,
                "target": {
                    "type": "post",
                    "id": "target_object_id",
                    "title": "post title"
                }
            },
            ...
        ]
        ```
    - **Failure (401 Unauthorized):**
        ```json
        {
            "detail": "Authentication credentials were not provided."
        }
        ```

---

### 2. **Mark Notification as Read**

- **Endpoint:** `POST notifications/notifications/read/<int:notification_id>/`
- **Description:** Marks a specific notification as read.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (200 OK):**
        ```json
        {
            "detail": "Notification marked as read."
        }
        ```
    - **Failure (404 Not Found):**
        ```json
        {
            "detail": "Notification not found."
        }
        ```
    - **Failure (401 Unauthorized):**
        ```json
        {
            "detail": "Authentication credentials were not provided."
        }
        ```

---

**Notes:**
- **Authentication:** Token-based authentication is required for all endpoints in the notifications app.
- **Response Fields:**
    - **id:** Unique identifier of the notification.
    - **actor:** Username of the user who triggered the notification.
    - **verb:** Description of the action that generated the notification (e.g., "liked your post").
    - **timestamp:** When the notification was created.
    - **is_read:** Boolean indicating if the notification has been read.
    - **target:** Contains details about the notification's target (e.g., post or comment).