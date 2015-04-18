from django.conf.urls import include, url
from django.contrib import admin

from app.views import IndexView , InicioView

urlpatterns = [
    # Examples:
     
     url(r'^$', IndexView.as_view()),
     url(r'^inicio/', InicioView.as_view()),
         # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
