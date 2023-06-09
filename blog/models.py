from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class BaseModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    upvotes = ArrayField(models.IntegerField(default=0), default=list)
    downvotes = ArrayField(models.IntegerField(default=0), default=list)

    def upvote(self, user):
        if user not in self.upvotes:
            self.upvotes.append(user)
            if user in self.downvotes:
                self.downvotes.remove(user)
        self.save()

    def downvote(self, user):
        if user not in self.downvotes:
            self.downvotes.append(user)
            if user in self.upvotes:
                self.upvotes.remove(user)
        self.save()

    def get_rating(self):
        return len(self.upvotes) - len(self.downvotes)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    class Meta:
        abstract = True


class Question(BaseModel):
    title = models.CharField(max_length=128)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title


class Answer(BaseModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text