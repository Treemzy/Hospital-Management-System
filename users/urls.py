from django.urls import path
from .models import Role
from .views import (
    RoleListView,
    RoleDetailView,
    RoleCreateView,
    RoleUpdateView,
    RoleDeleteView,

    UsersListView,
    UsersUpdateView,
    UsersDetailView,
    UsersDeleteView

)

urlpatterns = [
    path('Role/', RoleListView.as_view(), name='CHMS-Role'),
    path('Role/create/', RoleCreateView.as_view(), name='CHMS-RoleCreate'),
    path('Role/<int:pk>/update/', RoleUpdateView.as_view(), name='CHMS-RoleUpdate'),
    path('Role/<int:pk>/', RoleDetailView.as_view(), name='CHMS-RoleDetail'),
    path('Role/<int:pk>/delete/', RoleDeleteView.as_view(), name='CHMS-RoleDelete'),

    path('AllUsers/', UsersListView.as_view(), name='CHMS-AllUsers'),
    path('AllUsers/<int:pk>/update/', UsersUpdateView.as_view(), name='CHMS-AllUsersUpdate'),
    path('AllUsers/<int:pk>/', UsersDetailView.as_view(), name='CHMS-AllUsersDetail'),
    path('AllUsers/<int:pk>/delete/', UsersDeleteView.as_view(), name='CHMS-AllUsersDelete'),
]