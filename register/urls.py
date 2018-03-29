from django.conf.urls import url
from . import views

urlpatterns = [
	url('^$',views.UnescoIndex.as_view(),name = 'unescoindex'),
]