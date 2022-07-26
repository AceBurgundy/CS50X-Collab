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
        
@errors.app_errorhandler(400)
def error_400():
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."), 400

@errors.app_errorhandler(401)
def error_401(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="Although the HTTP standard specifies ""unauthorized"", semantically this response means ""unauthenticated"". That is, the client must authenticate itself to get the requested response."), 401

@errors.app_errorhandler(403)
def error_403(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server."), 403

@errors.app_errorhandler(404)
def error(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web"), 404

@errors.app_errorhandler(405)
def error_405(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource."), 405

@errors.app_errorhandler(406)
def error_406(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent."), 406

@errors.app_errorhandler(408)
def error_408(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message."), 408

@errors.app_errorhandler(409)
def error_409(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This response is sent when a request conflicts with the current state of the server."), 409

@errors.app_errorhandler(410)
def error_410(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for ""limited-time, promotional services"". APIs should not feel compelled to indicate resources that have been deleted with this status code."), 410

@errors.app_errorhandler(411)
def error_411(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="Server rejected the request because the Content-Length header field is not defined and the server requires it."), 411

@errors.app_errorhandler(412)
def error_412(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The client has indicated preconditions in its headers which the server does not meet."), 412

@errors.app_errorhandler(413)
def error_413(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field."), 413

@errors.app_errorhandler(414)
def error_414(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="  The URI requested by the client is longer than the server is willing to interpret."), 414

@errors.app_errorhandler(415)
def error_415(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The media format of the requested data is not supported by the server, so the server is rejecting the request."), 415

@errors.app_errorhandler(416)
def error_416(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=" The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data."), 416

@errors.app_errorhandler(417)
def error_417(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This response code means the expectation indicated by the Expect request header field cannot be met by the server."), 417

@errors.app_errorhandler(418)
def error_418(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=" The server refuses the attempt to brew coffee with a teapot."), 418

@errors.app_errorhandler(422)
def error_422(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The request was well-formed but was unable to be followed due to semantic errors."), 422

@errors.app_errorhandler(423)
def error_423(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The resource that is being accessed is locked."), 423

@errors.app_errorhandler(424)
def error_424(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The request failed due to failure of a previous request."), 424

@errors.app_errorhandler(428)
def error_428(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=" The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict."), 428

@errors.app_errorhandler(429)
def error_429(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message=" The user has sent too many requests in a given amount of time (""rate limiting"")."), 429

@errors.app_errorhandler(431)
def error_431(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields."), 431

@errors.app_errorhandler(451)
def error_451(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The user agent requested a resource that cannot legally be provided, such as a web page censored by a government."), 451

                                    
                                    # ---------- Server Error Responses ---------- #

@errors.app_errorhandler(500)
def error_500(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The server has encountered a situation it does not know how to handle."), 500

@errors.app_errorhandler(501)
def error_501(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD."), 501

@errors.app_errorhandler(502)
def error_502(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response."), 502

@errors.app_errorhandler(503)
def error_503(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached."), 503

@errors.app_errorhandler(504)
def error_504(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="This error response is given when the server is acting as a gateway and cannot get a response in time."), 504

@errors.app_errorhandler(505)
def error_505(error):
    return render_template("apology.html", code=str(error).split()[0],title=error_title(error), message="The HTTP version used in the request is not supported by the server."), 505
