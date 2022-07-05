
from flask import render_template

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code

def Search(list,search):   
    try:        
        index = indexOf(list, search)
        if index:
            return True
    except:
            return False

def save_picture(form_picture):
    random_value = secrets.token_hex(8)
    # fileName = "_"
    _, fileExtension = os.path.splitext(form_picture.filename)
    profilePictureFileName = random_value + fileExtension
    picture_path = os.path.join(app.root_path, 'static/profile_pictures', profilePictureFileName)

    outputSize = (125,125)
    
    i = Image.open(form_picture)
    i.thumbnail(outputSize)
    i.save(picture_path)
        
    return profilePictureFileName