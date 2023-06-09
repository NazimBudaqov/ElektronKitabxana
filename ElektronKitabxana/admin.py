from django.contrib import admin
from .models import Book, Category, Author

class BookAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","reyting","slug",)
    list_editable = ("is_active",)
    search_fields = ("title","description",)
    readonly_field = ("slug",)
    list_filter = ("category","author","is_active")

class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","middleName","lastName","slug",)
    readonly_field = ("slug",)

admin.site.register(Book,BookAdmin)
admin.site.register(Category) 
admin.site.register(Author, AuthorAdmin) 

# Register your models here.