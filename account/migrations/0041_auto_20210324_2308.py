# Generated by Django 3.0.5 on 2021-03-24 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0040_auto_20210324_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_type', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=300)),
                ('company_name', models.CharField(max_length=400)),
                ('phone', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ContactFormBank',
        ),
        migrations.DeleteModel(
            name='ContactFormBroker',
        ),
        migrations.DeleteModel(
            name='ContactFormCryptoExchange',
        ),
    ]
