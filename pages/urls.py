from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('Pricing', views.Pricing, name="Pricing"),
    path('services', views.services, name="services"),
    path('Portrait',views.Portrait, name="Portrait"),
    path('Wedding',views.Wedding, name="Wedding"),
    path('Fashion',views.Fashion, name="Fashion"),
    path('Baby',views.Baby, name="Baby"),
    path('maternity',views.maternity, name="maternity"),
    path('PreWedding',views.PreWedding, name="PreWedding"),
    path('video',views.video, name="video"),
    path('Booking',views.Booking, name="Booking"),
]
