from django.contrib import admin

# Register your models here.
from .models import Question, Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    #순서를 바꾸는 문장
    #fields = ['pub_date', 'question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Data Information', {'fields': ['pub_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInline]

    list_display=('question_text','pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
