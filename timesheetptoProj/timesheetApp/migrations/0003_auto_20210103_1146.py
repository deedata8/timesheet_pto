# Generated by Django 3.1.4 on 2021-01-03 18:46

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('timesheetApp', '0002_auto_20201231_1158'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='timesheet',
            name='employee_id',
        ),
        migrations.AddField(
            model_name='timesheet',
            name='employee',
            field=models.ForeignKey(default=26, on_delete=django.db.models.deletion.DO_NOTHING, to='auth.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='day_worked_hours',
            field=models.DecimalField(decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='hire_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='timesheet_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='timesheet',
            name='timesheet_stamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]