from django import template
import math
from django.utils.safestring import mark_safe
from aspc.settings import STATIC_URL

register = template.Library()

@register.filter
def star(rating):
    num_star_on = int(math.floor(rating))
    num_star_half = int(round(rating)) - num_star_on
    num_star_off = 5 - num_star_on - num_star_half

    html = num_star_on * ('<img height=15 src="'+STATIC_URL+'images/star-filled.png">') + \
        num_star_half * ('<img height=15 src="'+STATIC_URL+'images/star-half.png">') + \
        num_star_off * ('<img height=15 src="'+STATIC_URL+'images/star-empty.png">')
    return mark_safe(html)

@register.filter
def grade(rating):
    grades = dict([(1, u'A'), (2, u'A-'), (3, u'B+'), (4, u'B'), (5, u'B-'), (6, u'C+'), (7, u'C'),
    (8, u'C-'), (9, u'D+'), (10, u'D'), (11, u'D-'), (12, u'F')])
    return grades[rating]