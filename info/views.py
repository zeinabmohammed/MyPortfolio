

from django.shortcuts import render, redirect

from django.views.generic.base import TemplateView

from .models import *

class homepage(TemplateView):
	template_name = "index.html"
	def get_context_data(self, **kwargs):
		context = super(homepage, self).get_context_data(**kwargs)
		context['About'] = About.objects.all()
		context['Experience'] = Experience.objects.order_by('date')
		context['Projects'] = Project.objects.all().order_by('-id')
		context['CV'] = CV.objects.all()
		return context