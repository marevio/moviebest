from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('register/', views.Register, name='register'),
    path('login/', views.Register, name='login')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
