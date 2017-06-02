import datetime

from django.utils import timezone
from django.test import TestCase

from .models import Chore

class ChoreMethodTests(TestCase):

    def test_monthly_labor_hours_daily_chores(self):
        """
        monthly_labor_hours() for a daily chore of 30 minute duration should
        return the integer 900
        """
        daily_chore = Chore(occurance='1', 
                            duration_minutes=30)
        answer = int(900)
        question = daily_chore.monthly_labor_hours()
        self.assertEqual(question, answer)

    def test_monthly_labor_hours_weekly_chores(self):
        """
        monthly_labor_hours() for a chore that happens three times a week with
        a 30 minute duration should return the integer 360
        """
        weekly_chore = Chore(occurance='2', 
                             duration_minutes=30, 
                             days_weekly="0|1|4")
        answer = int(360)
        question = weekly_chore.monthly_labor_hours()
        self.assertEqual(question, answer)

    def test_monthly_labor_hours_monthly_chores(self):
        """
        monthly_labor_hours() for a monthly chore with a 30 minute duration
        should return the integer 30
        """
        monthly_chore = Chore(occurance='3', 
                              duration_minutes=30)
        answer = int(30)
        question = monthly_chore.monthly_labor_hours()
        self.assertEqual(question, answer)