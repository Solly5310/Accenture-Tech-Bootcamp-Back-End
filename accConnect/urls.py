from django.urls import path
from accConnect import views



from . import views

urlpatterns = [
     # ex: /polls/
    path('', views.index, name='index'),
    path('projects', views.ProjectView.as_view()),
    path('projects/<int:pk>', views.project_detail),
    path('teams', views.TeamView.as_view()),
    
    #pk is where the integer should go corresponding to the primary key in the model
    path('teams/<int:pk>', views.team_detail),
    path('users', views.UserView.as_view()),
    path('users/<int:pk>', views.user_detail),
    # ex: /polls/5/
]