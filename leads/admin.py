from django.contrib import admin
from leads.models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Lead)
