from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import User

# Create your models here.
class RequestStatus(models.TextChoices):
    "Enum that specifies the friend Request Status"

    PENDING = "PENDING"
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=RequestStatus.choices, default=RequestStatus.PENDING)

    class Meta:
        verbose_name = _("Friend Request")
        verbose_name_plural = _("Friend Requests")
        db_table = "friend_requests"

    def __str__(self) -> str:
        return f"{__class__}(id={self.id})" 