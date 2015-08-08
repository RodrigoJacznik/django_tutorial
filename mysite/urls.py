from django.conf.urls import include, url
from django.contrib import admin

# Django compara la url del request con todas las regexp desde la 
# primera a la ultima (el orden importa).
# Cuando machea la url, invoca el view y le pasa como primer arg
# un objeto HttpRequest y si la regexp tiene algun valor "capturado",
# tambien se lo pasa, el valor capturado puede ser posicional o "nombrado".
# El include incluye (valga la redundancia) las urls definidas en la app
# polls. El namespace es util para reverse url lookup en el caso de que se
# tengan muchas apps y pueda existir colisiones de nombres de urls. ver
# /polls/templates/polls/index.html

urlpatterns = [
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
