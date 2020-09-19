from django.urls import path
from . import views
from credit import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('view/', views.view, name='view'),
    path('transfer/', views.transfer, name='transfer'),
    path('history/', views.history, name='history'),
    path('feedback/', views.feedback, name='feedback'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)