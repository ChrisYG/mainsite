from django.views.generic.detail import DetailView
from django.shortcuts import render
from django.http import Http404
from aspc.folio.models import Page

def page_view(request, slug_path):
    '''slug_path: ^(?P<slug_path>(?:[\w\-\d]+/)+)$ '''
    slug_parts = slug_path.rstrip('/').split('/')
    pages = Page.objects.all()
    for part in slug_parts:
        try:
            new_page = pages.get(slug=part)
        except Page.DoesNotExist:
            raise Http404
        else:
            pages = new_page.page_set.all()
    
    return render(request, "folio/page.html", {
        "title": new_page.title,
        "body": new_page.body, 
        "page": new_page,
        "active_section": new_page.path()[0].slug,
        "active_section_root": new_page.section_root,
    })

from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = "temp_home.html"
    def get_context_data(self):
        context = super(HomeView, self).get_context_data()
        context["all_nav"] = True
        return context