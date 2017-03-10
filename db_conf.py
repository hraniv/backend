DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite.db',
    }
}

INSTALLED_APPS = (
    'data',
    'django_extensions',
)


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'falcon',
#         'USER': 'm',
#         'PASSWORD': '12'
#     }
# }

SECRET_KEY = 'REPLACE_ME'
