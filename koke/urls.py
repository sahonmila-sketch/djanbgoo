from django.urls import path
from .views import UserAllView, UserDetailView, UserCreateView, UserUpdateView, UserDeleteView, UserListCreateView, UserRetrieveUpdateView, UserRetrieveDestroyView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('users/', UserAllView.as_view()),  
    path('users/<int:pk>/', UserDetailView.as_view()),
    path('users/create/', UserCreateView.as_view()),
    path('users/<int:pk>/update/', UserUpdateView.as_view()),
    path('users/<int:pk>/delete/', UserDeleteView.as_view()),
    path('users/list-create/', UserListCreateView.as_view()),
    path('users/<int:pk>/retrieve-update/', UserRetrieveUpdateView.as_view()),
    path('users/<int:pk>/retrieve-delete/', UserRetrieveDestroyView.as_view()),
    path('users/<int:pk>/retrieve-update-delete/', UserRetrieveUpdateDestroyView.as_view()),
]