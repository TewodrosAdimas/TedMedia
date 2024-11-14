# Posts App API Documentation

## **Base URL**
```
http://yourdomain.com/posts/
```

---

### 1. **User Feed**

- **Endpoint:** `GET posts/feed/`
- **Description:** Retrieves posts from users followed by the authenticated user, ordered by creation date.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (200 OK):**
        ```json
        [
            {
                "id": "post_id",
                "author": "username",
                "content": "string",
                "created_at": "timestamp",
                "updated_at": "timestamp"
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

### 2. **Post CRUD**

- **Endpoint:** `posts/posts/`
- **Description:** Provides CRUD operations on posts.
- **Endpoints:**
    - **Create Post:** `POST posts/posts/`
    - **List Posts:** `GET posts/posts/`
    - **Retrieve Post:** `GET posts/posts/<id>/`
    - **Update Post:** `PUT posts/posts/<id>/`
    - **Delete Post:** `DELETE posts/posts/<id>/`
- **Request/Response**: Refer to `PostSerializer` fields.

---

### 3. **Like a Post**

- **Endpoint:** `POST posts/like/<int:post_id>/`
- **Description:** Likes a specified post and generates a notification for the post’s author.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (201 Created):**
        ```json
        {
            "detail": "Post liked successfully."
        }
        ```
    - **Failure (400 Bad Request):**
        - **Already liked:**
          ```json
          {
              "detail": "You have already liked this post."
          }
          ```
        - **Self like attempt or invalid post:**  
          ```json
          {
              "detail": "Post not found."
          }
          ```

---

### 4. **Unlike a Post**

- **Endpoint:** `DELETE posts/unlike/<int:post_id>/`
- **Description:** Unlikes a specified post.
- **Headers:**  
    - `Authorization: Token <auth_token>`
- **Response:**
    - **Success (204 No Content):**
        ```json
        {
            "detail": "Post unliked successfully."
        }
        ```
    - **Failure (400 Bad Request):**
        ```json
        {
            "detail": "You have not liked this post yet."
        }
        ```

---

### 5. **Comment on a Post**

- **Endpoint:** `POST posts/comments/`
- **Description:** Adds a comment to a specified post and generates a notification for the post’s author.
- **Request Body:**
    ```json
    {
        "post": "post_id",
        "content": "string"
    }
    ```
- **Response:**
    - **Success (201 Created):**
        ```json
        {
            "detail": "Comment added successfully."
        }
        ```
    - **Failure (400 Bad Request):**
        ```json
        {
            "detail": "Content is required."
        }
        ```

---

### 6. **List Comments**

- **Endpoint:** `GET posts/comments/`
- **Description:** Lists all comments.
- **Response:**
    - **Success (200 OK):**
        ```json
        [
            {
                "id": "comment_id",
                "author": "username",
                "content": "string",
                "created_at": "timestamp",
                "post": "post_id"
            },
            ...
        ]
        ```

---

### 7. **Post Filters**

- **Endpoint:** `GET posts/posts/`
- **Description:** Allows filtering posts by title and content.
- **Filter Parameters:**  
    - `title` (string, optional): Filters posts containing this string in the title.
    - `content` (string, optional): Filters posts containing this string in the content.
  
**Example:**  
`/posts/?title=example&content=test`

---

**Notes:**
- **Authentication:** `Token` authentication is required for liking, unliking, commenting, and retrieving user feeds.
- **Permissions:** Only authors can edit/delete their own posts and comments (`IsAuthorOrReadOnly` permission applied).