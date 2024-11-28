from django.contrib import admin

# Register your models here.
from .models import Category, Topping, Wrapper, IceCream


admin.site.empty_value_display = 'Не задано'


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper',
        'price'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category',
        'price'
    )
    search_fields = ['title', 'id']
    list_filter = ['category']
    list_display_links = ['title']
    filter_horizontal = ('toppings',)


class IceCreamInLine(admin.StackedInline):
    model = IceCream
    extra = 0
    filter_horizontal = ('toppings',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        IceCreamInLine
    ]
    list_display = ['title']


admin.site.register(IceCream, IceCreamAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Wrapper)
admin.site.register(Topping)
