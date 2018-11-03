from django.urls import path
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import RedirectView
from PlayWithMe import views


# urlpatterns = [
#     path("", views.index, name="index"),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home/', include('PlayWithMe.urls')),
    # path('', RedirectView.as_view(url='/home/')),
    path('', views.index, name='index'),
    path('search/', views.search, name='find_group'),
    path('results/', views.results, name='search_results'),
    path('chat/', views.chat, name='my_groups'),
    path('post_session/', views.post_session, name='create_group'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
