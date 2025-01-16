# Blogging System API

A RESTful API for a blogging system built with Django Rest Framework (DRF). This system allows users to create, manage, and interact with blogs and comments.

## Features

### User Management

- User registration, login, and logout.
- Password change functionality.
- View user profile details.

### Blog Management

- Create, edit, delete drafts and published blogs.
- Publish drafts.
- List and filter blogs by Author, Category, Tags, and search across all blog attributes.
- Pagination support for blog listings.
- Display the number of comments in blog responses.

### Comment Management

- Users can add comments to any published blog.
- Blog authors can delete any comment on their self-published blogs.

## Tech Stack

- Python 3.10.12
- Django 5.1.4
- Django Rest Framework
- SQLite

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vedpatel4/BlogApp.git
   cd BlogApp
   ```
2. **Create and activate a virtual environment:**

   ```bash
    python -m venv env
    source env/bin/activate
    # On Windows use `env\Scripts\activate`
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the project root directory and add the following:

   ```env
   SECRET_KEY=<your-django-secrete-key>
   DEBUG=True
   ```

5. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Users

- `POST /api/register/` - Register a new user.
- `POST /api/login/` - Log in a user.
- `POST /api/logout/` - Log out the current user.
- `POST /api/change-password/` - Change the password for the logged-in user.
- `GET /api/profile/` - Retrieve the current user's profile.

### Blogs

- `POST /api/blogs/create/` - Create a blog.
- `GET /api/blogs/` - List blogs with filtering, searching, and pagination.
- `GET /api/blogs/<id>/` - Retrieve all the blog details.
- `PUT /api/blogs/<id>/update` - Edit a blog.
- `DELETE /api/blogs/<id>/delete` - Delete a blog.
- `PUT /api/blogs/<id>/publish/` - Publish a draft blog.

### Comments

- `GET /api/blogs/<id>/comments` - List comments of a blog
- `POST /api/blogs/<id>/comments/create` - Add a comment to a blog.
- `DELETE /api/blogs/<id>/comments/<id>/delete` - Delete a comment (only by the blog author).

### Filtering and Searching

- Filter blogs by `author`, `category`, and `tags`.
- Search blogs across `title`, `content`, and other attributes.
