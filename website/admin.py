from django.contrib import admin
from django.utils import timezone

from .models import MembershipApplication


@admin.register(MembershipApplication)
class MembershipApplicationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "email",
        "country",
        "status",
        "submitted_at",
        "reviewed_at",
    )
    list_filter = ("status", "country", "submitted_at")
    search_fields = ("full_name", "email", "phone", "country", "interests")
    ordering = ("-submitted_at",)
    readonly_fields = ("submitted_at", "reviewed_at")
    actions = ("approve_applications", "decline_applications")

    @admin.action(description="Approve selected membership applications")
    def approve_applications(self, request, queryset):
        queryset.update(status=MembershipApplication.Status.APPROVED, reviewed_at=timezone.now())

    @admin.action(description="Decline selected membership applications")
    def decline_applications(self, request, queryset):
        queryset.update(status=MembershipApplication.Status.DECLINED, reviewed_at=timezone.now())
