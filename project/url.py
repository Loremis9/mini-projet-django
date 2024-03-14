from django.urls import include, path

from project.views import index

urlpatterns = [
    path("test/", index, name="project-index")
]