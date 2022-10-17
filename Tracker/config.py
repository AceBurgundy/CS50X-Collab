class Config:
        # Ensure templates are auto-reloaded
    TEMPLATES_AUTO_RELOAD = True

    SECRET_KEY = 'Blackasdasdasdwq324535jf34f34f.'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///collab.db'
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Configure session to use filesystem (instead of signed cookies)
    SESSION_PERMANENT = False
    SESSION_TYPE = "filesystem"