from django import forms
from .models import CustomUser, Team


class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password ", widget=forms.PasswordInput)
    team_name = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        required=False,
        widget=forms.Select(attrs={"class": "form-select"}),
        label="Team Name",
    )

    class Meta:
        model = CustomUser
        fields = ["email", "name", "team_name"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["team_name"].required = False

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if not user.is_superuser and not self.cleaned_data["team_name"]:
            raise forms.ValidationError(
                "Team name is required for non-superadmin users."
            )
        user.team_name = self.cleaned_data.get("team_name")
        if commit:
            user.save()
        return user
