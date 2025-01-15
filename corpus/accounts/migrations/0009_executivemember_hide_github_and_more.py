# Generated by Django 5.1.3 on 2025-01-07 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='executivemember',
            name='hide_github',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='executivemember',
            name='hide_linkedin',
            field=models.BooleanField(default=False),
        ),
    ]