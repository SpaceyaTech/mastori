from rest_framework import serializers
from .models import User, Account
from rest_framework.exceptions import AuthenticationFailed 
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken,TokenError
from django.contrib import auth
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ( 'name','display_picture','bio','created_at','updated_at')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Bifrost user writable nested serializer
    """
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ('url', 'email','username', 'first_name', 'last_name', 'password', 'profile','verification_code','phone_number',)
        extra_kwargs = {'password': {'write_only': True}}
     

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        Account.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        
        profile.name = profile_data.get('name', profile.name)
        profile.display_picture = profile_data.get('display_picture', profile.display_picture)
        profile.bio = profile_data.get('bio', profile.bio)
        profile.created_at = profile_data.get('created_at', profile.created_at)
        profile.updated_at = profile_data.get('updated_at', profile.updated_at)
       
        profile.save()

        return instance


class LogoutSerializer(serializers.Serializer):
    refresh=serializers.CharField()
    default_error_messages={
        'bad_token':('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
        
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68, min_length=6,write_only=True)
    username=serializers.CharField(max_length=255,min_length=3, read_only=True)
    tokens=serializers.SerializerMethodField()

    def get_tokens(self,obj):
        user = User.objects.get(email=obj['email'])

        return {
            'access':user.tokens()['access'],
            'refresh':user.tokens()['refresh']
        }
    class Meta:
        model=User
        fields=['email','password','username','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password=attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
      
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        #if not user.is_verified:
            #raise AuthenticationFailed('email is not verified')
        if not user.is_active:
            raise AuthenticationFailed('account disabled, contact admin')
        

        
        return {
            'email': user.email,
            'username':user.username,
            'tokens':user.tokens
        } 

'''
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('phone_number', 'display_picture')
class UserSerializer(serializers.ModelSerializer):
    account = ProfileSerializer(required=True)
    class Meta:
        model = User
        fields = ('first_name','last_name','username','account', 'email',  'created_at','updated_at')

    def create(self, validated_data):

        # create user 
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )

        profile_data = validated_data.pop('account')
        # create profile
        account = Account.objects.create(user = user,
            phone_number = profile_data['phone_number'],
            #display_picture = profile_data['display_picture'],
            )
        user.save()
        return user

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model= User
        fields=['email','username','password']

    def validate(self, attrs):
        email= attrs.get('email', '')
        username= attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username can only contain alphanumeric character')
        return attrs

    def create (self, validated_data):
        return User.objects.create_user(**validated_data)


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['id', 'user', 'phone_number','bio', 'created_at', 'updated_at']

        read_only_fields = ('user',)


class CustomUserSerializer(serializers.ModelSerializer):
   
    user_profile = AccountSerializer(many=True)
    password = serializers.CharField(max_length=68, min_length=6, write_only=True)
    class Meta:
        model = User
        fields = ['id', 'first_name','last_name','username','user_profile', 'email','password',  'created_at','updated_at']
    def validate(self, attrs):
        email= attrs.get('email', '')
        username= attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username can only contain alphanumeric character')
        return attrs
    def create(self, validated_data):
        profiles_data = validated_data.pop('user_profile')
        user = User.objects.create(**validated_data)
        for profile_data in profiles_data:
            Account.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profiles_data = validated_data.pop('user_profile')
        profiles = (instance.user_profile).all()
        profiles = list(profiles)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.save()

        for profile_data in profiles_data:
            profile = profiles.pop(0)
            profile.phone_number = profile_data.get('phone_number', profile.phone_number)
            profile.bio = profile_data.get('bio', profile.bio)
            profile.created_at = profile_data.get('created_at', profile.created_at)
            profile.updated_at = profile_data.get('updated_at', profile.updated_at)
            profile.save()
        return instance
class LogoutSerializer(serializers.Serializer):
    refresh=serializers.CharField()
    default_error_messages={
        'bad_token':('Token is expired or invalid')
    }
    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad_token')
        
class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255,min_length=3)
    password=serializers.CharField(max_length=68, min_length=6,write_only=True)
    username=serializers.CharField(max_length=255,min_length=3, read_only=True)
    tokens=serializers.SerializerMethodField()

    def get_tokens(self,obj):
        user = User.objects.get(email=obj['email'])

        return {
            'access':user.tokens()['access'],
            'refresh':user.tokens()['refresh']
        }
    class Meta:
        model=User
        fields=['email','password','username','tokens']

    def validate(self, attrs):
        email = attrs.get('email', '')
        password=attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)
      
        if not user:
            raise AuthenticationFailed('Invalid credentials, try again')
        
        if not user.is_verified:
            raise AuthenticationFailed('email is not verified')
        if not user.is_active:
            raise AuthenticationFailed('account disabled, contact admin')
        

        
        return {
            'email': user.email,
            'username':user.username,
            'tokens':user.tokens
        } 

    
class EmailVerificationSerializer(serializers.ModelSerializer):
    token=serializers.CharField(max_length=555)

    class Meta:
        model=User

        fields=['token']

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name')

'''