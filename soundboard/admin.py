# soundboard/admin.py
# Admin models for administrative application to manage soundboard website
# Last modified: 12/28/2021

from django.contrib import admin

from .models import SoundboardCategory, Soundboard, SoundCategory, Sound


# Soundboard admin models
class SoundboardCategoryAdmin(admin.ModelAdmin):
    fields = ['category_name']


class SoundboardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category', {'fields': ['category']}),
        ('Soundboard Information', {'fields': ['soundboard_name', 'soundboard_description', 'soundboard_image']})
    ]
    list_display = ('soundboard_name', 'category')


# Sound admin models
class SoundInLine(admin.TabularInline):
    model = Sound
    extra = 1


class SoundCategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Category Information', {'fields': ['category_name', 'soundboard']}),
    ]
    inlines = [SoundInLine]
    list_display = ('category_name', 'soundboard')


admin.site.register(SoundboardCategory, SoundboardCategoryAdmin)
admin.site.register(Soundboard, SoundboardAdmin)
admin.site.register(SoundCategory, SoundCategoryAdmin)
