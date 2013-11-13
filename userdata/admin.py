from django.contrib import admin
from userdata.models import TrainingData
from userdata.models import UserData

class UserDataAdmin(admin.ModelAdmin):
	list_display = ('username', 'legal_name', 'manager', 'l3', 'l2', 'l1')
	search_fields = ['eeid', 'username', 'legal_name', 'fname', 'lname',
	'manager', 'l1', 'l2', 'l3', 'email', 'hire_date', 'job_code',
	'job_title']

admin.site.register(TrainingData)
admin.site.register(UserData, UserDataAdmin)