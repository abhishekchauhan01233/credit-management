from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import user_model, transaction_model, feedback_model
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class user_model_Admin(ImportExportModelAdmin):
    list_display = ('user_id','name','email','credit',)

class transaction_model_Admin(ImportExportModelAdmin):
    list_display = ('from_email','to_email','date','credit',)
    list_filter = ('date',)

class feedback_model_Admin(ImportExportModelAdmin):
    list_display = ('name','role','feedback',)
    list_filter = ('role',)

admin.site.site_header = 'Credit Managemenet'
admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(user_model, user_model_Admin)
admin.site.register(transaction_model, transaction_model_Admin)
admin.site.register(feedback_model, feedback_model_Admin)