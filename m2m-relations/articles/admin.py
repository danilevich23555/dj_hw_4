from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Scorpe, Relationship


class RelationshipInlineFormset(BaseInlineFormSet):
    def clean(self):

        main_id_tag = [form.cleaned_data['is_main'] for form in self.forms]
        count_true_false = [main_id_tag.count(True)]
        if count_true_false[0] != 1:
            raise ValidationError('Основной тег должен быть один,уберите лишние и нажмите сохранить!')
        return super().clean()  # вызываем базовый код переопределяемого метода



class RelationshipInline(admin.TabularInline):
    model = Relationship
    formset = RelationshipInlineFormset
    extra = 0

@admin.register(Article)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at', 'image']
    inlines = [RelationshipInline]
