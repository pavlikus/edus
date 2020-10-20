import graphene

from graphene_django.types import DjangoObjectType

from sorl.thumbnail import get_thumbnail

from .models import Course, Teacher


class CourseType(DjangoObjectType):
    
    url = graphene.String(source='get_absolute_url')
    
    def resolve_logo(self, *args, **kwargs):
        return get_thumbnail(self.logo, '220x180').url

    class Meta:
        model = Course


class TeacherType(DjangoObjectType):
    
    full_name = graphene.String(source='full_name')
    avatar = graphene.List(graphene.String)
    
    def resolve_avatar(self, *args, **kwargs):
        return [self.avatar.url,
                get_thumbnail(self.avatar, '360x360', crop='center').url,
                get_thumbnail(self.avatar, '220x220', crop='center').url]

    class Meta:
        model = Teacher


class Query(graphene.ObjectType):

    courses = graphene.List(CourseType, limit=graphene.Int())
    teachers = graphene.List(TeacherType, limit=graphene.Int())

    def resolve_courses(self, *args, **kwargs):
        if 'limit' in kwargs:
            return Course.objects.all()[:kwargs['limit']]
        return Course.objects.all()
