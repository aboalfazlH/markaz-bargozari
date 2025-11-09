from django.urls import path
from .views import AdminPageView

app_name = 'user-admin'

urlpatterns = [
    path('',AdminPageView.as_view(),name="admin-page")
]