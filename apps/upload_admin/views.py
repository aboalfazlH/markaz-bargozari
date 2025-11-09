from django.views.generic import TemplateView
from django.http import JsonResponse
    
class AdminPageView(TemplateView):
    template_name = "admin_page.html"
    