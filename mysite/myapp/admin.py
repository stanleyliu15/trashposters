from django.contrib import admin

from .models import UserData
from .models import Posts
from .models import HazardType
from .models import Message
from .models import Comments
from .models import PostImageCollection

# Register your models here.
admin.site.register(HazardType)
admin.site.register(UserData)
admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Message)
admin.site.register(PostImageCollection)
