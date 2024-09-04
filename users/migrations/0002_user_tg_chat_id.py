# Generated by Django 5.1 on 2024-08-30 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="tg_chat_id",
            field=models.CharField(
                blank=True,
                help_text="Укажите телеграм chat-id",
                max_length=50,
                null=True,
                verbose_name="Телеграм chat-id",
            ),
        ),
    ]
