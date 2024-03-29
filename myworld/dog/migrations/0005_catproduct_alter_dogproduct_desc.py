# Generated by Django 4.1.1 on 2022-12-11 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0004_dogproduct_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catproduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='static/images')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('desc', models.TextField(default='SOME STRING')),
            ],
            options={
                'verbose_name_plural': 'Cat_Products',
            },
        ),
        migrations.AlterField(
            model_name='dogproduct',
            name='desc',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
