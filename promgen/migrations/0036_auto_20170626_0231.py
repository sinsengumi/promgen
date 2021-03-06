# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-26 02:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def convert_to_service(apps, schema_editor):
    Rule = apps.get_model('promgen', 'Rule')
    Service = apps.get_model('promgen', 'Service')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    service_type = ContentType.objects.get_for_model(Service)

    for rule in Rule.objects.all():
        if rule.content_type_id == service_type.id:
            rule.service_id = rule.object_id
            rule.save()
        else:
            rule.delete()


def convert_to_content_type(apps, schema_editor):
    Rule = apps.get_model('promgen', 'Rule')
    Service = apps.get_model('promgen', 'Service')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    service_type = ContentType.objects.get_for_model(Service)
    for rule in Rule.objects.all():
        rule.object_id = rule.service_id
        rule.content_type_id = service_type.id
        rule.save()


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('promgen', '0035_rule_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='rule',
            name='content_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rule',
            name='object_id',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.RunPython(convert_to_content_type, convert_to_service),
        migrations.RemoveField(
            model_name='rule',
            name='service',
        ),
        migrations.AlterModelOptions(
            name='rule',
            options={'ordering': ['content_type', 'object_id', 'name']},
        ),
    ]
