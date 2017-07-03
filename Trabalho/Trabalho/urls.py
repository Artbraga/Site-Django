from django.conf.urls import url
from django.contrib import admin
from Trabalho.core.views import home
from Trabalho.core.views import contato
from Trabalho.core.views import enfermagem
from Trabalho.core.views import instrumentacao
from Trabalho.core.views import mapa
from Trabalho.core.views import livres
from Trabalho.core.views import fotos


admin.autodiscover()
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^contato/$', contato, name='contato'),
    url(r'^enfermagem/$', enfermagem, name='enfermagem'),
    url(r'^instrumentacao/$', instrumentacao, name='instrumentacao'),
    url(r'^livres/$', livres, name='livres'),
    url(r'^mapa/$', mapa, name='mapa'),
    url(r'^fotos/$', fotos, name='fotos'),
    url(r'^admin/', admin.site.urls),
]

