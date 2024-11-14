## **Notification API Documentation**

### **Base URL**
```
http://<your-domain>/api/
```

---

### **1. Get Notifications**

#### **Endpoint**
```
GET /notifications/
```

#### **Description**
This endpoint retrieves all notifications for the authenticated user, ordered by the timestamp in descending order.

#### **Request Headers**
- **Authorization**: Required. The request must include an authentication token or session cookie to identify the user.
  
#### **Response**

- **Status Code**: `200 OK`
- **Response Body** (Example):
  ```json
  [
    {
      "id": 1,
      "recipient": 1,
      "actor": 2,
      "verb": "liked your post",
      "target_content_type": "post",
      "target_object_id": 10,
      "timestamp": "2024-11-14T10:00:00Z",
      "is_read": false
    },
    {
      "id": 2,
      "recipient": 1,
      "actor": 3,
      "verb": "commented on your post",
      "target_content_type": "post",
      "target_object_id": 15,
      "timestamp": "2024-11-13T15:30:00Z",
      "is_read": true
    }
  ]
  ```

#### **Error Response**

- **Status Code**: `401 Unauthorized`  
  - **Message**: `Authentication credentials were not provided.`  
  - This occurs if the user is not authenticated or the authentication token is missing/invalid.
  
---

### **2. Mark Notification as Read**

#### **Endpoint**
```
POST /notifications/read/<int:notification_id>/
```

#### **Description**
Marks a specific notification as read for the authenticated user.

#### **URL Parameters**
- `notification_id`: The ID of the notification to mark as read.

#### **Request Headers**
- **Authorization**: Required. The request must include an authentication token or session cookie to identify the user.

#### **Request Body**
No body is required for this endpoint.

#### **Response**

- **Status Code**: `200 OK`
  - **Response Body**:
    ```json
    {
      "detail": "Notification marked as read."
    }
    ```

#### **Error Responses**

- **Status Code**: `401 Unauthorized`  
  - **Message**: `Authentication credentials were not provided.`  
  - This occurs if the user is not authenticated or the authentication token is missing/invalid.

- **Status Code**: `404 Not Found`
  - **Message**: `Notification not found.`  
  - This occurs if the notification with the provided `notification_id` does not exist or is not associated with the authenticated user.

---

### **General Notes**
- All endpoints require the user to be authenticated. You can use Django's authentication mechanisms (like session-based authentication or token authentication) to authenticate requests.
  
- Responses are returned in JSON format.

- The `Notification` model contains the following fields:
  - `recipient`: The user who is receiving the notification.
  - `actor`: The user who caused the event (e.g., liking or commenting).
  - `verb`: A textual description of the event (e.g., "liked your post").
  - `target_content_type`: The content type of the target object (e.g., a post or comment).
  - `target_object_id`: The ID of the target object (e.g., the ID of the post).
  - `timestamp`: The timestamp when the notification was created.
  - `is_read`: Whether the notification has been read by the recipient.

---