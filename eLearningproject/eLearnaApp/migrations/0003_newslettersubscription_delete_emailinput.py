# Generated by Django 5.0.7 on 2024-07-30 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eLearnaApp', '0002_emailinput_delete_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsletterSubscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='EmailInput',
        ),
    ]
