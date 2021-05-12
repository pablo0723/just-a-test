from rest_framework import serializers

from component.board.models import Board, TodoTask


class BoardSerializer(serializers.ModelSerializer):
    todos = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Board
        fields = [
            'id',
            'slug',
            'name',
            'todos',
        ]

    def get_todos(self, board):
        from component.board.views import BoardListCreateView
        if isinstance(self.context.get('view'), BoardListCreateView):
            return TodoTask.objects.filter(board=board).count()
        return TodoTaskSerializer(TodoTask.objects.filter(board=board), many=True).data


class TodoTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = [
            'id',
            'name',
            'done'
        ]
