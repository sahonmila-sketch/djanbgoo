from django.urls import path
from .views import UserAllView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, UserListCreateView, UserRetrieveDestroyView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserAllView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('users/list-create/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:pk>/retrieve-destroy/', UserRetrieveDestroyView.as_view(), name='user-retrieve-destroy'),
    path('users/<int:pk>/retrieve-update-destroy/', UserRetrieveUpdateDestroyView.as_view(), name='user-retrieve-update-destroy'),
]  