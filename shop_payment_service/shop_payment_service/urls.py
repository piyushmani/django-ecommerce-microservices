from django.urls import path, include
from django.contrib import admin
from rest_framework.documentation import include_docs_urls
from payment import urls as url_payment
API_TITLE = 'PAYMENT SERVICE'
API_DESCRIPTION = 'A Web API Description for PAYMENT SERVICE'



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(url_payment)),
    
    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]