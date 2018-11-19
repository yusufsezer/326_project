from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views import generic
from django.views.generic import RedirectView
from PlayWithMe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('search/', views.search, name='find_group'),
    path('results/', views.results, name='search_results'),
    path('my_groups/', views.my_groups, name='my_groups'),
    path('post_session/', views.post_session, name='create_group'),
    path('signup/', views.signup, name='signup'),
    path('session/<str:pk>', views.session_view, name='session'),
    path('join_session/<str:pk>', views.join_session, name='join_session'),
    path('create_online_session/', views.create_online_session, name='create_online_session'),
    path('create_local_session/', views.create_local_session, name='create_local_session'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [path("accounts/", include("django.contrib.auth.urls"))]
