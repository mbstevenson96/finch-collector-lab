# Generated by Django 4.1.3 on 2022-11-10 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_finch_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feeding',
            name='finch',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main_app.finch'),
            preserve_default=False,
        ),
    ]
