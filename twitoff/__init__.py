'''Entry point to the Twitoff Flask application'''

from .app import create_app

# creates global variable for twitoff directory
APP = create_app()
