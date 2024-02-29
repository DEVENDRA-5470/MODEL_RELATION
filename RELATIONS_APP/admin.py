from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Comment)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'content', 'display_authors')

    def display_authors(self, obj):
        return ', '.join(author.firstName + ' ' + author.lastName for author in obj.author.all())

    display_authors.short_description = 'Authors'

admin.site.register(Book, BookAdmin)


