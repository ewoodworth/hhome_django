from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import field_details

class Address(models.Model):
    """Addresses for users of website."""

    apartment = models.CharField(max_length=6, null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    standard_address = models.CharField(max_length=150, null=True)
    address_street_num = models.CharField(max_length=10, null=True)
    address_street = models.CharField(max_length=50, null=True)
    address_city = models.CharField(max_length=50, null=True)
    address_state = field_details.USStateField(null=True)
    address_zip = models.CharField(max_length=50, null=True)


    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Address address_id=%s address=%s>" % (self.address_id, self.standard_address)

class Chore(models.Model):
    """Chore model"""
    #ID is generated automatically
    name = models.CharField(max_length=63, null=True)
    description = models.CharField(max_length=150, null=True)
    duration_minutes = models.IntegerField(null=True)
    occurance = field_details.OccuranceField(null=True)
    days_weekly = field_details.DayOfTheWeekField(null=True)
    #offers choices of long-written DOW and stores choices as single digits
    #https://stackoverflow.com/questions/5966629/django-days-of-week-representation-in-model
    date_monthly = models.CharField(max_length=2, null=True)
    by_time = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
    # comment = models.CharField(max_length=15), nullable=True)

    class Meta:
        verbose_name = 'chore'
        ordering = ['name']

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Chore chore_id=%s name=%s>" % (self.id, self.name)

    def __str__(self):
        return "{}: {}".format(
            self.name,
            self.description)

    def monthly_labor_hours(self):
        """Returns time(min) per month for a given chore"""
        if self.occurance == '1':
            monthly_hours = self.duration_minutes * int(30)
        elif self.occurance == '2':
            monthly_hours = len(self.days_weekly.split("|")) * 4 * self.duration_minutes
        elif self.occurance == '3':
            monthly_hours = self.duration_minutes
        return (monthly_hours)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Contribution(models.Model):
    """User contribution to household labor"""
    user = models.ForeignKey(User)
    chore = models.ForeignKey(Chore)
    contribution = models.CharField(max_length=50, null=True)