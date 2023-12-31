# Generated by Django 3.2.4 on 2023-09-04 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crms', '0003_auto_20230903_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalprojects',
            name='cipa_id',
            field=models.CharField(default=None, max_length=200, verbose_name='Enter CIPA Unique Identification Number (UIN) Without BW'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='projects',
            name='cipa_id',
            field=models.CharField(default=None, max_length=200, verbose_name='Enter CIPA Unique Identification Number (UIN) Without BW'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='historicalprimarycontactperson',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='historicalsecondarycontactperson',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='primarycontactperson',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='secondarycontactperson',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
    ]
