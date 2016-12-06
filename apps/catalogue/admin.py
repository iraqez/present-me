from django.contrib import admin
from treebeard.admin import TreeAdmin
from treebeard.forms import movenodeform_factory
from modeltranslation.admin import TabbedTranslationAdmin
#Category
from .models import Category as CategoryNew
from oscar.apps.catalogue.admin import Category as CategoryOld
#ProductClass
from .models import ProductClass as ProductClassNew
from oscar.apps.catalogue.admin import ProductClass as ProductClassOld

#Product
from .models import Product as ProductNew
from oscar.apps.catalogue.admin import Product as ProductOld
#all_oscar
from oscar.apps.catalogue.admin import ProductAttributeInline,\
    AttributeInline, CategoryInline, ProductRecommendationInline
import apps.catalogue.translation

admin.site.unregister(CategoryOld)
admin.site.unregister(ProductClassOld)
admin.site.unregister(ProductOld)


class ProductClassAdminI18n(TabbedTranslationAdmin):
    list_display = ('name', 'requires_shipping', 'track_stock')
    inlines = [ProductAttributeInline]

class CategoryAdminI18n(TreeAdmin, TabbedTranslationAdmin):
    form = movenodeform_factory(CategoryOld)
    list_display = ('name', 'name_ru', 'name_uk', 'slug')
    list_filter = ('name_ru', 'name_uk')

class ProductAdminI18n(TabbedTranslationAdmin):
    date_hierarchy = 'date_created'
    list_display = ('get_title', 'upc', 'get_product_class', 'structure',
                    'attribute_summary', 'date_created')
    list_filter = ['structure', 'is_discountable']
    raw_id_fields = ['parent']
    inlines = [AttributeInline, CategoryInline, ProductRecommendationInline]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['upc', 'title']

    def get_queryset(self, request):
        qs = super(ProductAdminI18n, self).get_queryset(request)
        return (
            qs
            .select_related('product_class', 'parent')
            .prefetch_related(
                'attribute_values',
                'attribute_values__attribute'))

admin.site.register(ProductNew, ProductAdminI18n)
admin.site.register(ProductClassNew, ProductClassAdminI18n)
admin.site.register(CategoryNew, CategoryAdminI18n)
from oscar.apps.catalogue.admin import *  # noqa

