#resume_upload
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('resume/', views.PersonView.as_view(), name='resume'),
    path('list/', views.PersonView.as_view(), name='list'),
    path('all/', views.PersonView.as_view(), name='all'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
