import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Chore

    name = models.CharField(max_length=63, null=True)
    description = models.CharField(max_length=150, null=True)
    duration_minutes = models.IntegerField(, null=True)
    occurance = field_details.OccuranceField(, null=True)
    days_weekly = field_details.DayOfTheWeekField(, null=True)
    #offers choices of long-written DOW and stores choices as single digits
    #https://stackoverflow.com/questions/5966629/django-days-of-week-representation-in-model
    date_monthly = models.CharField(max_length=2, null=True)
    by_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)

class ChoreMethodTests(TestCase):

    def test_monthly_labor_hours_daily_chores(self):
        """
        monthly_labor_hours() for a daily chore of 30 minute duration should
        return the integer 900
        """
        daily_chore = Chore(occurance='1', 
                            duration_minutes=30)
        self.assertIs(daily_chore.monthly_labor_hours(), 900)

    def test_monthly_labor_hours_weekly_chores(self):
        """
        monthly_labor_hours() for a chore that happens three times a week with
        a 30 minute duration should return the integer 360
        """
        weekly_chore = Chore(occurance='2', 
                             duration_minutes=30, 
                             days_weekly="0|1|4")
        self.assertIs(weekly_chore.monthly_labor_hours(), 360)

    def test_monthly_labor_hours_monthly_chores(self):
        """
        monthly_labor_hours() for a monthly chore with a 30 minute duration
        should return the integer 30
        """
        monthly_chore = Chore(occurance='3', 
                              duration_minutes=30)
        self.assertIs(monthly_chore.monthly_labor_hours(), 30)
