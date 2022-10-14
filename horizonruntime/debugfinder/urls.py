from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    path('server_status', views.server_status, name='ss'),
    path('search', views.search, name='search'),
    path('docs', views.docs_index, name='docs_index'),
    path('bookstore_home', views.bookstore_page, name='bookstore_home'),
    path('<int:bookstore_id>', views.bookstore_sep, name='bookstore_id_name')
] 