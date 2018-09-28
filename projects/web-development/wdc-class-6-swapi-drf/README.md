# SWAPI django-rest-framework

Do you remember [our previous project](https://github.com/rmotr-curriculum/wdc-class-5-swapi-clone) about cloning SWAPI? Well, today we will migrate the exact same functionality to use the amazing [django-rest-framework](http://www.django-rest-framework.org/) library. If you ever need to work with Django and RESTful APIs, this is probably the library you want to use. 💪

## 1) Setting up the environment

As we mentioned earlier, `django-rest-framework` is not part of Django's Core. It's an external library you need to install.

```bash
$ pip install djangorestframework==3.8.2
```

Note, version `3.8.2` is the latest at the moment of writing this file. Make sure to keep it updated to the last version for better compatibility.

## 2) What can DRF do for me?

If you remember from our previous project, we needed to define custom Django views to handle all the different action for the `People` model. That is: creating new objects, updating existing one, getting the list of all objects, getting the detail of one particular object, deleting objects, etc.

We needed to handle everything manually. That means, evaluate the request HTTP method, determine if it was a "detail" or "listing" view, looking up for the object / list of objects, handling the response status, content type, etc.

It's good to start in that way, because now we know all the internals about how a request/response lifecycle works. Now, wouldn't be great to have some abstraction layers on top that do some of the work for us? At the end, RESTful APIs follow always the same pattern and there must be some way of reusing functionality.

That's basically what `django-rest-framework` does for us. It implementes all the RESTful patterns in a very convenient way to use and extend, following all the good practices and conventions.

No more writing, let's jump right into it. 🙌

## 3) Doing some initial training

Following the same structure of the previous project, you will find a `training` Django App. To get started with `django-rest-framework`, take a look at the views we've proposed there and try to implement them using DRF resources.

It shouldn't take long. It's just scraping the surface of all that `django-rest-framrwork` can actually do.

You will notice that DRF comes with a very cool and stylish HTML template for interacting with its endpoints. It should look similar to this:

![image](https://user-images.githubusercontent.com/1155573/38947349-c455f4ca-4312-11e8-8f77-b444654f8560.png)

If you need to disable it, or you prefer to see the response in plain JSON format, you can always add a `?format=json` GET parameter to each request, and the response will automatically be returned as JSON.

## 4) Implementing SWAPI with DRF

We will implement SWAPI in three different ways:
1. using DRF's APIView classes. Splitting "detail" actions from "listing" actions into two different classes.

2. using DRF's ViewSet class. We will implement each action-related methods (ie: create, retrieve, delete, etc).

3. let DRF do the magic do us, and get all the logic implemented by using ModelViewSet class.

At the end, `django-rest-framework` will do most of the work for us. Unless you have a very complicated use case or data model (this is not the case), you won't probably need to implement things manually. It just plugging the right parts together and let DRF do the magic.

We suggest this progressive implementation on purpose. It's very cool to get all the functionality implemented for us magically, but you must know what's happening underneath. That's why we are moving from hardest to easiest, learning how the internal details of the workflow are, and once we understand it conceptually, we can delegate it to DRF so it can do it for us.

You should end up with something like this:

![image](https://user-images.githubusercontent.com/1155573/38947959-a8a08af4-4314-11e8-85b7-faf3a7aee76b.png)

Note that DRF ViewSets already provides a HTML interface to interact with the API, not only GETing objects but also POSTing and updating already saved instances.

## Final notes

Again, `django-rest-framework` is a very convenient way of implementing RESTful APIs using Django. What we've covered in this tutorial is just its basic functionality. We encourage you to read the [official documentation](http://www.django-rest-framework.org/#api-guide) to learn about more advances features, like authentication, permissions, versioning, etc.
