from django.contrib import admin
from django.urls import path

#need album view here
#admin just for demo
urlpatterns = [
    path('admin/', admin.site.urls),
]