# Generated by Django 3.2.6 on 2021-09-04 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210904_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apply',
            name='Period',
            field=models.IntegerField(default=6),
        ),
        migrations.AlterField(
            model_name='apply',
            name='admission_no',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='apply',
            name='email_address',
            field=models.EmailField(max_length=254),
        ),
    ]