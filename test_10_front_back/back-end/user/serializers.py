from rest_framework import serializers

from .models import User


#### user
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
