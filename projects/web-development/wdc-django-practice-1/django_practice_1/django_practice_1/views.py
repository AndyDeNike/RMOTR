from datetime import datetime, timedelta

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest


# Use /hello-world URL
def hello_world(request):
    """Return a 'Hello World' string using HttpResponse"""
    return HttpResponse("Hello World")


# Use /date URL
def current_date(request):
    """
        Return a string with current date using the datetime library.

        i.e: 'Today is 5, January 2018'
    """
    today = datetime.now()
    return HttpResponse(today.strftime('Today is %d, %B, %Y'))


# Use URL with format /my-age/<year>/<month>/<day>
def my_age(request, year, month, day):
    """
        Return a string with the format: 'Your age is X years old'
        based on given /year/month/day datetime that come in the URL.

        i.e: /my-age/1992/1/20 returns 'Your age is 26 years old'
    """
    try:
        birthday = datetime(year=year, month=month, day=day)
    except ValueError:
        return HttpResponseBadRequest()
        
    difference = datetime.now() - birthday
    return HttpResponse("Your age is {} years old".format(round(difference.days/365, 2)))
        


# Use URL with format /next-birthday/<birthday>
def next_birthday(request, birthday):
    """
        Return a string with the format: 'Days until next birthday: XYZ'
        based on a given string GET parameter that comes in the URL, with the
        format 'YYYY-MM-DD'
    """
    try:
        #strptime transforms into datetime object w/ custom date attributes as 2nd parameter 
        bday = datetime.strptime(birthday, '%Y-%m-%d')
    except ValueError:
        return HttpResponseBadRequest()
    now = datetime.now()    
    current_bday = bday.replace(year=now.year)

    if bday < now:
        current_bday = current_bday.replace(year=current_bday.year+1)

    difference = current_bday - now
    
    return HttpResponse("Days until next birthday: {}".format(difference.days))


# Use /profile URL
def profile(request):
    """
        Render the 'profile.html' sending the context given below, using the
        'render' function imported from Django.
        Make sure to replace the values inside the template in the proper places.
    """
    me = {'name': 'Joonny Tohottie', 'age': 1230}
    return render(request, 'profile.html', context=me)



"""
    The goal for next task is to practice routing between two URLs.
    You will have:
        - /authors --> contains a list of Authors (template is provided to you)
        - /author/<authors_last_name> --> contains the detail for given author,
        using the AUTHORS_INFO provided below.

    First view just have to render the given 'authors.html' template sending the
    AUTHORS_INFO as context.

    Second view has to take the authors_last_name provided in the URL, look for
    for the proper author info in the dictionary, and send it as context while
    rendering the 'author.html' template. Make sure to complete the given
    'author.html' template with the data that you send.
"""
AUTHORS_INFO = {
    'poe': {
        'full_name': 'Edgar Allan Poe',
        'nationality': 'US',
        'notable_work': 'The Raven',
        'born': 'January 19, 1809',
    },
    'borges': {
        'full_name': 'Jorge Luis Borges',
        'nationality': 'Argentine',
        'notable_work': 'The Aleph',
        'born': 'August 24, 1899',
    }
}

# Use provided URLs, don't change them
def authors(request):
    return render(request, 'authors.html', context=AUTHORS_INFO)


def author(request, authors_last_name):
    return render(request, 'author.html', context=AUTHORS_INFO[authors_last_name])
