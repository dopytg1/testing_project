from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=150)


class TestSet(models.Model):
    description = models.CharField(max_length=250)
    title = models.CharField(max_length=150)

    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)


class Question(models.Model):
    text = models.CharField(max_length=250)
    test_set_id = models.ForeignKey(TestSet, on_delete=models.CASCADE)


class Answer(models.Model):
    answer_text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)

