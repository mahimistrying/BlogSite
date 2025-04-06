# BlogSite

**BlogSite** is a personal blogging platform built using Django. It allows users to create, manage, and view blog posts. The project is structured to support extensibility for features like portfolios, games, media galleries, and more.

## Features

- User authentication (login/logout)
- Create, edit, and delete blog posts
- Display blog posts on homepage
- Organized folder structure for different app modules
- Media and static file handling
- Easily extensible for portfolio, media, or game projects

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, Bootstrap (via static files)
- **Database**: SQLite (development)

## Project Structure

```
BlogSite/
├── blog/                 # Blog application
├── portfolio/            # Portfolio app (optional/extendable)
├── games/                # Games app (optional/extendable)
├── media/                # Media uploads
├── static/               # CSS, JS, and static assets
├── templates/            # Shared HTML templates
├── BlogSite/             # Project settings and URLs
├── db.sqlite3            # SQLite database
├── manage.py             # Django CLI entry point
└── README.md             # Project overview
```

## Getting Started

### Prerequisites

- Python 3.x
- Django 4.x or above (install via pip)

### Installation

```bash
git clone https://github.com/mahimistrying/BlogSite.git
cd BlogSite
pip install -r requirements.txt
```

### Running the Server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Visit `http://127.0.0.1:8000/` to view the blog site in your browser.

## Screenshots

*(Add screenshots of your homepage, post view, and admin panel if available.)*

## License

This project is licensed under the MIT License.

## Author

**Mahim Uddin Ahmed**  
GitHub: [@mahimistrying](https://github.com/mahimistrying)

