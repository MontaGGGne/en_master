# Generated by Django 4.2.6 on 2023-10-24 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_alter_wordtranslate_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('surname', models.CharField(default='', max_length=50, verbose_name='Имя')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('avatar', models.ImageField(height_field=100, upload_to='static/user/img', width_field=100)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Users',
        ),
    ]
