# Generated by Django 5.0.7 on 2024-09-03 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_user_date_of_brith'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='date_of_brith',
            new_name='date_of_birth',
        ),
    ]
