import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def text_response(request):
    """
    Return a HttpResponse with a simple text message.
    Check that the default content type of the response must be "text/html".
    """

    return HttpResponse('This is a simple text message!')


def looks_like_json_response(request):
    """
    Return a HttpResponse with a text message containing something that looks
    like a JSON document, but it's just "text/html".
    """
    
    return HttpResponse('{"json": "but its not really json"}')


def simple_json_response(request):
    """
    Return an actual JSON response by setting the `content_type` of the HttpResponse
    object manually.
    """
    return HttpResponse('{"json": "real json son"}', content_type="application/json")


def json_response(request):
    """
    Return the same JSON document, but now using a JsonResponse instead.
    """
    content = {"json": "real json son"}
    return JsonResponse(content)


def json_list_response(request):
    """
    Return a JsonReponse that contains a list of JSON documents
    instead of a single one.
    Note that you will need to pass an extra `safe=False` parameter to
    the JsonResponse object it order to avoid built-in validation.
    https://docs.djangoproject.com/en/2.0/ref/request-response/#jsonresponse-objects
    """
    content = [{"Reptile": "Snake"}, {"Mammal": "Dolphin"}]
    return JsonResponse(content, safe=False)


def json_error_response(request):
    """
    Return a JsonResponse with an error message and 400 (Bad Request) status code.
    """
    content = {'status': 'error 400', 'message': 'Bad Request, get a good one!'}
    return JsonResponse(content, status=400)


@csrf_exempt
def only_post_request(request):
    """
    Perform a request method check. If it's a POST request, return a message saying
    everything is OK, and the status code `200`. If it's a different request
    method, return a `400` response with an error message.
    """
    if request.method == "POST":
        content = {'status': 'Everything is OK!'}
        return JsonResponse(content)
    content = {'status': 'Everything is NOT OK!'}
    return JsonResponse(content, status=400)


@csrf_exempt
def post_payload(request):
    """
    Write a view that only accepts POST requests, and processes the JSON
    payload available in `request.body` attribute.
    """
    if request.method != "POST":
        return JsonResponse(
            {"status": False, "message": "We only support POST!"}, status=400)
    
    try:
        payload = json.loads(request.body.decode('utf-8'))
    except ValueError: 
        return JsonResponse(
            {"status": False, "message": "Not a valid json payload"}, status=400)
            
    if not payload:
        message = "We did not receive anything!"
    else: 
        message = "We received your message of: {}".format(dict(payload))
    return JsonResponse({"status": True, "message": message})
        


def custom_headers(request):
    """
    Return a JsonResponse and add a custom header to it.
    """
    content = {"status": "True"}
    content["custom"] = "header"
    return JsonResponse(content)


def url_int_argument(request, first_arg):
    """
    Write a view that receives one integer parameter in the URL, and displays it
    in the response text.
    """
    return JsonResponse(
        {"status": True, "message": "Your message is {}".format(first_arg)})


def url_str_argument(request, first_arg):
    """
    Write a view that receives one string parameter in the URL, and displays it
    in the response text.
    """
    return JsonResponse(
        {"status": True, "message": "Your message is {}".format(first_arg)})


def url_multi_arguments(request, first_arg, second_arg):
    """
    Write a view that receives two parameters in the URL, and display them
    in the response text.
    """
    return JsonResponse(
        {"status": True, 
         "message": "Your message is {} and {}".format(first_arg, second_arg)})


def get_params(request):
    """
    Write a view that receives GET arguments and display them in the
    response text.
    """
    arguments = request.GET 
    
    if not arguments:
        message = "Please include parameter arguments"
    else:
        message = "Thank you for these parameter arguments: {}".format(arguments.dict())
    
    return JsonResponse({"status": True, "message": message})
