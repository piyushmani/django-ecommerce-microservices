from django.contrib import admin
from django.urls import path, include
from userAuth import urls as url_user
from rest_framework.documentation import include_docs_urls 
from allauth.account.views import LoginView


API_TITLE = 'USER API'  
API_DESCRIPTION = 'A Web API Description for USER SERVICE'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(url_user)),
    path('accounts/login/', LoginView.as_view(), name='account_login'),

    path('', include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
]