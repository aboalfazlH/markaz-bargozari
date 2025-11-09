from django.contrib import admin
from .models import UploadFile


@admin.register(UploadFile)
class UploadFileAdmin(admin.ModelAdmin):

    list_display = ('id','user','file_name','upload_date',)
    list_filter = ('upload_date',)
    readonly_fields = ('upload_date',)
    search_fields = ('user','user__username','user__first_name','user__last_name','file_name')
    date_hierarchy = 'upload_date'