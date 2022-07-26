from operator import indexOf
from flask import Blueprint, render_template

errors = Blueprint('errors', __name__, template_folder="templates/errors", static_folder="static/errors")

def error_title(error):
    array = []
    for word in str(error):
        if word == ":":
            break
        else:
            if not word.isnumeric():
                array.append(word)
    array[0] = ""
    return "".join(array)

def error_message(error):
    return "".join([str(error)[word] for word in range((indexOf([word for word in str(error)], ":")+2),len(str(error)))])
        
@errors.app_errorhandler(400)
def error_400(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 400

@errors.app_errorhandler(401)
def error_401(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 401

@errors.app_errorhandler(403)
def error_403(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 403

@errors.app_errorhandler(404)
def error_404(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 404

@errors.app_errorhandler(405)
def error_405(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 405

@errors.app_errorhandler(406)
def error_406(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 406

@errors.app_errorhandler(408)
def error_408(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 408

@errors.app_errorhandler(409)
def error_409(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 409

@errors.app_errorhandler(410)
def error_410(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 410

@errors.app_errorhandler(411)
def error_411(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 411

@errors.app_errorhandler(412)
def error_412(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 412

@errors.app_errorhandler(413)
def error_413(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 413

@errors.app_errorhandler(414)
def error_414(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 414

@errors.app_errorhandler(415)
def error_415(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 415

@errors.app_errorhandler(416)
def error_416(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 416

@errors.app_errorhandler(417)
def error_417(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 417

@errors.app_errorhandler(418)
def error_418(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 418

@errors.app_errorhandler(422)
def error_422(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 422

@errors.app_errorhandler(423)
def error_423(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 423

@errors.app_errorhandler(424)
def error_424(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 424

@errors.app_errorhandler(428)
def error_428(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 428

@errors.app_errorhandler(429)
def error_429(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 429

@errors.app_errorhandler(431)
def error_431(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 431

@errors.app_errorhandler(451)
def error_451(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 451

                                    
                                    # ---------- Server Error Responses ---------- #

@errors.app_errorhandler(500)
def error_500(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 500

@errors.app_errorhandler(501)
def error_501(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 501

@errors.app_errorhandler(502)
def error_502(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 502

@errors.app_errorhandler(503)
def error_503(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 503

@errors.app_errorhandler(504)
def error_504(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 504

@errors.app_errorhandler(505)
def error_505(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=error_message(error)), 505
