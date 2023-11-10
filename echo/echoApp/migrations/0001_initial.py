# Generated by Django 4.2.6 on 2023-10-28 10:48

from django.db import migrations, models
import django.db.models.deletion
import echoApp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Messenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255, validators=[echoApp.models.message_url_validator])),
                ('is_publish', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='echoApp.country')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(blank=True, max_length=150)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('username', models.CharField(blank=True, max_length=230, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=30, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Man'), ('W', 'Women')], default=None, max_length=255, null=True)),
                ('img', models.ImageField(blank=True, upload_to='user')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('publish_phone', models.BooleanField(default=False)),
                ('public_status', models.BooleanField(default=False)),
                ('region', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='echoApp.region')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
