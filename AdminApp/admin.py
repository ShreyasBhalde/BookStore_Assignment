from django.contrib import admin
from .models import Category,Book,Accounts

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name']

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','Book_name','Publication_date','Author','price','description','image','cat_fk']

class AccountsAdmin(admin.ModelAdmin):
    list_display = ['cardno','cvv','expiry','balance']

admin.site.register(Book,BookAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Accounts,AccountsAdmin)
