from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from .models import CustomUser


class UserLoginView(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("home")

    def get_success_url(self):
        return self.success_url


class UserRegisterView(CreateView):
    template_name = "user/register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    model = CustomUser

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        # Superadmin users should not see the team name field
        if self.request.user.is_authenticated and self.request.user.is_superuser:
            form.fields.pop("team_name")
        return form


class UserLogoutView(LogoutView):
    next_page = reverse_lazy("login")
