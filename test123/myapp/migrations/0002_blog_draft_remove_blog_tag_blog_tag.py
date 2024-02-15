# Generated by Django 4.2.10 on 2024-02-15 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog", name="draft", field=models.BooleanField(default=True),
        ),
        migrations.RemoveField(model_name="blog", name="tag",),
        migrations.AddField(
            model_name="blog", name="tag", field=models.ManyToManyField(to="myapp.tag"),
        ),
    ]