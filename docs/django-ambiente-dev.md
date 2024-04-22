DJANGO HowTo
-------------

1. Clonar o repositório:

```
$ git clone git@github.com:asbmails2/School-days-grupo3-eng-sw-unifesp.git

$ cd School-days-grupo3-eng-sw-unifesp/
```

2. Instalar [ambiente virtual Python](https://docs.python.org/3/library/venv.html) e o framework [Django](https://www.djangoproject.com/):

```
$ python3 -m venv venv

$ source venv/bin/activate

(venv) $ pip install django

(venv) $ python -m django --version
4.2.11
```

3. Criar o [projeto Django](https://docs.djangoproject.com/en/4.2/intro/tutorial01/#creating-a-project):

```
(venv) $ django-admin startproject schooldays

(venv) $ ls -F
LICENSE  README.md  docs/  schooldays/  venv/
```