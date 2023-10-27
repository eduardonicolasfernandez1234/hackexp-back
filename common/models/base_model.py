from django.db import models

# from auth.models import User


class NonDeletedObjectsQuerySet(models.QuerySet):
    def non_deleted(self):
        return self.filter(is_deleted=False)


class NonDeletedObjectsManager(models.Manager):
    def get_queryset(self):
        return NonDeletedObjectsQuerySet(self.model, using=self._db).non_deleted()


class BaseModel(models.Model):
    """ Abstract base class for models with audit logs. """
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    last_user_id = models.PositiveIntegerField(default=0)

    objects = NonDeletedObjectsManager()
    everything = models.Manager()

    class Meta:
        abstract = True

    # @property
    # def user(self):
    #     if not hasattr('self', '_last_user_id'):
    #         self._last_user_id = User.objects.filter(
    #             pk=self.last_user_id).first()
    #         return self._last_user_id

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.save()

    def undelete(self):
        self.is_deleted = False
        self.save()
