import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    FLASK_RUN_PORT = os.environ.get('FLASK_RUN_PORT')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLAlchemy 1.4 no longer supports url strings that start with 'postgres'
    # (only 'postgresql') but heroku's postgres add-on automatically sets the
    # url in the hidden config vars to start with postgres.
    # so the connection uri must be updated here (for production)
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL').replace('postgres://', 'postgresql://')
    SQLALCHEMY_ECHO = True
    # ✅ Session & CSRF cookie config
    # SESSION_COOKIE_SAMESITE = "None" if os.environ.get("FLASK_ENV") == "production" else "Lax"
    # SESSION_COOKIE_SECURE = os.environ.get("FLASK_ENV") == "production"
    if os.environ.get("FLASK_ENV") == "production":
        SESSION_COOKIE_SAMESITE = "None"
        SESSION_COOKIE_SECURE = True
    else:
        SESSION_COOKIE_SAMESITE = "Lax"
        SESSION_COOKIE_SECURE = False
