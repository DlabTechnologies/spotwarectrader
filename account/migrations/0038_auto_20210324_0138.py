# Generated by Django 3.0.5 on 2021-03-24 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0037_delete_userwithdrawrequestothermethod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactform',
            old_name='subject',
            new_name='company_name',
        ),
    ]
