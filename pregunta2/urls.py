from django.urls import include, path
from rest_framework import routers
from quiz import views

router = routers.DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'answers', views.AnswerViewSet)



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path("random_question/", views.GetRandomQuestion.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
