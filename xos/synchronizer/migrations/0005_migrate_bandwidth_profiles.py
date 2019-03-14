# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-14 22:35
from __future__ import unicode_literals

import core.models.xosbase_header
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    def forwards(apps, schema_editor):
        # create a default bandwidth profile
        Model = apps.get_model('rcord', 'BandwidthProfile')
        bp = Model(
            name="default",
            cir=10000,
            cbs=10000,
            eir=10000,
            ebs=10000,
            air=10000,
        )
        bp.save()

        # assign the default bandwidth profile to all subscribers
        subscribers = apps.get_model('rcord', 'RCORDSubscriber')

        for s in subscribers.objects.all():
            s.downstream_bps = bp
            s.upstream_bps = bp
            s.save()

    dependencies = [
        ('rcord', '0004_bandwidth_profiles'),
    ]

    operations = [
        migrations.RunPython(forwards),
    ]
