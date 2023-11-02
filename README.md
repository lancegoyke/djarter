# `djarter` – An opinionated Django starter project

![black](https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge)
![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge)

Main features:

- Custom User model with email, no username, includes auth views
- CSS layout primitives instead of CSS frameworks (no Bootstrap!)
- Formatters and linters configured with pre-commit
- and [more](#features)

For more explanation, see [Why make a template?](#why-make-a-template) below.

## How to use `djarter`

Overview:

1. "Use this template" on GitHub
1. `python -m venv .venv`
1. `source .venv/bin/activate` (Unix/Linux/Mac) or `.\.venv\Scripts\Activate.ps1` (Windows)
1. `python -m pip install -r requirements.txt`
1. `python manage.py migrate`
1. `python manage.py createsuperuser`
1. `python manage.py runserver`
1. [Customize](#customizations) for your project

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
- [ ] Alter the main menu in `templates/partials/header.html`
- [ ] Install [`pre-commit`](https://pre-commit.com/)
- [ ] `pre-commit install` to register your Git Hook to run the pre-commit formatters, linters, and checks

## Features

- Custom user model at `users.CustomUser` using unique emails and no username
- A test which checks if there are migrations to run
- Template directory in `BASE_DIR / "templates"`
- Templates for authentication URLs in `templates/registration/`
- A header template partial in `templates/partials/header.html`
- A base template in `templates/base.html`
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

## Why make a template?

I have spent six years resisting the urge to make a starter template because (a) it locks you in to a particular development style, and (b) it prevents the repetition that promotes learning.

But in the spirit of deploying high quality work, this repo contains a few best practices and useful tools for Django projects.

These features would take a while to get set up from scratch, and might not be worth it for every project. But cloning this starter template can save you roughly a full day of work if you're planning to extend the built-in user authentication.

Most importantly, though, no Bootstrap styling was used in the making of this template.

### Summary of usefulness

This template is likely useful to you if:

- your app requires non-admin user registration
- you want pre-commit enabled for code quality
- you want to avoid using CSS frameworks

### User Authentication

If your app doesn't require user registration, then this template is probably not exactly what you want.

#### The `CustomUser` model

There's a custom user model located at `users.models.CustomUser`.

For most projects, I find the `username` field unnecessary, so it is set to `None`.

Instead, the "username field" is set to `email`.

#### Social authentication and `django-allauth`

`django-allauth` is included because I often find myself using it to enable authentication with social media accounts.

Social authentication is not enabled by default.

#### Authentication views

I have found that I don't like using `django.contrib.auth` views or `allauth` views as they are set because I would prefer to customize the messages on these pages to fit the brand of the site.

As such, these views have been extended. See them in `users/views.py` and `users/urls.py`.

There is no "confirm logout" page. When clicking through to the logout view, the user is logged out and redirected to the home page. You can change with with the `success_url`.

Similarly, there is a success message when a password is changed, but the user is redirected to the home page. You can change the redirect with `success_url` and the message in `get_success_url()`.

### Style

First we will discuss [why this template isn't using a more popular `CSS` framework](#css-frameworks), then we will discuss [how you can use the included `CSS` to make this project your own](#styling-to-your-liking).

#### CSS frameworks

I have used packages like [`Bootstrap`](https://getbootstrap.com/), [`Bulma`](https://bulma.io/), and [`Tailwind`](https://tailwindcss.com/) in the past, and I like them, but I don't like using them. I feel like they make me spend a bunch of time learning a framework instead of learning **CSS**.

I used `Bootstrap`, and it was useful, but I didn't like the look.

So I used `Bulma`, which felt more unique and special, but I barely scratched the surface.

Then I tried `Tailwind`, and the intro course was great for training my eye for design, but it requires a ton of study to use it well. Plus, that HTML markup is _ugly_.

Enter, [Every Layout](https://every-layout.dev/), which taught me how to write CSS that didn't require `@media` queries. It teaches you layout, and only layout, instead of trying to break into the world of colors and animations. I've used a few of their layout primitives:

- Various layout rudiments including a modular scale and liberal use of `rem` for sizing that scales with browser magnification
- "cluster" for the main menu
- "box" for buttons, header, and more
- "center" for centering elements
- "stack" for vertical separation
- default styles for form elements

Again, these are all wonderful tools! But if you're comfortable with CSS, I think this is a better starting point.

#### Styling to your liking

When left to my own devices, I find I'm likely to *over*design, meaning a make something too complicated and too messy to be pretty.

In hopes of preventing this, here are some main ideas and simplifications regarding styling with this template.

- [Variables](#variables)
- [Main menu](#main-menu)
- [Modular scale](#modular-scale)
- [Unset most browser defaults](#unset-most-browser-defaults)
- [Buttons](#buttons)
- [Boxes](#boxes)
- [Accessibility of interactive elements](#accessibility-of-interactive-elements)

##### Variables

Included at the top of `style.css` are three color variables to change to suit your brand: `--color-light`, `--color-dark`, and `--color-accent`. The site aims to be roughly 60% light, 30% dark, and 10% accent a la [the 60-30-10 rule](https://www.google.com/search?q=60+30+10+rule).

##### Main menu

You can add and change items to the main menu. If they exceed available space, they will fall below the site title on the left hand side of the menu.

There is no hamburger menu to toggle and, therefore, no JavaScript for that behavior.

##### Modular scale

Below that is a modular scale that allows for spacing elements with a particular ratio. You should generally use these instead of hard-coding pixel values to dial in spacing.

##### Unset most browser defaults

After that, the `*` declaration sets some defaults. And shortly thereafter, some of these are unset if it makes sense.

##### Buttons

You can create buttons with:

- `<button>`
- `<a class="button">`
- `<a class="button bare">`

The first two are visually equivalent and will default to using your `--color-accent` for the background and `--color-light` for the text.

The third option looks like text but maintains button spacing.

See the "Log In" and "Forgot Password" buttons on the `/accounts/login/` page for an example of both styles.

##### Boxes

You can create boxes of information with:

- `<div class="box">`
- `<div class="box invert">`

##### Accessibility of interactive elements

Links should be underlined to make them more accessible.

Hover states are noted with a simple opacity change.

## Pull requests welcome

This project is still in its early stages. If you have any improvements you believe to be obvious, feel free to open an issue to discuss!

## Other Django starters you might like

- [`DjangoX`](https://github.com/wsvincent/djangox)
- [`Cookiecutter Django`](https://github.com/pydanny/cookiecutter-django)
- [`django-template`](https://github.com/michael-awe/django-template)
- [`django-starter`](https://github.com/AlTosterino/django-starter)
