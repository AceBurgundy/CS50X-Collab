
import os
import secrets
from flask import render_template
from Tracker import app
from PIL import Image

def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message), code

def save_picture(form_picture):
    random_value = secrets.token_hex(8)
    file_name, file_extension = os.path.splitext(form_picture.filename)
    new_file_name = random_value + file_extension
    file_path = os.path.join(app.root_path, 'static/profile_pictures', new_file_name)
    
    output_size = (125,125)
    image = Image.open(form_picture)
    image.thumbnail(output_size)
    image.save(file_path)
    
    return new_file_name