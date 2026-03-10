from django.contrib import admin
from .models import Category, Quiz, Question, Choice, Attempt

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'time_limit_minutes', 'created_at')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Attempt)
