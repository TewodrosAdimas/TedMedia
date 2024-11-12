

### **Post API Endpoints**

---

#### **1. List Posts**
- **URL**: `/api/posts/`
- **Method**: `GET`
- **Description**: Returns a list of all posts.
- **Authentication**: Required (Logged-in user).
- **Response**:
    - **200 OK**
    ```json
    [
        {
            "id": 1,
            "title": "Post Title",
            "content": "Post content here",
            "created_at": "2024-11-01T12:34:56Z",
            "updated_at": "2024-11-02T12:34:56Z"
        },
        ...
    ]
    ```

---

#### **2. Create a Post**
- **URL**: `/api/posts/`
- **Method**: `POST`
- **Description**: Creates a new post. The `author` field is automatically set to the logged-in user.
- **Authentication**: Required (Logged-in user).
- **Request Body**:
    ```json
    {
        "title": "New Post Title",
        "content": "Content of the post"
    }
    ```
- **Response**:
    - **201 Created**
    ```json
    {
        "id": 2,
        "title": "New Post Title",
        "content": "Content of the post",
        "created_at": "2024-11-02T14:00:00Z",
        "updated_at": "2024-11-02T14:00:00Z"
    }
    ```

---

#### **3. Retrieve a Post**
- **URL**: `/api/posts/{id}/`
- **Method**: `GET`
- **Description**: Retrieves a specific post by ID.
- **Authentication**: Required (Logged-in user).
- **Response**:
    - **200 OK**
    ```json
    {
        "id": 1,
        "title": "Post Title",
        "content": "Post content here",
        "created_at": "2024-11-01T12:34:56Z",
        "updated_at": "2024-11-02T12:34:56Z"
    }
    ```

---

#### **4. Update a Post**
- **URL**: `/api/posts/{id}/`
- **Method**: `PUT` or `PATCH`
- **Description**: Updates a specific post. Only the author of the post can update it.
- **Authentication**: Required (Logged-in user, must be the author of the post).
- **Request Body**:
    ```json
    {
        "title": "Updated Post Title",
        "content": "Updated content of the post"
    }
    ```
- **Response**:
    - **200 OK**
    ```json
    {
        "id": 1,
        "title": "Updated Post Title",
        "content": "Updated content of the post",
        "created_at": "2024-11-01T12:34:56Z",
        "updated_at": "2024-11-02T15:00:00Z"
    }
    ```

---

#### **5. Delete a Post**
- **URL**: `/api/posts/{id}/`
- **Method**: `DELETE`
- **Description**: Deletes a specific post. Only the author of the post can delete it.
- **Authentication**: Required (Logged-in user, must be the author of the post).
- **Response**:
    - **204 No Content**

---

### **Comment API Endpoints**

---

#### **1. List Comments**
- **URL**: `/api/comments/`
- **Method**: `GET`
- **Description**: Returns a list of all comments.
- **Authentication**: Required (Logged-in user).
- **Response**:
    - **200 OK**
    ```json
    [
        {
            "id": 1,
            "post": 1,
            "content": "This is a comment",
            "created_at": "2024-11-01T12:34:56Z",
            "updated_at": "2024-11-02T12:34:56Z"
        },
        ...
    ]
    ```

---

#### **2. Create a Comment**
- **URL**: `/api/comments/`
- **Method**: `POST`
- **Description**: Creates a new comment. The `author` field is automatically set to the logged-in user, and the comment is associated with a specific post.
- **Authentication**: Required (Logged-in user).
- **Request Body**:
    ```json
    {
        "post": 1,
        "content": "This is a comment"
    }
    ```
- **Response**:
    - **201 Created**
    ```json
    {
        "id": 2,
        "post": 1,
        "content": "This is a comment",
        "created_at": "2024-11-02T14:00:00Z",
        "updated_at": "2024-11-02T14:00:00Z"
    }
    ```

---

#### **3. Retrieve a Comment**
- **URL**: `/api/comments/{id}/`
- **Method**: `GET`
- **Description**: Retrieves a specific comment by ID.
- **Authentication**: Required (Logged-in user).
- **Response**:
    - **200 OK**
    ```json
    {
        "id": 1,
        "post": 1,
        "content": "This is a comment",
        "created_at": "2024-11-01T12:34:56Z",
        "updated_at": "2024-11-02T12:34:56Z"
    }
    ```

---

#### **4. Update a Comment**
- **URL**: `/api/comments/{id}/`
- **Method**: `PUT` or `PATCH`
- **Description**: Updates a specific comment. Only the author of the comment can update it.
- **Authentication**: Required (Logged-in user, must be the author of the comment).
- **Request Body**:
    ```json
    {
        "content": "Updated content of the comment"
    }
    ```
- **Response**:
    - **200 OK**
    ```json
    {
        "id": 1,
        "post": 1,
        "content": "Updated content of the comment",
        "created_at": "2024-11-01T12:34:56Z",
        "updated_at": "2024-11-02T15:00:00Z"
    }
    ```

---

#### **5. Delete a Comment**
- **URL**: `/api/comments/{id}/`
- **Method**: `DELETE`
- **Description**: Deletes a specific comment. Only the author of the comment can delete it.
- **Authentication**: Required (Logged-in user, must be the author of the comment).
- **Response**:
    - **204 No Content**

---

### **Filtering and Search**
- **Posts**: You can filter posts by title or content using query parameters, such as:
    - `/api/posts/?title=searchterm`
    - `/api/posts/?content=searchterm`
  
### **Permissions**
- Both **Post** and **Comment** endpoints require authentication. 
- Only the **author** of a post or comment can update or delete it. This is enforced by the `IsAuthorOrReadOnly` permission.

---

