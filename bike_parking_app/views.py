# from django.shortcuts import render
from bike_parking_app.models import User, BikeRackData,Achievements,Badge
from django.contrib.auth import login, logout
from rest_framework.views import APIView, Response
from rest_framework import permissions, status, generics
from rest_framework.authentication import SessionAuthentication
from .validations import custom_validation,validate_username,validate_password
from .serializers import UserRegisterSerializer, UserLoginSerializer,UserSerializer,BikeRackDataSerializer,AchievementsSerializer,BadgeSerializer,LeaderboardSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class UserRegister(APIView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request):
        clean_data = custom_validation(request.data)
        serializer = UserRegisterSerializer(data=clean_data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(clean_data)
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UserLogin(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (SessionAuthentication,)

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            login(request, user)
            return Response(serializer.data, status=status.HTTP_200_OK) 

class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()
    def post(self, request):
        logout(request)
        return Response(status=status.HTTP_200_OK)

class UserView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

class BikeRackDataDetail(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = BikeRackData.objects.all()
    serializer_class = BikeRackDataSerializer
    lookup_field = 'Site_ID'

class BikeRackDataCreate(generics.CreateAPIView):
    queryset = BikeRackData.objects.all()
    serializer_class = BikeRackDataSerializer


class AchievementsView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = AchievementsSerializer

    def get_queryset(self):
        return Achievements.objects.all()

    def get(self, request, format=None):
        achievements = self.get_queryset()
        serializer = self.serializer_class(achievements, many=True)
        return Response(serializer.data)

class BadgeView(APIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = BadgeSerializer

    def get_queryset(self):
        return Badge.objects.all()

    def get(self, request, format=None):
        badge = self.get_queryset()
        serializer = self.serializer_class(badge, many=True)
        return Response(serializer.data)

class LeaderboardListView(generics.ListAPIView):
    queryset = User.objects.all().order_by('-assessment_count')
    serializer_class = LeaderboardSerializer