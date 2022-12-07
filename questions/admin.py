from django.contrib import admin
from django.contrib.auth.models import Group

from .models import Category, TestSet, Question, Answer


admin.site.register(Category)
admin.site.register(TestSet)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.unregister(Group)
