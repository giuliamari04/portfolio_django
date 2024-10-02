from rest_framework import viewsets
from rest_framework import generics
from .models import Posts
from .serializers import PostSerializer
from .models import Technologies
from .serializers import TechnologieSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug' 
class TechnologieViewSet(viewsets.ModelViewSet):
    queryset = Technologies.objects.all()
    serializer_class = TechnologieSerializer
class PostDetailView(generics.RetrieveAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'  # Specifica che il campo da usare per cercare è lo slug
