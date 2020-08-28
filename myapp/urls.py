from django.contrib import admin
from django.urls import path,include
admin.autodiscover()
admin.site.site_header = 'To Do App | admin'
admin.site.site_title = 'To Do App | admin'

admin.site.index_title = 'To Do App administration'
admin.empty_value_display = '**Empty**'

urlpatterns = [
    path(r'', include('todoapp.urls')),
    path('admin/', admin.site.urls),
]