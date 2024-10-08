# Generated by Django 5.0.7 on 2024-09-15 16:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('languages', models.CharField(choices=[('abkhazian', 'Abkhazian'), ('afrikaans', 'Afrikaans'), ('albanian', 'Albanian'), ('amharic', 'Amharic'), ('arabic', 'Arabic'), ('armenian', 'Armenian'), ('assamese', 'Assamese'), ('azerbaijani', 'Azerbaijani'), ('bangla', 'Bangla'), ('basque', 'Basque'), ('belarusian', 'Belarusian'), ('bengali', 'Bengali'), ('bosnian', 'Bosnian'), ('bulgarian', 'Bulgarian'), ('burmese', 'Burmese'), ('catalan', 'Catalan'), ('cebuano', 'Cebuano'), ('chichewa', 'Chichewa'), ('chinese', 'Chinese'), ('croatian', 'Croatian'), ('czech', 'Czech'), ('danish', 'Danish'), ('dutch', 'Dutch'), ('english', 'English'), ('esperanto', 'Esperanto'), ('estonian', 'Estonian'), ('ewe', 'Ewe'), ('filipino', 'Filipino'), ('finnish', 'Finnish'), ('french', 'French'), ('georgian', 'Georgian'), ('german', 'German'), ('greek', 'Greek'), ('gujarati', 'Gujarati'), ('haitian creole', 'Haitian Creole'), ('hebrew', 'Hebrew'), ('hindi', 'Hindi'), ('hmong', 'Hmong'), ('hungarian', 'Hungarian'), ('indonesian', 'Indonesian'), ('irish', 'Irish'), ('italian', 'Italian'), ('japanese', 'Japanese'), ('javanese', 'Javanese'), ('kannada', 'Kannada'), ('kazakh', 'Kazakh'), ('khmer', 'Khmer'), ('korean', 'Korean'), ('kurdish', 'Kurdish'), ('lao', 'Lao'), ('latin', 'Latin'), ('latvian', 'Latvian'), ('lingala', 'Lingala'), ('lithuanian', 'Lithuanian'), ('luxembourgish', 'Luxembourgish'), ('macedonian', 'Macedonian'), ('malagasy', 'Malagasy'), ('malayalam', 'Malayalam'), ('marathi', 'Marathi'), ('moldovan', 'Moldovan'), ('mongolian', 'Mongolian'), ('nepali', 'Nepali'), ('norwegian', 'Norwegian'), ('nyanja', 'Nyanja'), ('odia', 'Odia'), ('oriya', 'Oriya'), ('pashto', 'Pashto'), ('persian', 'Persian'), ('polish', 'Polish'), ('portuguese', 'Portuguese'), ('punjabi', 'Punjabi'), ('quechua', 'Quechua'), ('romanian', 'Romanian'), ('russian', 'Russian'), ('rwaganda', 'Rwaganda'), ('serbian', 'Serbian'), ('sesotho', 'Sesotho'), ('shona', 'Shona'), ('sindhi', 'Sindhi'), ('sinhala', 'Sinhala'), ('slovak', 'Slovak'), ('slovene', 'Slovene'), ('somali', 'Somali'), ('spanish', 'Spanish'), ('swahili', 'Swahili'), ('swedish', 'Swedish'), ('tagalog', 'Tagalog'), ('tajik', 'Tajik'), ('tamil', 'Tamil'), ('telugu', 'Telugu'), ('thai', 'Thai'), ('tigrinya', 'Tigrinya'), ('turkish', 'Turkish'), ('ukrainian', 'Ukrainian'), ('urdu', 'Urdu'), ('uzbek', 'Uzbek'), ('vietnamese', 'Vietnamese'), ('yoruba', 'Yoruba'), ('zhuang', 'Zhuang'), ('zulu', 'Zulu')], max_length=100)),
                ('awards', models.CharField(blank=True, max_length=250, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='journalist', to=settings.AUTH_USER_MODEL)),
                ('specialization', models.ManyToManyField(to='journalists.specialization')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institute', models.CharField(max_length=250)),
                ('degree_type', models.CharField(max_length=250)),
                ('field_of_study', models.CharField(max_length=250)),
                ('start_year', models.DateField()),
                ('end_year', models.DateField()),
                ('journalist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='educations', to='journalists.journalist')),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('subscribed_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscribers', to='journalists.journalist')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('subscriber', 'subscribed_to')},
            },
        ),
    ]
