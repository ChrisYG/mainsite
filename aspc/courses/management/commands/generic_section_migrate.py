from django.core.management.base import BaseCommand
from aspc.courses.models import Section, GenericSection


AREAS_URL = settings.COURSE_API_URL + 'courseareas'

class Command(BaseCommand):
    args = ''
    help = 'Create generic sections from sections and initialize their ratings'

    def handle(self, *args, **options):
        sections = Section.objects.all()
        for section in sections:
            for instructor in section.instructors.all():
                generic, created = GenericSection.objects.get_or_create(course=section.course, instructor=instructor)
                section.generic = generic
                section.save()
