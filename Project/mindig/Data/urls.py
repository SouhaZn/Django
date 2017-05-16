from django.conf.urls import url, include
from django.contrib import admin
from Data.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'data', DatasetViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^mindig/', HomePageView.as_view()),
    url(r'^plate/', include('django_spaghetti.urls')),
    url(r'^api/', include(router.urls)),
]


"""urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eboutique.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

  #   url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
)
"""
