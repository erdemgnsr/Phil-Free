from django.db import models

# Create your models here.

class Lessons(models.Model):
    title = models.CharField(max_length = 1000,verbose_name="Lesson Name")
    speaker_name = models.CharField(max_length = 1000,verbose_name="Speaker Name")
    content = models.TextField(verbose_name = "Content")
    published_date = models.DateTimeField(verbose_name="Published Date")
    lesson_date = models.DateTimeField(blank=True, null=True, verbose_name="Lesson Date")
    is_ended = models.BooleanField(verbose_name="Is Ended")
    youtube_link = models.URLField(blank=True, max_length=200, verbose_name="Link")
    speaker_image = models.FileField(blank=True,null=True,verbose_name="Speaker Photo")
    is_published = models.BooleanField(default=0, verbose_name="Is Published")
    def __str__(self):
        return self.title

