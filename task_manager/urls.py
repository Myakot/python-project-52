from django.contrib import admin
from django.urls import path, include
from task_manager.views import IndexView, UserLoginView, UserLogoutView


urlpatterns = [
    path('', IndexView.as_view(), name='home'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', include('task_manager.included_apps.users.urls')),
    path('statuses/', include('task_manager.included_apps.statuses.urls')),
    path('tasks/', include('task_manager.included_apps.tasks.urls')),
    path('labels/', include('task_manager.included_apps.labels.urls')),
    path('admin/', admin.site.urls),
]
