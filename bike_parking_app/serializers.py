from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate
from .models import BikeRackData, Achievements, Badge

UserModel = get_user_model()

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        phone_number = validated_data.get('phone_number')
        password = validated_data.get('password')


        user_obj = UserModel.objects.create_user(username=username, email=email, phone_number=phone_number, password=password)

        return user_obj

class UserLoginSerializer(serializers.Serializer):
    password = serializers.CharField()
    credentials = serializers.CharField()

    def check_user(self, clean_data):
        credentials = clean_data['credentials']
        password = clean_data['password']
        
        # Attempt authentication with username
        user = authenticate(username=credentials, password=password)
        
        # If authentication fails with username, attempt with email
        if user is None:
            try:
                user = UserModel.objects.get(email=credentials)
                user = authenticate(username=user.username, password=password)
            except UserModel.DoesNotExist:
                pass
        
        if user is None:
            try:
                user = UserModel.objects.get(phone_number=credentials)
                user = authenticate(username=user.username, password=password)
            except UserModel.DoesNotExist:
                pass
        
        if user is None:
            raise serializers.ValidationError('User not found or incorrect credentials.Please provide a valid username,email or phone number, and password')
        
        return user

class AchievementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievements
        fields = '__all__'

class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'
   
class UserSerializer(serializers.ModelSerializer):
    achievements = AchievementsSerializer(many=True, read_only=True)
    badges = BadgeSerializer(many=True, read_only=True)
    phone_number = serializers.CharField(source='get_formatted_phone_number', read_only=True)    
    
    class Meta:
        model = UserModel
        fields = ['id','email', 'username','phone_number', 'achievements', 'image_id','assessment_count','assessment_streak','distance_traveled','achievements_completed','badges_earned','mistery_boxes_earned','badges']

class BikeRackDataSerializer(serializers.ModelSerializer):

    class Meta:
        model = BikeRackData
        fields = '__all__'

class LeaderboardSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ['username','assessment_count']