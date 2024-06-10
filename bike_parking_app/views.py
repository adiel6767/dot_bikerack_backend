# from django.shortcuts import render
from bike_parking_app.models import CustomUser, BikeRackData,Achievements,Badge
from rest_framework.generics import GenericAPIView, RetrieveAPIView,RetrieveUpdateAPIView,CreateAPIView,ListAPIView
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

    def post(self, request):
        data = request.data
        assert validate_username(data)
        assert validate_password(data)
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.check_user(data)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                }, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UserView(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
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
    queryset = CustomUser.objects.all().order_by('-assessment_count')
    serializer_class = LeaderboardSerializer