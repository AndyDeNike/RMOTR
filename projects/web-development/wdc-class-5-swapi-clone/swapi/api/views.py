import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Planet, People
from api.fixtures import SINGLE_PEOPLE_OBJECT, PEOPLE_OBJECTS
from api.serializers import serialize_people_as_json


def single_people(request):
    return JsonResponse(SINGLE_PEOPLE_OBJECT)


def list_people(request):
    return JsonResponse(PEOPLE_OBJECTS, safe=False)


@csrf_exempt
def people_list_view(request):
    """
    People `list` actions:

    Based on the request method, perform the following actions:

        * GET: Return the list of all `People` objects in the database.

        * POST: Create a new `People` object using the submitted JSON payload.

    Make sure you add at least these validations:

        * If the view receives another HTTP method out of the ones listed
          above, return a `400` response.

        * If submited payload is nos JSON valid, return a `400` response.
    """
    if request.body:
        try:
            #https://www.geeksforgeeks.org/byte-objects-vs-string-python/
            payload = json.loads(request.body.decode('utf-8'))
            
        except ValueError:
            return JsonResponse({"success": False, 
            "message": "Please provide valid Json"}, status=400)
    
    status = 200
    if request.method=='GET':
        people = People.objects.all()
        data = [serialize_people_as_json(people) for people in people]
        
    elif request.method=='POST':
        planet_id = payload.get('homeworld', None)
        try:
            personal_planet = Planet.objects.get(id=planet_id)
        except DoesNotExist:
            return JsonResponse({"success": False, 
                "message": "That planet doesn't exist!"}, status=400)
        
        try:
            person = People.objects.create(
                    name = payload['name'],
                    homeworld = personal_planet,
                    height = payload['height'],
                    hair_color = payload['hair_color'],
                    mass = payload['mass']
                )
        except (ValueError, KeyError):
            return JsonResponse({"success": False, "message": "Invalid payload!"},
                status=400)
            
        data = serialize_people_as_json(person)
        status = 201
    
    else:
        status = 400
        return JsonResponse({"success": False, 
        "message": "Only GET/POST requests are accepted!"}, status)
    
    return JsonResponse(data, safe=False, status=status)


@csrf_exempt
def people_detail_view(request, people_id):
    """
    People `detail` actions:

    Based on the request method, perform the following actions:

        * GET: Returns the `People` object with given `people_id`.

        * PUT/PATCH: Updates the `People` object either partially (PATCH)
          or completely (PUT) using the submitted JSON payload.

        * DELETE: Deletes `People` object with given `people_id`.

    Make sure you add at least these validations:

        * If the view receives another HTTP method out of the ones listed
          above, return a `400` response.

        * If submited payload is nos JSON valid, return a `400` response.
    """
    try:
        person = People.objects.get(id=people_id)
    except People.DoesNotExist:
        return JsonResponse(
            {"success": False, "msg": "Could not find people with id: {}".format(people_id)},
            status=404)
    
    if request.body:
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return JsonResponse({"success": False, 
            "message": "Please provide valid Json"}, status=400)
    
    status=200  
    if request.method=='GET':
        pass
    
    elif request.method in ['PATCH', 'PUT']:
        for field in ['name', 'homeworld', 'height', 'mass', 'hair_color']:
            if field not in payload:
                if request.method == 'PATCH':
                    continue 
                else:
                    return JsonResponse({"success": False,
                        "message": "Field missing! PUT requires all fields present"
                    })
            
            if field == 'homeworld':
                try:
                    payload['homeworld'] = Planet.objects.get(id=payload['homeworld'])
                except Planet.DoesNotExist:
                    return JsonResponse({"success": False,
                    "message": "That planet doesn't exist!"}, status=400)
            
             
            try:
                setattr(person, field, payload[field])
                person.save()
            except ValueError:
                return JsonResponse(
                    {"success": False, "msg": "Provided payload is not valid"},
                    status=400)


    data = serialize_people_as_json(person)
    
    return JsonResponse(data, safe=False, status=status)
