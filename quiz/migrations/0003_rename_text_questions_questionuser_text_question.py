# Generated by Django 4.0.3 on 2022-03-08 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_questionaryuser_alter_question_created_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionuser',
            old_name='text_questions',
            new_name='text_question',
        ),
    ]