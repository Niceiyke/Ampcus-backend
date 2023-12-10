from django.contrib import admin

# Register your models here.
from . import models


class LoanAdmin(admin.ModelAdmin):
    list_display = (
        "member",
        "loan_type",
        "borrowed_amount",
        "repaid_amount",
        "is_active",
        "is_approved",
    )
    list_filter = (
        "is_active",
        "is_approved",
        "is_tresurer_approved",
        "is_president_approved",
        "is_tresurer_declined",
        "is_president_declined",
        "is_user_declined",
        "is_declined",
    )
    search_fields = (
        "member__user__first_name",
        "member__user__last_name",
        "loan_type__name",
    )
    date_hierarchy = "date_initiated"
    ordering = ["date_initiated"]


# Register your models here.
admin.site.register(models.LoanType)
admin.site.register(models.Comment)
admin.site.register(models.Loan, LoanAdmin)
admin.site.register(models.LoanRepayment)
admin.site.register(models.HomeAppliance)
admin.site.register(models.FoodItem)
admin.site.register(models.LoanApprovalQueue)
admin.site.register(models.LoanAwaitingDisbursmentQueue)
