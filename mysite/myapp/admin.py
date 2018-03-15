from django.contrib import admin
from .models import Users
from .models import UserData
from .models import Posts
from .models import Locations
from .models import Messages
from .models import Comments

# Register your models here.
admin.site.register(Users)
admin.site.register(UserData)
admin.site.register(Posts)
admin.site.register(Locations)
admin.site.register(Messages)
admin.site.register(Comments)