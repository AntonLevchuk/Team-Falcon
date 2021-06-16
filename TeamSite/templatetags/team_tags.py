from django import template
from TeamSite.models import Tournaments

register = template.Library()


@register.simple_tag()
def get_tournament():
    return Tournaments.objects.order_by('-created_at')