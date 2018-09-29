**Before starting**

Install the [Heroku Toolbelt](https://devcenter.heroku.com/articles/heroku-cli) and login in your console:

```bash
$ heroku login
```

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
