from django.contrib import admin
from . models import Product, Variation,ReviewRating,ProductGallery
import admin_thumbnails
# Register your models here.

@admin_thumbnails.thumbnail('image')
class ProductgalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price','stock','category','modified_date','is_available')
    prepopulated_fields = {'slug':('product_name',)}
    inline = [ProductgalleryInline]

class VariationAdmin(admin.ModelAdmin):
    list_display = ('product','variation_category','variation_value','is_active','created_date')
    list_editable =('is_active',)
    list_filter = ('product','variation_category','variation_value')


class ReviewRatingAdmin(admin.ModelAdmin):
    list_display = ('product','user','rating','ip','status','created_at','updated_at')

    

admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating, ReviewRatingAdmin)
admin.site.register(ProductGallery)