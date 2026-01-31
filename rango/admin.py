from django.contrib import admin
from rango.models import Category, Page, PageAdmin

# Register your models here.

admin.site.register(Category)
# admin.site.register(Page)
admin.site.register(Page, PageAdmin)

from django.contrib import admin

from .models import Choice, Question


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
