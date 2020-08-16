from django.contrib import admin

# Register your models here.

from .models import Post,Category,ContactFormModel, SubscriberEmailModel


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(ContactFormModel)
admin.site.register(SubscriberEmailModel)