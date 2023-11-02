# `djarter` – An opinionated Django starter project

I have spent six years resisting the urge to make a starter template because (a) it locks you in to a particular development style, and (b) it prevents repetition which promotes learning.

But in the spirit of getting things done, this repo contains a few best practices and useful tools for Django projects.

These features would take a while to get set up from scratch, and might not be worth it for every project. But cloning this starter template can save you roughly a full day of work.

Most importantly, though, no Bootstrap styling was used in the making of this template.

## How to use `djarter`

### Make a copy of the template

Click the green "Use this template" button on the repository page. This creates a shallow copy, making a new repository with a single commit under your account.

### Setup the database

The template is ready to use SQLite for your database out of the box.

```shell
python manage.py migrate
```

### Create a superuser

```shell
python manage.py createsuperuser
```

### Run the tests

```shell
python manage.py test
```

### Run the development server

```shell
python manage.py runserver
```

### Customizations

Then, here are some areas you'll likely want to customize:

- [ ] `pyproject.toml` contains project info
- [ ] `static/style.css` has customizable CSS variables at the top of the file
- [ ] Edit your site name in the Django sites framework from within the admin at http://127.0.0.1:8000/backside; this value is used when sending password reset emails
- [ ] `cp .env-example .env` and adjust values
- [ ] Update the meta description and keywords in `templates/base.html`

## Features included

- Custom user model in at `users.CustomUser` with tests
- A test which checks if there are migrations to run
- Template directory in `BASE_DIR / "templates"`
- Templates for authentication URLs in `templates/registration/`
- A header template partial
- A base template
- Plain old CSS, powered by
  - [Every Layout](https://every-layout.dev/) primitives
  - CSS variables for colors and spacing
  - ZERO @media queries 🙌
  - ZERO Bootstrap
  - ZERO TailwindCSS
- [`pip-tools`](https://github.com/jazzband/pip-tools) for managing dependencies
- [`.editorconfig`](https://editorconfig.org/) to give your editor or IDE some guidelines
- `.env` enabled through the [`environs`](https://pypi.org/project/environs/) package
- [`django-allauth`](https://github.com/pennersr/django-allauth), which can set up social authentication
- [`django-watchfiles`](https://github.com/adamchainz/django-watchfiles) for lower CPU usage when running the development server
- [`pre-commit`](https://pre-commit.com/) for a bunch of useful formatting and linting
  - [`black`](https://github.com/psf/black)
  - [`isort`](https://pycqa.github.io/isort/)
  - [`flake8`](https://flake8.pycqa.org/en/latest/)
  - [`pyupgrade`](https://github.com/asottile/pyupgrade)
  - [`django-upgrade`](https://github.com/adamchainz/django-upgrade)
  - [`djhtml`](https://github.com/rtts/djhtml)
  - [`curlylint`](https://www.curlylint.org/)

## Other Django starters you might like

- [`DjangoX`](https://github.com/wsvincent/djangox)
- [`Cookiecutter Django`](https://github.com/pydanny/cookiecutter-django)
- [`django-template`](https://github.com/michael-awe/django-template)
- [`django-starter`](https://github.com/AlTosterino/django-starter)
