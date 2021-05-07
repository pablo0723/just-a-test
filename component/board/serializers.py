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
        todos = TodoTask.objects.filter(board=board)
        if self.context.get('request').path.endswith('boards/'):
            return todos.count()
        return TodoTaskSerializer(todos, many=True).data


class TodoTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = TodoTask
        fields = [
            'id',
            'name',
            'done'
        ]
