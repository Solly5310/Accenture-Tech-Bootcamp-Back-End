from rest_framework import serializers
from . models import Project, Team, User


class projectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'

class teamSerializer(serializers.ModelSerializer):
    class Meta:
            model = Team
            fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = '__all__'

#turn the models into a JSON format
#Whenever a call goes to the endpoint, it will automatically convert it into json