from rest_framework import serializers
from users.models import User
from groups.models import Group

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'role']

    def create(self, validated_data):
        password = validated_data.pop('password')

        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user
class GroupSerializer(serializers.ModelSerializer):

    leader = serializers.StringRelatedField()
    members = serializers.StringRelatedField(many=True)

    class Meta:
        model = Group
        fields = [
            'id',
            'name',
            'code',
            'leader',
            'members',
            'created_at'
        ]

class JoinGroupSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=20)