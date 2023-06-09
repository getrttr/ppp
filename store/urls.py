
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from products.views import index, products, email, login, profile, register
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('email/', email, name='email'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


