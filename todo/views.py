from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status

from todo.models import ToDo
from todo.serializers import ToDoSerializer


# - view that can let us create a record
# - view that can help us list all the records we have
# - view that can let us view a single record (update and delete)
# decorators would come in for a function based view

class ToDoListView(APIView):
    def get(self, request, *args, **kwargs):
        all_todo_records = ToDo.objects.all() # python object
        browser_data = ToDoSerializer(all_todo_records, many=True) # is just an object
        return Response(browser_data.data) # correct

    def post(self, request, *args, **kwargs):
        # request.data # json/xml
        todo_data = ToDoSerializer(data=request.data)
        if todo_data.is_valid():
            todo_data.save()
            return Response(todo_data.data, status=status.HTTP_201_CREATED)
        return Response(todo_data.errors, status=status.HTTP_400_BAD_REQUEST)

class ToDoDetailView(APIView):
    def get_todo_item(self, item_pk: int):
        return ToDo.objects.get(pk=item_pk)

    def get(self, request, pk: int, *args, **kwargs):
        todo_item = self.get_todo_item(pk)
        browser_data = ToDoSerializer(todo_item,) 
        return Response(browser_data.data)


class GenericTodoListView(generics.ListCreateAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()

class GenericTodoDetailView(generics.RetrieveAPIView):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()