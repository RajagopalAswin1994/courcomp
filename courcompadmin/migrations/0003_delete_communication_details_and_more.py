# Generated by Django 4.0.5 on 2022-06-23 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courcompadmin', '0002_communication_details_course_categories_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Communication_Details',
        ),
        migrations.DeleteModel(
            name='Course_Categories',
        ),
        migrations.DeleteModel(
            name='Course_Details',
        ),
        migrations.DeleteModel(
            name='Educational_Details',
        ),
        migrations.DeleteModel(
            name='Personal_details',
        ),
        migrations.DeleteModel(
            name='Registration_Details',
        ),
    ]
