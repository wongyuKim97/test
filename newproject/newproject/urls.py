from django.contrib import admin
from django.urls import path
import mm.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mm.views.home, name="home"),
    path('new/', mm.views.new, name="new"),
    path('ii/', mm.views.ii, name="ii"),
    path('i2/', mm.views.i2, name="i2"),   
]
