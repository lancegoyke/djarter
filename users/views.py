from django.contrib import messages
from django.contrib.auth import views
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic.edit import CreateView

from .forms import CustomUserCreationForm


class LoginView(views.LoginView):
    template_name = "registration/login.html"


class LogoutView(views.LogoutView):
    pass


class PasswordChangeView(views.PasswordChangeView):
    template_name = "registration/password_change_form.html"
    success_url = reverse_lazy("home")

    def get_success_url(self):
        """Add a success message and redirect"""
        messages.success(self.request, _("Password changed successfully"))
        return super().get_success_url()


class PasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = "registration/password_change_done.html"


# FLOW: Reset -> ResetSent -> ResetConfirm -> ResetComplete
class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"


class PasswordResetConfirmView(views.PasswordResetConfirmView):
    template_name = "registration/password_reset_confirm.html"
    success_url = reverse_lazy("accounts:password_reset_complete")


class PasswordResetSentView(views.PasswordResetDoneView):
    template_name = "registration/password_reset_sent.html"


class PasswordResetView(views.PasswordResetView):
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy("accounts:password_reset_sent")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("accounts:login")
    template_name = "registration/signup.html"
