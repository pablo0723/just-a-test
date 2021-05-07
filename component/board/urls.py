from django.urls import path

from component.board.views import BoardListCreateView, BoardUpdateDeleteView, TodoListCreateView, TodoUpdateDeleteView

urlpatterns = [
    path(r'boards/', BoardListCreateView.as_view(), name='board-list-create'),
    path(r'boards/<int:id>/', BoardUpdateDeleteView.as_view(), name='board-rud'),
    path(r'<slug:board>/todos/', TodoListCreateView.as_view(), name='todos-list-create'),
    path(r'<slug:board>/todos/<int:id>/', TodoUpdateDeleteView.as_view(), name='todos-list-create'),
]
