from .base import * #NOQA

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE' : 'django.db.backends.mysql',
        'NAME' : 'blog',
        'USER' : 'root',
        'PASSWORD' : '123456',
        'HOST' : '47.95.1.144',
        'PORT' : '6788',
        'CHARSET' : 'utf8',  
    }
}

