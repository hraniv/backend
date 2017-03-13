from django.contrib import admin
from django.contrib.auth.models import Group

from db.models import AuthToken, Feedback, InfoObject, Category

admin.site.unregister(Group)


@admin.register(AuthToken)
class AuthTokenAdmin(admin.ModelAdmin):
    list_display = ('key', 'user', 'created')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created')
    prepopulated_fields = {'url': ('title',), }


@admin.register(InfoObject)
class InfoObjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'created')


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'subject', 'created')

