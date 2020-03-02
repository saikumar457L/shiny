from django.urls import path
from . import views

urlpatterns = [
    path("",views.HomePageView.as_view(),name="welcome"),
    path("about/",views.AboutPageView.as_view(),name="about"),
    path("detail/",views.DetailPageView.as_view(),name="detail"),

]
