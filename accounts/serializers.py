from rest_framework import serializers
from .models import Account, User


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ["id", "name", "display_picture", "bio"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'verification_code', 'phone_number')
        extra_kwargs = {'password': {'write_only': True}}


"""
class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password', 'verification_code', 'phone_number', 'account')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        profile_data = validated_data.pop('account')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Account.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('account')
        profile = instance.account

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.name = profile_data.get('name', profile.name)
        #profile.display_picture = profile_data.get('display_picture', profile.display_picture)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.save()

        return instance

"""