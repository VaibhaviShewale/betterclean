# Generated by Django 3.2.2 on 2021-10-22 05:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('betterclean', '0002_auto_20211022_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='staff',
            field=models.ForeignKey(blank=True, limit_choices_to={'is_active': True, 'is_staff': True, 'is_superuser': False}, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Staff'),
        ),
    ]
