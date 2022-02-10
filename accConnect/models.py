from django.db import models

class Project(models.Model):
    def __str__(self):
        return self.project_name
    
    project_name = models.CharField(max_length=42)
    
    

class Team(models.Model):
    def __str__(self):
        return self.team_name

    team_name = models.CharField(max_length=42)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class User(models.Model):
    def __str__(self):
        return self.user_name
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=42)
    email = models.EmailField(max_length=75)




   




#question = models.ForeignKey(Question, on_delete=models.CASCADE)
#choice_text = models.CharField(max_length=200)
#votes = models.IntegerField(default=0)