
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'jagd'

urlpatterns = [
    path("add-boulder/", views.add_boulders_view, name="add_boulders_view"),
    path("ranking/", views.ranking_view, name="ranking_view"),
    path("view-boulder/", views.view_boulder, name="view_boulder"),
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_URL)