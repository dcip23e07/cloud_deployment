from django.contrib import admin
from todo.models import ToDo


# also have an admin class
admin.site.register(ToDo)