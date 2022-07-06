from django.urls import path
from . import views
# urlpatterns => static name
urlpatterns = [
    # Have your root route redirect to /shows
    path('', views.viewShows),
    # /shows/new- GET - method should return a template containing the form for adding a new TV show
    path('shows/new', views.viewAddShow),
    path('shows/create', views.addShow, name="addShow"), #/shows/create - POST - method should add the show to the database, then redirect to /shows/<id>
    path('shows/<int:showId>', views.viewShow, name="viewShow"),
    path('shows/delete/<int:showId>', views.deleteShow, name="delete"),
    path('shows/<int:showId>/update', views.updateShow, name="update"),
    path('shows/<int:showId>/edit', views.viewUpdateShow, name="edit"),    
]
