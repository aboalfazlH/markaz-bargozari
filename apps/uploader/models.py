from django.db import models
from apps.users.models import User


def get_upload_path(instance,filename):
    user = instance.user
    return f"{user}/{filename}"


class UploadFile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    file_name = models.CharField(verbose_name="نام فایل")
    file = models.FileField(upload_to=get_upload_path)
    upload_date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'فایل'
        verbose_name_plural = 'فایل ها'


    def save(self, *args, **kwargs):
        if not self.file_name:
            self.file_name = self.file.name
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.file_name}"