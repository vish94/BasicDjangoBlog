# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import articles.models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20151118_1947'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='thumbnail',
            field=models.FileField(default=b'', upload_to=articles.models.get_upload_file_name),
        ),
    ]
