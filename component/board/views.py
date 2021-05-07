from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


from component.board.models import Board, TodoTask
from component.board.serializers import BoardSerializer, TodoTaskSerializer


class BoardListCreateView(ListCreateAPIView):
    serializer_class = BoardSerializer
    permission_classes = [AllowAny] # Just for fast testing
    queryset = Board.objects.all()
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'name'
        'created'
    ]
    filterset_fields=[
        'name'
    ]


class BoardUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    permission_classes = [AllowAny] # Just for fast testing
    serializer_class = BoardSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'


class TodoListCreateView(ListCreateAPIView):
    serializer_class = TodoTaskSerializer
    permission_classes = [AllowAny] # Just for fast testing
    lookup_field = 'board__slug'
    lookup_url_kwarg = 'board'
    filter_backends = [
        SearchFilter,
        OrderingFilter,
        DjangoFilterBackend
    ]
    search_fields = [
        'name'
    ]
    ordering_fields = [
        'name'
        'created'
    ]
    filterset_fields=[
        'done'
    ]

    # can be change with Custom Filter and a custom DjangoFilterBackend ( so  FilterBackend will take kwargs.get('board'))
    def get_queryset(self):
        return TodoTask.objects.filter(board__slug=self.kwargs.get('board'))


class TodoUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = TodoTask.objects.all()
    permission_classes = [AllowAny] # Just for fast testing
    serializer_class = TodoTaskSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'id'

    def get_queryset(self):
        return TodoTask.objects.filter(board__slug=self.kwargs.get('board'))