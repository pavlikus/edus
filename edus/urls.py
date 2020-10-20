from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter

from edus_app.views import Index, AccountLoginView, AccountLogoutView
from contacts.views import ContactView
from courses.views import CourseAPIListView

from graphene_django.views import GraphQLView
from .schema import schema


router = DefaultRouter()
router.register('course', CourseAPIListView)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('courses/', include('courses.urls')),
    path('teachers/', include('members.urls', namespace='teachers')),
    path('contact/', ContactView.as_view(), name='contact'),
    path("graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
    #path('students/', include('members.urls', namespace='students')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
