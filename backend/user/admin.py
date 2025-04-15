from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Team


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("name", "team_name")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "team_name",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    list_display = ("email", "name", "team_name", "is_staff")
    search_fields = ("email", "name", "team_name")
    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Team)
class TeamNameAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)
