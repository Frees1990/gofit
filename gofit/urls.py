from django.contrib import admin
from django.urls import path, include
from django.conf import settings 
from django.conf.urls.static import static
from django.conf.urls import handler403, handler404
from gofit import views

# Assign Custom Error Handlers
handler403 = 'gofit.views.handler403'
handler404 = 'gofit.views.handler404'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('about/', include('about.urls')),
    path('products/', include('products.urls')),
    path('gallery/', include('gallery.urls')),
    path('bag/', include('bag.urls')),
    path('checkout/', include('checkout.urls')),
    path('profile/', include('profiles.urls')),
    path('membership/', include('membership.urls')),
    path('fitness_classes/', include('fitness_class.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
