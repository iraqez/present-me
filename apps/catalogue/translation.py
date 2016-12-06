from modeltranslation.translator import translator, TranslationOptions
from .models import Category, ProductClass, Product, ProductAttribute,\
    ProductAttributeValue


class CategoryTranslationOptions(TranslationOptions):
    """
    Класс настроек интернационализации полей модели Category.
    """
    fields = ('name', 'description',)


class ProductClassTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProductTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)

class ProductAttributeTranslationOptions(TranslationOptions):
    fields = ('name',)

class ProductAttributeValueTranslationOptions(TranslationOptions):
    fields = ('value_text', 'value_richtext')

translator.register(ProductAttributeValue, ProductAttributeValueTranslationOptions)
translator.register(ProductAttribute, ProductAttributeTranslationOptions)
translator.register(ProductClass, ProductClassTranslationOptions)
translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)