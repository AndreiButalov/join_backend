from rest_framework import serializers
from join_app.models import Users, GuestContacts, Tasks


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class GuestContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GuestContacts
        fields = '__all__'


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = '__all__'