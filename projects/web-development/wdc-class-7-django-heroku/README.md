# Django ❤️ Heroku

**This app is live on Heroku. Check it out: [https://wdc-class-7-django-heroku.herokuapp.com/](https://wdc-class-7-django-heroku.herokuapp.com/)**

This app serves as an example of how to deploy a simple Django app using heroku (including Database, static files, etc).

## Local Development

To make it work locally:

```bash
$ mkvirtualenv django-heroku -p /usr/bin/python3
$ pip install requirements.txt
$ django-admin migrate --settings coinmarketcap.settings.dev --pythonpath coinmarketcap
$ django-admin runserver --settings coinmarketcap.settings.dev --pythonpath coinmarketcap
```

## Heroku Deployment

There are just a few files to modify in order to make it work in Heroku. They're ready to go live, so just check the changes we've made:

* `settings/prod.py`: we're reading the database configuration with `dj_database_url`. We've also added `whitenoise` as the `STATICFILES_STORAGE`.
* `Procfile` & `runtime.txt`: Heroku configurations
* `requirements.txt`: These libraries will be installed automatically by heroku.
* `coinmarketcap/wsgi.py`: We've surrounded the default Django `application` with `DjangoWhiteNoise`.

### Steps to deploy
_(You need to install the [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli) and login in your console using the `heroku login` command)_

**Django app - Base setup**
```bash
# Create the app
$ heroku create wdc-class-7-django-heroku
# Set Django ENV_VARS
$ heroku config:set PYTHONPATH=coinmarketcap
$ heroku config:set DJANGO_SETTINGS_MODULE=coinmarketcap.settings.prod
```

**Initial deploy**

```bash
$ git push heroku master
```

**Migrate Database**

```bash
$ heroku run django-admin migrate
```

**Create superuser**

```bash
$ heroku run django-admin createsuperuser
```

**Import cryptos using the command**

```bash
$ heroku run django-admin shell
# paste the content of import-sample-data.py
```

**Showing logs**

```bash
$ heroku logs --tail
```
