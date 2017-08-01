from django.conf.urls import url
from django.contrib import admin
from .core.views import home
from .core.views import contato
from .core.views import enfermagem
from .core.views import instrumentacao
from .core.views import mapa
from .core.views import livres
from .core.views import fotos


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

