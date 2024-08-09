from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

# Create your models here.

CONDITIONS_CHOICES = {
    1: "registration success",
    2: "login per day",
    3: "reach VIP level",
    4: "recharge success"
}

CYCLE_CHOICES = {
    1: "once",
    2: "every day",
    3: "every week"
}


class TurnTableModel(models.Model):
    id = models.AutoField(primary_key=True)
    activity_name = models.CharField(max_length=100)
    turntable_name = models.CharField(max_length=100)
    blocks_number = models.IntegerField()
    turntable_setting = models.JSONField()
    participate_condition = models.IntegerField()
    vip_level = models.IntegerField(null=True)
    home_tab = models.BooleanField()
    tab_order = models.IntegerField()
    support_language = models.JSONField()
    share_language = models.BooleanField()
    reward_currency = models.CharField(max_length=100)
    reward_init_amount = models.DecimalField(max_digits=10, decimal_places=2)
    reward_available_amount = models.DecimalField(max_digits=10, decimal_places=2)
    init_num = models.IntegerField()
    interval = models.IntegerField()
    interval_per_inc_num = models.IntegerField()
    interval_total_inc_num = models.IntegerField()
    invite_people_num = models.IntegerField()
    invite_people_per_inc_num = models.IntegerField()
    invite_people_total_inc_num = models.IntegerField()
    invite_people_valid_charge_amount = models.DecimalField(max_digits=10, decimal_places=2)
    invite_people_valid_betting_num = models.IntegerField()
    invite_people_valid_betting_amount = models.DecimalField(max_digits=10, decimal_places=2)
    self_per_inc_num = models.IntegerField()
    self_total_inc_num = models.IntegerField()
    self_charge_amount = models.DecimalField(max_digits=10, decimal_places=2)
    self_betting_num = models.IntegerField()
    self_betting_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cycle = models.IntegerField()
    status = models.IntegerField()
    expired = models.BooleanField()
    expired_days = models.IntegerField()
    expired_hours = models.IntegerField()
    expired_minutes = models.IntegerField()
    expired_handler = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.activity_name

    class Meta:
        ordering = ["tab_order", "create_time"]
        db_table = "turntable_activity_manage"


class ActivityConditionModel(models.Model):
    id = models.AutoField(primary_key=True)
    condition = models.CharField(max_length=100)

    def __str__(self):
        return self.condition

    class Meta:
        db_table = "turntable_activity_condition"
