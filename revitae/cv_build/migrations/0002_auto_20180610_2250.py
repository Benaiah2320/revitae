# Generated by Django 2.0.6 on 2018-06-10 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv_build', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='resume',
            name='name',
        ),
        migrations.AddField(
            model_name='resume',
            name='first_name',
            field=models.CharField(default='Zach', max_length=100, verbose_name='First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resume',
            name='last_name',
            field=models.CharField(default='Sizemore', max_length=100, verbose_name='Last Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End Date'),
        ),
    ]
