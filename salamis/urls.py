from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from salamis.settings import DEBUG, MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    # admin
    path('admin/', admin.site.urls),    
    # any
    path('', include('main.urls', namespace='main')),
    path('catalog/', include('goods.urls', namespace='catalog')),
    path('user/', include('users.urls', namespace='user')),
    path('cart/', include('carts.urls', namespace='cart')),
    path('orders/', include('orders.urls', namespace='orders')),



]
if DEBUG:
    urlpatterns += [path('__debug__/', include('debug_toolbar.urls'))]
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
