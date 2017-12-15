# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-13 16:13
from __future__ import unicode_literals

from django.db import migrations

import requests

GITLAB_API = 'https://eur0c.laas.fr/api/v4'

def gitlab(apps, schema_editor):
    Project, License, Package, Repo = (apps.get_model('gepetto_packages', model)
                                       for model in ['Project', 'License', 'Package', 'Repo'])
    for data in requests.get(f'{GITLAB_API}/projects', verify=False).json():
        package_qs = Package.objects.filter(name=data['name'])
        if package_qs.exists():
            Repo.objects.create(package=package_qs.first(), url=data['web_url'], repo_id=data['id'])


class Migration(migrations.Migration):

    dependencies = [
        ('gepetto_packages', '0002_github'),
    ]

    operations = [
        migrations.RunPython(gitlab),
    ]
