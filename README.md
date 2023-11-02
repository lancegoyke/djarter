# `djarter` – An opinionated Django starter project

Main features:

- Custom User model with auth views
- Every Layout CSS primitives (no Bootstrap!)
- Formatters and linters configured with pre-commit
- and [more](#features)

For more explanation, see [Why make a template?](#why-make-a-template) below.

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
- [ ] Alter the main menu in `templates/partials/header.html`
- [ ] Install [`pre-commit`](https://pre-commit.com/)
- [ ] `pre-commit install` to register your Git Hook to run the pre-commit formatters, linters, and checks

## Features

- Custom user model in at `users.CustomUser` with tests
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

I have spent six years resisting the urge to make a starter template because (a) it locks you in to a particular development style, and (b) it prevents repetition which promotes learning.

But in the spirit of deploying high quality work, this repo contains a few best practices and useful tools for Django projects.

These features would take a while to get set up from scratch, and might not be worth it for every project. But cloning this starter template can save you roughly a full day of work.

Most importantly, though, no Bootstrap styling was used in the making of this template.

### Style

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

#### Styling

When left to my own devices, I find I'm likely to *over*design, meaning a make something too complicated and too messy to be pretty.

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

##### Accessibility of interactive elements, e.g., links and buttons

Links should be underlined to make them more accessible.

Hover states are noted with a simple opacity change.

## Other Django starters you might like

- [`DjangoX`](https://github.com/wsvincent/djangox)
- [`Cookiecutter Django`](https://github.com/pydanny/cookiecutter-django)
- [`django-template`](https://github.com/michael-awe/django-template)
- [`django-starter`](https://github.com/AlTosterino/django-starter)
