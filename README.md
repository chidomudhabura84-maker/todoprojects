# Django Todo App

A modern, feature-rich todo application built with Django 6.0.4, featuring a beautiful dark theme with warm accent colors.

## Features

- ✅ Create, read, update, and delete todos
- 📊 Priority levels (Low, Medium, High, Urgent)
- 🏷️ Categories (Work, Personal, Shopping, Health, Other)
- 📅 Due dates with overdue detection
- 🔍 Real-time search and filtering
- 📈 Statistics dashboard
- 🌙 Dark theme with warm color accents
- 📱 Responsive design
- ⚡ Modern UI with animations

## Local Development

### Prerequisites
- Python 3.8+
- pip

### Setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser (optional):
   ```bash
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser to `http://127.0.0.1:8000/`

## Deployment

This app is configured for deployment on Render.com.

### Environment Variables
- `DEBUG`: Set to `false` for production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `SECRET_KEY`: Django secret key (auto-generated on Render)

### Deploy to Render
1. Connect your GitHub repository to Render
2. Use the `render.yaml` configuration file
3. Set the environment variables as specified above
4. Deploy!

## Project Structure

```
django_todo/
├── todoproject/          # Main Django project
│   ├── settings.py      # Django settings
│   ├── urls.py          # Main URL configuration
│   └── wsgi.py          # WSGI configuration
├── todos/               # Todo app
│   ├── models.py        # Todo model
│   ├── views.py         # Views and logic
│   ├── urls.py          # App URL configuration
│   ├── forms.py         # Django forms
│   └── templates/       # HTML templates
├── requirements.txt     # Python dependencies
├── render.yaml         # Render deployment config
└── manage.py           # Django management script
```

## Technologies Used

- **Backend**: Django 6.0.4
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **Icons**: Font Awesome
- **Styling**: Custom CSS with gradients and animations

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).