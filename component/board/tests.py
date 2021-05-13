from rest_framework.test import APIClient, APITestCase

from component.board.models import Board, TodoTask
from component.board.serializers import BoardSerializer, TodoTaskSerializer


class TestBoardViews(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.board = Board.objects.create(name='test') #better use test fixtures
        self.todo = TodoTask.objects.create(board=self.board, name='Test Task')

    # GET TESTS
    def test_boards_get(self):
        response = self.client.get('/api/board/boards/')
        self.assertEqual(response.status_code, 200)
        boards = Board.objects.all()
        serializer = BoardSerializer(boards, many=True)
        self.assertEqual(response.json()['count'], len(serializer.data))

    def test_todos_get(self):
        response = self.client.get(f'/api/board/{self.board.slug}/todos/')
        self.assertEqual(response.status_code, 200)
        todo = TodoTask.objects.filter(board=self.board)
        serializer = TodoTaskSerializer(todo, many=True)
        self.assertEqual(response.json()['count'], len(serializer.data))
        self.assertEqual(response.json()['results'], serializer.data)

    def test_board_get(self):
        response = self.client.get(f'/api/board/boards/{self.board.id}/')
        self.assertEqual(response.status_code, 200)
        board = Board.objects.get(id=self.board.id)
        serializer = BoardSerializer(board)
        self.assertEqual(response.json(), serializer.data)

    def test_todo_get(self):
        response = self.client.get(f'/api/board/{self.board.slug}/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 200)
        board = TodoTask.objects.get(id=self.todo.id)
        serializer = TodoTaskSerializer(board)
        self.assertEqual(response.json(), serializer.data)

    # POST TEST
    def test_boards_post(self):
        response = self.client.post('/api/board/boards/', {'name': 'TEST 2'})
        self.assertEqual(response.status_code, 201)
        board = Board.objects.get(id=response.json()['id'])
        data = BoardSerializer(board).data
        data['todos'] = len(data['todos'])
        self.assertEqual(response.json(), data)

    def test_todos_post(self):
        response = self.client.post(f'/api/board/{self.board.slug}/todos/', {'board': self.board.id, 'name': 'Test 2'})
        self.assertEqual(response.status_code, 201)
        todo = TodoTask.objects.get(id=response.json()['id'])
        serializer = TodoTaskSerializer(todo)
        self.assertEqual(response.json(), serializer.data)

    # DELETE
    def test_board_delete(self):
        response = self.client.delete(f'/api/board/boards/{self.board.id}/')
        self.assertEqual(response.status_code, 204)

    def test_todo_delete(self):
        response = self.client.delete(f'/api/board/{self.board.slug}/todos/{self.todo.id}/')
        self.assertEqual(response.status_code, 204)