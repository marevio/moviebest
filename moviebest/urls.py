from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from movies import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('team/', views.aboutus, name='team'),
    path('contact/', views.contact, name='contact'),
    path('register/', views.Register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('detail/<movie_id>', views.detail, name='detail'),
    path('search/<movie_id>', views.search, name='search'),
    path('search_2/<movie_id>', views.search_2, name='search_2'),
    path('director/<movie_id>', views.director, name='director'),
    path('adv_search/', views.advSearch, name='adv_search')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
