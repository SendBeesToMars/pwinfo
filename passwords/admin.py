from django.contrib import admin

from .models import Option, Website


class ChoiceInline(admin.TabularInline):
    model = Option
    max_num = 1


class WebsiteAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ('website_name', "date_added")
    list_filter = ['date_added']
    search_fields = ['website_name']

admin.site.register(Website, WebsiteAdmin)