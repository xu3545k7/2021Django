from django.contrib import admin
from mysite.models import Post,Country,City
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')

admin.site.register(Post, PostAdmin)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','country_id')
admin.site.register(Country, CountryAdmin)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name','population','country_id')
admin.site.register(City, CityAdmin)