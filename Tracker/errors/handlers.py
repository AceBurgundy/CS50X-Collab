from flask import Blueprint
from Tracker.helpers import Apology

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(400)
def error_400(error):
    return Apology(code=error,title="Bad Request", message="The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."), 400

@errors.app_errorhandler(401)
def error_401(error):
    return Apology(code=error,title="Unauthorized", message="Although the HTTP standard specifies ""unauthorized"", semantically this response means ""unauthenticated"". That is, the client must authenticate itself to get the requested response."), 401

@errors.app_errorhandler(402)
def error_402(error):
    return Apology(code=error,title="Payment Required Experimental", message="This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists."), 402

@errors.app_errorhandler(403)
def error_403(error):
    return Apology(code=error,title="Forbidden", message="The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server."), 403

@errors.app_errorhandler(404)
def error_404(error):
    return Apology(code=error,title="Not Found", message="The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web"), 404

@errors.app_errorhandler(405)
def error_405(error):
    return Apology(code=error,title="Method Not Allowed", message="The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource."), 405

@errors.app_errorhandler(406)
def error_406(error):
    return Apology(code=error,title="Not Acceptable", message="This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent."), 406

@errors.app_errorhandler(407)
def error_407(error):
    return Apology(code=error,title="Proxy Authentication Required", message="This is similar to 401 Unauthorized but authentication is needed to be done by a proxy."), 407

@errors.app_errorhandler(408)
def error_408(error):
    return Apology(code=error,title="Request Timeout", message="This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message."), 408

@errors.app_errorhandler(409)
def error_409(error):
    return Apology(code=error,title="Conflict", message="This response is sent when a request conflicts with the current state of the server."), 409

@errors.app_errorhandler(410)
def error_410(error):
    return Apology(code=error,title="Gone", message="This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for ""limited-time, promotional services"". APIs should not feel compelled to indicate resources that have been deleted with this status code."), 410

@errors.app_errorhandler(411)
def error_411(error):
    return Apology(code=error,title="Length Required", message="Server rejected the request because the Content-Length header field is not defined and the server requires it."), 411

@errors.app_errorhandler(412)
def error_412(error):
    return Apology(code=error,title="Precondition Failed", message="The client has indicated preconditions in its headers which the server does not meet."), 412

@errors.app_errorhandler(413)
def error_413(error):
    return Apology(code=error,title="Payload Too Large", message="Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field."), 413

@errors.app_errorhandler(414)
def error_414(error):
    return Apology(code=error,title="URI Too Long", message="  The URI requested by the client is longer than the server is willing to interpret."), 414

@errors.app_errorhandler(415)
def error_415(error):
    return Apology(code=error,title="Unsupported Media Type", message="The media format of the requested data is not supported by the server, so the server is rejecting the request."), 415

@errors.app_errorhandler(416)
def error_416(error):
    return Apology(code=error,title="Range Not Satisfiable", message=" The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data."), 416

@errors.app_errorhandler(417)
def error_417(error):
    return Apology(code=error,title="Expectation Failed", message="This response code means the expectation indicated by the Expect request header field cannot be met by the server."), 417

@errors.app_errorhandler(418)
def error_418(error):
    return Apology(code=error,title="I'm a teapot", message=" The server refuses the attempt to brew coffee with a teapot."), 418

@errors.app_errorhandler(421)
def error_421(error):
    return Apology(code=error,title="Misdirected Request", message=" The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI."), 421

@errors.app_errorhandler(422)
def error_422(error):
    return Apology(code=error,title="Unprocessable Entity (WebDAV)", message="The request was well-formed but was unable to be followed due to semantic errors."), 422

@errors.app_errorhandler(423)
def error_423(error):
    return Apology(code=error,title="Locked (WebDAV)", message="The resource that is being accessed is locked."), 423

@errors.app_errorhandler(424)
def error_424(error):
    return Apology(code=error,title="Failed Dependency (WebDAV)", message="The request failed due to failure of a previous request."), 424

@errors.app_errorhandler(425)
def error_425(error):
    return Apology(code=error,title="Too Early Experimental", message="Indicates that the server is unwilling to risk processing a request that might be replayed."), 425

@errors.app_errorhandler(426)
def error_426(error):
    return Apology(code=error,title="Upgrade Required", message="The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s)."), 426

@errors.app_errorhandler(428)
def error_428(error):
    return Apology(code=error,title="Precondition Required", message=" The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict."), 428

@errors.app_errorhandler(429)
def error_429(error):
    return Apology(code=error,title="Too Many Requests", message=" The user has sent too many requests in a given amount of time (""rate limiting"")."), 429

@errors.app_errorhandler(431)
def error_431(error):
    return Apology(code=error,title="Request Header Fields Too Large", message="The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields."), 431

@errors.app_errorhandler(451)
def error_451(error):
    return Apology(code=error,title="Unavailable For Legal Reasons", message="The user agent requested a resource that cannot legally be provided, such as a web page censored by a government."), 451

                                    
                                    # ---------- Server Error Responses ---------- #

@errors.app_errorhandler(500)
def error_500(error):
    return Apology(code=error,title="Internal Server Error", message="The server has encountered a situation it does not know how to handle."), 500

@errors.app_errorhandler(501)
def error_501(error):
    return Apology(code=error,title="Not Implemented", message="The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD."), 501

@errors.app_errorhandler(502)
def error_502(error):
    return Apology(code=error,title="Bad Gateway", message="This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response."), 502

@errors.app_errorhandler(503)
def error_503(error):
    return Apology(code=error,title="Service Unavailable", message="The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached."), 503

@errors.app_errorhandler(504)
def error_504(error):
    return Apology(code=error,title="Gateway Timeout", message="This error response is given when the server is acting as a gateway and cannot get a response in time."), 504

@errors.app_errorhandler(505)
def error_505(error):
    return Apology(code=error,title="HTTP Version Not Supported", message="The HTTP version used in the request is not supported by the server."), 505

@errors.app_errorhandler(506)
def error_506(error):
    return Apology(code=error,title="Variant Also Negotiates", message="The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process."), 506

@errors.app_errorhandler(507)
def error_507(error):
    return Apology(code=error,title="Insufficient Storage (WebDAV)", message="The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request."), 507

@errors.app_errorhandler(508)
def error_508(error):
    return Apology(code=error,title="Loop Detected (WebDAV)", message="The server detected an infinite loop while processing the request."), 508

@errors.app_errorhandler(510)
def error_510(error):
    return Apology(code=error,title="Not Extended", message=" Further extensions to the request are required for the server to fulfill it."), 510

@errors.app_errorhandler(511)
def error_511(error):
    return Apology(code=error,title="Network Authentication Required", message="Indicates that the client needs to authenticate to gain network access."), 511

"""
Client error responses

400 Bad Request

    The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
401 Unauthorized

    Although the HTTP standard specifies "unauthorized", semantically this response means "unauthenticated". That is, the client must authenticate itself to get the requested response.
402 Payment Required Experimental

    This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists.
403 Forbidden

    The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server.
404 Not Found

    The server can not find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web.
405 Method Not Allowed

    The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource.
406 Not Acceptable

    This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent.
407 Proxy Authentication Required

    This is similar to 401 Unauthorized but authentication is needed to be done by a proxy.
408 Request Timeout

    This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message.
409 Conflict

    This response is sent when a request conflicts with the current state of the server.
410 Gone

    This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. The HTTP specification intends this status code to be used for "limited-time, promotional services". APIs should not feel compelled to indicate resources that have been deleted with this status code.
411 Length Required

    Server rejected the request because the Content-Length header field is not defined and the server requires it.
412 Precondition Failed

    The client has indicated preconditions in its headers which the server does not meet.
413 Payload Too Large

    Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field.
414 URI Too Long

    The URI requested by the client is longer than the server is willing to interpret.
415 Unsupported Media Type

    The media format of the requested data is not supported by the server, so the server is rejecting the request.
416 Range Not Satisfiable

    The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data.
417 Expectation Failed

    This response code means the expectation indicated by the Expect request header field cannot be met by the server.
418 I'm a teapot

    The server refuses the attempt to brew coffee with a teapot.
421 Misdirected Request

    The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI.
422 Unprocessable Entity (WebDAV)

    The request was well-formed but was unable to be followed due to semantic errors.
423 Locked (WebDAV)

    The resource that is being accessed is locked.
424 Failed Dependency (WebDAV)

    The request failed due to failure of a previous request.
425 Too Early Experimental

    Indicates that the server is unwilling to risk processing a request that might be replayed.
426 Upgrade Required

    The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s).
428 Precondition Required

    The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict.
429 Too Many Requests

    The user has sent too many requests in a given amount of time ("rate limiting").
431 Request Header Fields Too Large

    The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields.
451 Unavailable For Legal Reasons

    The user agent requested a resource that cannot legally be provided, such as a web page censored by a government.

Server error responses

500 Internal Server Error

    The server has encountered a situation it does not know how to handle.
501 Not Implemented

    The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD.
502 Bad Gateway

    This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response.
503 Service Unavailable

    The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached.
504 Gateway Timeout

    This error response is given when the server is acting as a gateway and cannot get a response in time.
505 HTTP Version Not Supported

    The HTTP version used in the request is not supported by the server.
506 Variant Also Negotiates

    The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process.
507 Insufficient Storage (WebDAV)

    The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request.
508 Loop Detected (WebDAV)

    The server detected an infinite loop while processing the request.
510 Not Extended

    Further extensions to the request are required for the server to fulfill it.
511 Network Authentication Required

    Indicates that the client needs to authenticate to gain network access.

"""
