## **Post API Endpoints**

### 1. **List Posts**
- **Endpoint:** `/posts/posts/`
- **Method:** `GET`
- **Description:** Retrieves a list of all posts.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only authenticated users can access this endpoint.
- **Response:**
  - `200 OK`: List of posts (serialized data).
  
### 2. **Create a Post**
- **Endpoint:** `/posts/posts/`
- **Method:** `POST`
- **Description:** Creates a new post. The authenticated user will be automatically set as the author.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only authenticated users can create posts.
- **Request Body:** 
  ```json
  {
    "title": "Post Title",
    "content": "Post Content"
  }
  ```
- **Response:**
  - `201 Created`: Post created successfully.
  - `400 Bad Request`: If required fields (`title`, `content`) are missing.

### 3. **Retrieve a Specific Post**
- **Endpoint:** `/posts/posts/{id}/`
- **Method:** `GET`
- **Description:** Retrieves a specific post by its ID.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Post can be viewed by any authenticated user.
- **Response:**
  - `200 OK`: Detailed data of the requested post.
  - `404 Not Found`: If post with given ID does not exist.

### 4. **Update a Post**
- **Endpoint:** `/posts/posts/{id}/`
- **Method:** `PUT`
- **Description:** Updates an existing post. Only the author of the post can update it.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only the author of the post can update it.
- **Request Body:**
  ```json
  {
    "title": "Updated Post Title",
    "content": "Updated Content"
  }
  ```
- **Response:**
  - `200 OK`: Post updated successfully.
  - `400 Bad Request`: If invalid data is provided.
  - `404 Not Found`: If post with given ID does not exist.

### 5. **Delete a Post**
- **Endpoint:** `/posts/posts/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes an existing post. Only the author of the post can delete it.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only the author of the post can delete it.
- **Response:**
  - `204 No Content`: Post deleted successfully.
  - `404 Not Found`: If post with given ID does not exist.

## **Comment API Endpoints**

### 1. **Create a Comment**
- **Endpoint:** `/posts/posts/{post_id}/comments/`
- **Method:** `POST`
- **Description:** Adds a comment to a post. The authenticated user will be set as the author of the comment.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only authenticated users can comment on posts.
- **Request Body:**
  ```json
  {
    "content": "This is a comment."
  }
  ```
- **Response:**
  - `201 Created`: Comment added successfully.
  - `400 Bad Request`: If content is not provided in the request.

### 2. **Retrieve Comments for a Post**
- **Endpoint:** `/posts/posts/{post_id}/comments/`
- **Method:** `GET`
- **Description:** Retrieves all comments for a specific post.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Any authenticated user can view the comments of a post.
- **Response:**
  - `200 OK`: List of comments for the specified post.

### 3. **Update a Comment**
- **Endpoint:** `/posts/comments/{id}/`
- **Method:** `PUT`
- **Description:** Updates a specific comment. Only the author of the comment can update it.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only the author of the comment can update it.
- **Request Body:**
  ```json
  {
    "content": "Updated comment content"
  }
  ```
- **Response:**
  - `200 OK`: Comment updated successfully.
  - `404 Not Found`: If comment with given ID does not exist.

### 4. **Delete a Comment**
- **Endpoint:** `/posts/comments/{id}/`
- **Method:** `DELETE`
- **Description:** Deletes a specific comment. Only the author of the comment can delete it.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only the author of the comment can delete it.
- **Response:**
  - `204 No Content`: Comment deleted successfully.
  - `404 Not Found`: If comment with given ID does not exist.

## **Like API Endpoints**

### 1. **Like a Post**
- **Endpoint:** `/posts/posts/like/{post_id}/`
- **Method:** `POST`
- **Description:** Likes a post and generates a notification for the post author.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only authenticated users can like a post.
- **Response:**
  - `201 Created`: Post liked successfully.
  - `400 Bad Request`: If user has already liked the post.

### 2. **Unlike a Post**
- **Endpoint:** `/posts/posts/unlike/{post_id}/`
- **Method:** `DELETE`
- **Description:** Unlikes a post.
- **Authentication Required:** Yes, user must be authenticated.
- **Permissions:** Only authenticated users can unlike a post.
- **Response:**
  - `204 No Content`: Post unliked successfully.
  - `400 Bad Request`: If the user has not liked the post yet.


### **Permissions**

- `IsAuthenticated`: Ensures the user must be logged in to access certain endpoints.
- `IsAuthorOrReadOnly`: Custom permission allowing only the author of a post or comment to modify or delete it. Other users can view the post/comment, but not update or delete.

---