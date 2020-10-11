"""edus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from edus_app.views import Index, AccountLoginView, AccountLogoutView
from contacts.views import ContactView


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('courses/', include('courses.urls')),
    path('teachers/', include('members.urls', namespace='teachers')),
    path('contact/', ContactView.as_view(), name='contact'),
    #path('students/', include('members.urls', namespace='students')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
