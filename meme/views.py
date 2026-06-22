from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView, ListCreateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from .models import UserModel
from .serializers import UserSerializer

class UserAllView(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']  # Allow unrestricted access

class UserDetailView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

class UserCreateView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

class UserUpdateView(UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

class UserDeleteView(DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

class UserListCreateView(ListCreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

class UserRetrieveDestroyView(RetrieveDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

class UserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = ['IsAuthenticated']

# Create your views here.
