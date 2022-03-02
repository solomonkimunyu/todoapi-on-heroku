from django.contrib import admin
from django.urls import include, path  # new


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("todos.urls")),  # new
]
