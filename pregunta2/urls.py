from django.urls import include, path
from django.contrib import admin
from quiz import urls as quiz_urls
from users import urls as user_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('quiz/', include(quiz_urls, namespace='quiz')),
    path('users/', include(user_urls, namespace='users'))
]
