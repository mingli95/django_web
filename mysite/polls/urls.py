from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^\?',views.auth,name='auth'),
    # url(r'^authlogin',views.authlogin,name='authlogin'),
    url(r'^$',views.login,name="login"),
    url(r'^login',views.login,name="login"),
    url(r'^index',views.index,name='index'),
    url(r'^flot',views.flot,name='flot'),
    url(r'^morris',views.morris,name='morris'),
    url(r'^tables',views.tables,name='tables'),
    url(r'^forms',views.forms,name='forms'),
    url(r'^panels-wells',views.panels_wells,name='panels_wells'),
    url(r'^buttons',views.buttons,name='buttons'),
    url(r'^notifications',views.notifications,name='notifications'),
    url(r'^typography',views.typography,name='typography'),
    url(r'^icons',views.icons,name='icons'),
    url(r'^grid',views.grid,name='grid'),
    url(r'^blank',views.blank,name='blank'),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)