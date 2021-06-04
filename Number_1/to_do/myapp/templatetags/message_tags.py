# Use datetime if not localizing timezones
import datetime
# Otherwise use timezone
from django.utils import timezone

from django import template

register = template.Library()


@register.filter
def hours_ago(time, hours):
    # or timezone.now() if your time is offset-aware
    # return time + datetime.timedelta(hours=hours) < datetime.datetime.now()
    # print(timezone.localtime(time))
    # print(timezone.now())
    # print(datetime.timedelta(hours=hours))
    print(time - timezone.now()+datetime.timedelta(hours=7) +
          datetime.timedelta(hours=24))
    return (time - timezone.now()+datetime.timedelta(hours=7) + datetime.timedelta(hours=24) < datetime.timedelta(hours=hours)) and (time - timezone.now()+datetime.timedelta(hours=7) + datetime.timedelta(hours=24) > datetime.timedelta(hours=0))


@register.filter
def hours_after(time, hours):
    # or timezone.now() if your time is offset-aware
    # return time + datetime.timedelta(hours=hours) < datetime.datetime.now()
    return -(time - timezone.now()+datetime.timedelta(hours=7) + datetime.timedelta(hours=24)) < datetime.timedelta(hours=hours)
