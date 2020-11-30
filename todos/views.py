from rest_framework.exceptions import NotFound

from todos.firebase_client import FirebaseClient
from todos.serializers import TodoSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response


class TodoViewSet(viewsets.ViewSet):
    client = FirebaseClient()

    def create(self, request, *args, **kwargs):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.create(serializer.data)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED
        )

    def list(self, request):
        todos = self.client.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        todo = self.client.get_by_id(pk)

        if todo:
            serializer = TodoSerializer(todo)
            return Response(serializer.data)

        raise NotFound(detail="Todo Not Found", code=404)

    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        self.client.delete_by_id(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.client.update(pk, serializer.data)

        return Response(serializer.data)
