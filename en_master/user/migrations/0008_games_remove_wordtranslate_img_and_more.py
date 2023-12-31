# Generated by Django 4.2.7 on 2023-11-28 15:37

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_alter_imggame_img_alter_profile_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Games',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_question', models.CharField(default='', max_length=250, verbose_name='Наводящий вопрос')),
                ('img', models.ImageField(blank=True, upload_to='user/images/ImgGame/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=('png', 'jpg', 'jpeg'))], verbose_name='Картинка для ImgGame')),
            ],
            options={
                'verbose_name': 'Игра',
                'verbose_name_plural': 'Игры',
            },
        ),
        migrations.RemoveField(
            model_name='wordtranslate',
            name='img',
        ),
        migrations.RemoveField(
            model_name='wordtranslate',
            name='lead_question',
        ),
        migrations.DeleteModel(
            name='ImgGame',
        ),
        migrations.DeleteModel(
            name='WordGame',
        ),
        migrations.AddField(
            model_name='wordtranslate',
            name='games',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.games'),
        ),
    ]
