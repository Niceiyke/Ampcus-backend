from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    list_display = (
        "email",
        "first_name",
        "last_name",
        "sap_number",
        "is_active",
        "is_staff",
    )
    search_fields = ("email", "first_name", "last_name", "sap_number")
    readonly_fields = ("id", "date_joined_nb")

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            "Personal Info",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "sap_number",
                    "place_of_birth",
                    "state_of_origin",
                    "lga",
                    "marital_status",
                    "next_of_kin",
                    "phone_number",
                    "date_joined_nb",
                    "date_of_birth",
                    "currnent_grade",
                )
            },
        ),
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
                "fields": ("email", "password1", "password2", "is_active", "is_staff"),
            },
        ),
    )

    ordering = ("email",)


admin.site.register(CustomUser, CustomUserAdmin)
