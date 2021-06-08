from django.urls import path

from django.views.generic import TemplateView

urlpatterns = [

path(
        route='<str:username>/',
        view=TemplateView.as_view(template_name='users/detail.html'),
        name='detail_user'
    ),

]