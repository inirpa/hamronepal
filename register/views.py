from django.shortcuts import render
from django.views import generic

from . models import Site

# Create your views here.

class UnescoIndex(generic.ListView):
	template_name = 'unescosites/index.html'
	context_object_name = 'all_sites'

	def get_queryset(self):
		return Site.objects.all()
		