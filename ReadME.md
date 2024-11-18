```markdown
# Social Media Application

This project is a social media application that allows users to register, authenticate, follow/unfollow other users, post content, comment on posts, like/unlike posts, and receive notifications for various actions such as following, liking, and commenting.

## Features
- **User Registration & Authentication**: Users can create accounts, log in, and manage their profiles.
- **Follow/Unfollow Users**: Users can follow and unfollow others to see their posts.
- **Notifications**: Users are notified when others follow them, like their posts, or comment on their posts.
- **Posts & Comments**: Users can create posts, comment on posts, and manage their content.
- **Like/Unlike Posts**: Users can like and unlike posts, generating notifications for the post authors.

## Setup

### Prerequisites

- Python 3.x
- Django
- Django REST Framework
- Token-based authentication

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/TewodrosAdimas/TedMedia.git
    cd TedMedia
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply migrations:
    ```bash
    python manage.py migrate
    ```

4. Create a superuser (for accessing the admin interface):
    ```bash
    python manage.py createsuperuser
    ```

5. Run the development server:
    ```bash
    python manage.py runserver
    ```

6. Access the application via `http://127.0.0.1:8000/`

---

## API Endpoints

### Accounts App

1. **User Registration**
    - **POST /accounts/register/** - Registers a new user with provided credentials.
    - **Request Body:**
        ```json
        {
            "username": "string",
            "password": "string",
            "bio": "string (optional)",
            "profile_picture": "file (optional)"
        }
        ```

2. **User Login**
    - **POST /accounts/login/** - Authenticates a user and returns a token.
    - **Request Body:**
        ```json
        {
            "username": "string",
            "password": "string"
        }
        ```

3. **User Profile**
    - **GET /accounts/profile/** - Retrieves the profile of the authenticated user.
    - **PUT /accounts/profile/** - Updates the authenticated user’s profile.

4. **Follow a User**
    - **POST /accounts/follow/<user_id>/** - Follows a user and generates a notification.
    - **Request Headers:** 
        ```plaintext
        Authorization: Token <your_token>
        ```

5. **Unfollow a User**
    - **POST /accounts/unfollow/<user_id>/** - Unfollows a user.

---

### Notifications App

1. **Get All Notifications**
    - **GET /notifications/notifications/** - Retrieves all notifications for the authenticated user.
    - **Request Headers:**
        ```plaintext
        Authorization: Token <your_token>
        ```

2. **Mark Notification as Read**
    - **POST /notifications/notifications/read/<notification_id>/** - Marks a notification as read.

---

### Posts App

1. **User Feed**
    - **GET /posts/feed/** - Retrieves posts from users followed by the authenticated user.
    - **Request Headers:**
        ```plaintext
        Authorization: Token <your_token>
        ```

2. **Post CRUD**
    - **POST /posts/posts/** - Create a new post.
    - **GET /posts/posts/** - List all posts.
    - **GET /posts/posts/<id>/** - Retrieve a single post.
    - **PUT /posts/posts/<id>/** - Update a post.
    - **DELETE /posts/posts/<id>/** - Delete a post.

3. **Like a Post**
    - **POST /posts/like/<post_id>/** - Likes a post.
    - **Request Headers:**
        ```plaintext
        Authorization: Token <your_token>
        ```

4. **Unlike a Post**
    - **DELETE /posts/unlike/<post_id>/** - Unlikes a post.

5. **Comment on a Post**
    - **POST /posts/comments/** - Adds a comment to a post.
    - **Request Body:**
        ```json
        {
            "post": "post_id",
            "content": "string"
        }
        ```

6. **List Comments**
    - **GET /posts/comments/** - Lists all comments on posts.

---

## Authentication

Token-based authentication is required for the following endpoints:
- **/accounts/profile/**
- **/accounts/follow/**
- **/accounts/unfollow/**
- **/posts/feed/**
- **/posts/like/**
- **/posts/unlike/**
- **/posts/comments/**

To authenticate, include the token in the request headers:
```plaintext
Authorization: Token <your_token>
```

## Contributing

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

### Key Adjustments:
- The project is specified as a **Social Media Application**.
- The API structure includes user registration, login, following/unfollowing users, notifications, posts, likes, and comments.
- **Authentication** is token-based for all sensitive operations, such as accessing profiles, liking posts, and interacting with notifications.
- Instructions and endpoints are tailored to a typical social media platform structure, where users can interact through posts, comments, and social connections (followers). 

