# Generated by Django 4.1.3 on 2022-11-04 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_tag_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ['name'], 'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
    ]
