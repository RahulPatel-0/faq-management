# Generated by Django 4.2.11 on 2025-02-01 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faqs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_bn',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='faq',
            name='answer_hi',
            field=models.TextField(blank=True, null=True),
        ),
    ]
