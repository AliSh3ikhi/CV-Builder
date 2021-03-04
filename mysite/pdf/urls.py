from django.urls import path
from . import views

app_name = 'pdf'

urlpatterns = [
    path('',views.CreateProfile.as_view(),name='create_profile'),
    path('<int:pk>/',views.ProfileDetailView.as_view(),name='profile_detail'),
    path('<int:pk>/download/',views.create_pdf,name='download'),
]
