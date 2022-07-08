
from operator import indexOf
import os
import secrets
from turtle import width
from flask import render_template
from Tracker import app
from PIL import Image

def apology(message, code=400):
    """Render message as an apology to user."""
    return render_template("apology.html", top=code, bottom=message), code

def Search(list,search):   
    try:        
        index = indexOf(list, search)
        if index:
            return True
    except:
            return False

def save_picture(form_picture):
    i = Image.open(form_picture)
    
    width, height = i.size
    print(width,height)
    random_value = secrets.token_hex(8)
    # fileName = "_"
    _, fileExtension = os.path.splitext(form_picture.filename)
    profilePictureFileName = random_value + fileExtension
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', profilePictureFileName)
    outputSize = (125,125)
    
    # cropped = i.crop((500,100,500,500))

    if width > height:
        cropped = i.crop((400,100,1470,1100))
    else:
        cropped = i.crop((0,-(width/2),height,height)) #fix this shit tomorrow
    
    cropped.thumbnail(outputSize)
    cropped.save(picture_path)
    
    return profilePictureFileName