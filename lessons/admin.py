from django.contrib import admin
from .models import Lessons

# Register your models here.
#admin.site.register(Projects)
@admin.register(Lessons)
class LessonsAdmin(admin.ModelAdmin):
    list_display = ["title","is_ended","speaker_name","is_published"]
    list_display_links = ["title", "is_ended"]
    search_fields = ["title","speaker_name"]
    list_filter = ["is_ended"]
    class Meta:
        model = Lessons