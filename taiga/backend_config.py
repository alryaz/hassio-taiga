# -*- coding: utf-8 -*-
import os

from .common import *   # noqa, pylint: disable=unused-wildcard-import

#########################################
## GENERIC
#########################################

DEBUG = False

#ADMINS = (
#    ("Admin", "example@example.com"),
#)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ['POSTGRES_DB'],
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
        'HOST': os.environ['POSTGRES_HOST'],
        'PORT': '5432',
    }
}

SECRET_KEY = os.environ["TAIGA_SECRET_KEY"]

TAIGA_SITES_SCHEME = "https"
TAIGA_SITES_DOMAIN = "host_to_be_replaced"
FORCE_SCRIPT_NAME = os.environ["INGRESS_ENTRY"]

TAIGA_URL = f"{ TAIGA_SITES_SCHEME }://{ TAIGA_SITES_DOMAIN }{ FORCE_SCRIPT_NAME }"
SITES = {
        "api": { "name": "api", "scheme": TAIGA_SITES_SCHEME, "domain": TAIGA_SITES_DOMAIN },
        "front": { "name": "front", "scheme": TAIGA_SITES_SCHEME, "domain": f"{ TAIGA_SITES_DOMAIN }{ FORCE_SCRIPT_NAME }" }
}

# Setting DEFAULT_PROJECT_SLUG_PREFIX to false
# removes the username from project slug
DEFAULT_PROJECT_SLUG_PREFIX = False

#########################################
## MEDIA AND STATIC
#########################################

# MEDIA_ROOT = '/home/taiga/media'
MEDIA_URL = f"{ TAIGA_URL }/media/"
DEFAULT_FILE_STORAGE = "taiga_contrib_protected.storage.ProtectedFileSystemStorage"
THUMBNAIL_DEFAULT_STORAGE = DEFAULT_FILE_STORAGE

# STATIC_ROOT = '/home/taiga/static'
STATIC_URL = f"{ TAIGA_URL }/static/"

#########################################
## EMAIL
#########################################
# https://docs.djangoproject.com/en/3.1/topics/email/
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 120  # seconds

DEFAULT_FROM_EMAIL = 'changeme@example.com'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = True
EMAIL_HOST = 'localhost'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'user'
EMAIL_HOST_PASSWORD = 'password'

RABBITMQ_PASSWORD=os.environ['RABBITMQ_DEFAULT_PASS']
RABBITMQ_VHOST=os.environ['RABBITMQ_VHOST']

#########################################
## EVENTS
#########################################
EVENTS_PUSH_BACKEND = "taiga.events.backends.rabbitmq.EventsPushBackend"
EVENTS_PUSH_BACKEND_OPTIONS = {
    # "url": "amqp://taiga:rabbitmqpassword@rabbitmqhost:5672/taiga"
    "url": "amqp://taiga:" + RABBITMQ_PASSWORD + "@9547a9e0-rabbitmq:5672/" + RABBITMQ_VHOST
}


#########################################
## TAIGA ASYNC
#########################################
CELERY_ENABLED = os.getenv('CELERY_ENABLED', 'True') == 'True'

from kombu import Queue  # noqa

CELERY_BROKER_URL = "amqp://taiga:" + RABBITMQ_PASSWORD + "@9547a9e0-rabbitmq:5672/" + RABBITMQ_VHOST
CELERY_RESULT_BACKEND = None # for a general installation, we don't need to store the results
CELERY_ACCEPT_CONTENT = ['pickle', ]  # Values are 'pickle', 'json', 'msgpack' and 'yaml'
CELERY_TASK_SERIALIZER = "pickle"
CELERY_RESULT_SERIALIZER = "pickle"
CELERY_TIMEZONE = 'Europe/Madrid'
CELERY_TASK_DEFAULT_QUEUE = 'tasks'
CELERY_QUEUES = (
    Queue('tasks', routing_key='task.#'),
    Queue('transient', routing_key='transient.#', delivery_mode=1)
)
CELERY_TASK_DEFAULT_EXCHANGE = 'tasks'
CELERY_TASK_DEFAULT_EXCHANGE_TYPE = 'topic'
CELERY_TASK_DEFAULT_ROUTING_KEY = 'task.default'


#########################################
## CONTRIBS
#########################################
# INSTALLED_APPS += [
#     "taiga_contrib_slack",
#     "taiga_contrib_github_auth",
#     "taiga_contrib_gitlab_auth"
# ]
#
# GITHUB_API_CLIENT_ID = "changeme"
# GITHUB_API_CLIENT_SECRET = "changeme"
#
# GITLAB_API_CLIENT_ID = "changeme"
# GITLAB_API_CLIENT_SECRET = "changeme"
# GITLAB_URL = "changeme"


#########################################
## TELEMETRY
#########################################

ENABLE_TELEMETRY = False

#########################################
##  REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = False

#########################################
## THROTTLING
#########################################

#REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon-write": "20/min",
#    "user-write": None,
#    "anon-read": None,
#    "user-read": None,
#    "import-mode": None,
#    "import-dump-mode": "1/minute",
#    "create-memberships": None,
#    "login-fail": None,
#    "register-success": None,
#    "user-detail": None,
#    "user-update": None,
#}

# This list should contain:
#  - Taiga users IDs
#  - Valid clients IP addresses (X-Forwarded-For header)
#REST_FRAMEWORK["DEFAULT_THROTTLE_WHITELIST"] = []

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
#USER_EMAIL_ALLOWED_DOMAINS = None

# PUCLIC OR PRIVATE NUMBER OF PROJECT PER USER
#MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
#MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
#MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
#MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
#FRONT_SITEMAP_ENABLED = False
#FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
#FEEDBACK_ENABLED = True
#FEEDBACK_EMAIL = "support@taiga.io"


#########################################
## STATS
#########################################

#STATS_ENABLED = False
#STATS_CACHE_TIMEOUT = 60*60  # In second


#########################################
## IMPORTERS
#########################################

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
#IMPORTERS["github"] = {
#    "active": True,
#    "client_id": "XXXXXX_get_a_valid_client_id_from_github_XXXXXX",
#    "client_secret": "XXXXXX_get_a_valid_client_secret_from_github_XXXXXX"
#}

# Configuration for the Trello importer
# Remember to enable it in the front client too.
#IMPORTERS["trello"] = {
#    "active": True, # Enable or disable the importer
#    "api_key": "XXXXXX_get_a_valid_api_key_from_trello_XXXXXX",
#    "secret_key": "XXXXXX_get_a_valid_secret_key_from_trello_XXXXXX"
#}

# Configuration for the Jira importer
# Remember to enable it in the front client too.
#IMPORTERS["jira"] = {
#    "active": True, # Enable or disable the importer
#    "consumer_key": "XXXXXX_get_a_valid_consumer_key_from_jira_XXXXXX",
#    "cert": "XXXXXX_get_a_valid_cert_from_jira_XXXXXX",
#    "pub_cert": "XXXXXX_get_a_valid_pub_cert_from_jira_XXXXXX"
#}
