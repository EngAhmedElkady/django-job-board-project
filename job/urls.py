from django.urls import path
from .import views
urlpatterns = [
    path('',views.job_list),
    path('<ind:id>',views.job_detail),
]