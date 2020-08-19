from django.contrib import admin
from .models import Programs, Category


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

    ordering = (
        'friendly_name',
    )


class ProgramsAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'title',
        'post_date',
    )

    ordering = (
        '-pk',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Programs, ProgramsAdmin)
