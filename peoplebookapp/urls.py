from django.urls import path
from peoplebookapp import views

urlpatterns = [
    path('users/', views.showUsers),
    path('users/<str:display>/', views.showUsers),
    # grace a name='peoplebook-user-detail', on va pouvoir appeler cette url dans no templates
    path('users/<str:name>/detail/', views.showUserDetail2, name='peoplebook-user-detail'),
]
