# Generated by Django 5.0.7 on 2024-08-09 01:46

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityConditionModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('condition', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'turntable_activity_condition',
            },
        ),
        migrations.CreateModel(
            name='TurnTableModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('activity_name', models.CharField(max_length=100)),
                ('turntable_name', models.CharField(max_length=100)),
                ('blocks_number', models.IntegerField(validators=[django.core.validators.MinValueValidator(3), django.core.validators.MaxValueValidator(20)])),
                ('turntable_setting', models.JSONField()),
                ('participate_condition', models.IntegerField(choices=[(1, 'registration success'), (2, 'login per day'), (3, 'reach VIP level'), (4, 'recharge success')])),
                ('vip_level', models.IntegerField(null=True)),
                ('home_tab', models.BooleanField()),
                ('tab_order', models.IntegerField()),
                ('support_language', models.JSONField()),
                ('share_language', models.BooleanField()),
                ('reward_currency', models.CharField(max_length=20)),
                ('reward_init_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reward_available_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('init_num', models.IntegerField()),
                ('interval', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(60)])),
                ('interval_per_inc_num', models.IntegerField()),
                ('interval_total_inc_num', models.IntegerField()),
                ('invite_people_num', models.IntegerField()),
                ('invite_people_per_inc_num', models.IntegerField()),
                ('invite_people_total_inc_num', models.IntegerField()),
                ('invite_people_valid_charge_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('invite_people_valid_betting_num', models.IntegerField()),
                ('invite_people_valid_betting_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('self_per_inc_num', models.IntegerField()),
                ('self_total_inc_num', models.IntegerField()),
                ('self_charge_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('self_betting_num', models.IntegerField()),
                ('self_betting_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cycle', models.IntegerField(choices=[(1, 'once'), (2, 'every day'), (3, 'every week')])),
                ('status', models.IntegerField()),
                ('expired', models.BooleanField()),
                ('expired_days', models.IntegerField()),
                ('expired_hours', models.IntegerField()),
                ('expired_minutes', models.IntegerField()),
                ('expired_handler', models.IntegerField()),
                ('create_time', models.DateTimeField(default=datetime.datetime(2024, 8, 9, 9, 46, 37, 756139))),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'turntable_activity_manage',
                'ordering': ['tab_order', 'create_time'],
            },
        ),
    ]
