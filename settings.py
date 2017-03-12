# DJANGO SETTINGS
INSTALLED_APPS = (
    'data',
    'django_extensions',
)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        # use host specific settings to indicate database's name and access
    }
}
SECRET_KEY = 'TRY_TO_GUESS'


# OTHER SETTINGS
DEFAULT_PAGE_SIZE = 20
MAX_PER_PAGE = 1000
