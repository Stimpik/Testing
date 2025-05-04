from django.db import models
from django.contrib.auth.models import User


class Ad(models.Model):
    class Condition(models.TextChoices):
        NEW = 'NEW', 'Новая'
        USED = 'US', 'Б/У'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50)
    condition = models.CharField(max_length=50, choices=Condition, default=Condition.USED)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ExchangeProposal(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PD', 'Ожидает'
        ACCEPTED = 'AC', 'Принята'
        REJECTED = 'RJ', 'Отклонена'

    ad_sender = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='sender')
    ad_receiver = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='reciver')
    comment = models.TextField()
    status = models.CharField(max_length=50, choices=Status, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Предложение от {self.ad_sender.user.username} к {self.ad_receiver.user.username}'
