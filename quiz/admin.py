#Django
from django.contrib import admin

#Local
from .models import AnswerUser, Question, Answer, QuestionUser, QuestionaryUser

# Register your models here.
admin.site.register(Question) 
admin.site.register(Answer)
admin.site.register(QuestionaryUser)
admin.site.register(QuestionUser)
admin.site.register(AnswerUser)