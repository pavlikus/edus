import graphene

from courses.schema import Query as CourseQuery


class Query(CourseQuery, graphene.ObjectType):
    """Mixin class, include Course schema query"""


schema = graphene.Schema(query=Query)
