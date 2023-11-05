from django import forms
from django.shortcuts import render


class ExampleForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100, required=True)
    email = forms.EmailField(label="Your email", max_length=100, required=True)
    message = forms.CharField(label="Your message", max_length=1000)
    is_retired = forms.BooleanField(
        label="Are you retired?",
        required=False,
        help_text="Optional",
    )
    country = forms.ChoiceField(
        label="Your country",
        choices=[
            ("US", "United States"),
            ("CA", "Canada"),
            ("MX", "Mexico"),
        ],
        widget=forms.RadioSelect,
    )
    homepage = forms.URLField(
        label="Your homepage",
        max_length=100,
        required=False,
        help_text="Optional",
    )
    number = forms.IntegerField(
        label="Your number",
        min_value=1,
        max_value=10,
        help_text="Select a number from 1 to 10",
    )
    birthday = forms.DateField(
        label="Your birthday",
        help_text="Select a date",
    )
    wake_up_time = forms.TimeField(
        label="Your preferred wake up time",
        help_text="Select a time",
    )
    event_start = forms.DateTimeField(
        label="Event start",
        help_text="Select a date and time",
    )
    tags = forms.MultipleChoiceField(
        label="Tags",
        choices=[
            ("python", "Python"),
            ("django", "Django"),
            ("javascript", "JavaScript"),
            ("react", "React"),
        ],
        help_text="Select one or more tags",
    )


def example_form(request):
    if request.method == "POST":
        form = ExampleForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return render(request, "example_form.html", {"form": form})
    else:
        form = ExampleForm()
    return render(request, "example_form.html", {"form": form})
