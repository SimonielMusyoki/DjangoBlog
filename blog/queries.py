import graphene
from .types import AuthorType, PostType
from .models import Author, Post


class Query(graphene.ObjectType):
    feed = graphene.List(PostType)
    post = graphene.Field(PostType, postId=graphene.String())
    all_authors = graphene.List(AuthorType)
    author = graphene.Field(AuthorType, authorId=graphene.String())

    # Resolver for feed
    def resolve_feed(self, info):
        return Post.objects.all().order_by("-created_at")

    def resolve_post(self, info, postId):
        return Post.objects.get(id=postId)

    def resolve_all_authors(self, info):
        return Author.objects.all()

    def resolve_author(self, info, authorId):
        return Author.objects.get(id=authorId)
