# Generated by Django 3.0.5 on 2021-02-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='youtube_link',
            field=models.URLField(blank=True, verbose_name='Youtube Link'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='is_ended',
            field=models.BooleanField(verbose_name='Is Ended'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='lesson_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Lesson Date'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='published_date',
            field=models.DateTimeField(verbose_name='Published Date'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='speaker_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Speaker Photo'),
        ),
        migrations.AlterField(
            model_name='lessons',
            name='title',
            field=models.CharField(max_length=1000, verbose_name='Lesson Name'),
        ),
    ]
