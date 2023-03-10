# Generated by Django 3.2.2 on 2023-02-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AnkaraClothing', '0004_offer'),
    ]

    operations = [
        migrations.CreateModel(
            name='bestseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_names', models.CharField(max_length=100)),
                ('descriptions', models.TextField(default='')),
                ('image', models.ImageField(upload_to='images/')),
                ('image_two', models.ImageField(blank=True, upload_to='images/')),
                ('image_three', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.IntegerField(default=0)),
                ('previous_price', models.IntegerField()),
                ('slug', models.SlugField(default='offer', max_length=100)),
            ],
        ),
        migrations.RenameModel(
            old_name='protector',
            new_name='USB_drive',
        ),
    ]
