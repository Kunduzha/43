
from webapp.views import first_view, second_view, third_view
from django.urls import path


urlpatterns = [

    path('hi/', first_view),
    path('2/', second_view),
    path('3/', third_view),


]
