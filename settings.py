
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework_simplejwt',
    'your_app',
]

CORS_ALLOWED_ORIGINS = [
    'https://yourfrontend.netlify.app',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

JWT_AUTH = {
    'JWT_SECRET_KEY': 'your_secret_key',
    'JWT_ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'JWT_REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}
    