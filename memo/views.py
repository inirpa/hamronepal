from django.shortcuts import render
from django.views import generic

# Create your views here.
class MemoView(generic.ListView):
	template_name = 'memo/index.html'

	def get_queryset(self):
		return 1