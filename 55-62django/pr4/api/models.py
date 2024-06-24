from tastypie.resources import ModelResource
from shop.models import Category, Course
from tastypie.authorization import Authorization
from .authentication import CustomAuthentication


class CategoryResource(ModelResource):
    class Meta:
        queryset = Category.objects.all()
        resource_name = 'categories'
        allowed_methods = ['get']


class CourseResource(ModelResource):
    class Meta:
        queryset = Course.objects.all()
        resource_name = 'courses'
        allowed_methods = ['get', 'post', 'delete']
        excludes = ['reviews_qty', 'created_at']  # excludes these fields when send to client
        authentication = CustomAuthentication()
        authorization = Authorization()

    def hydrate(self, bundle):  # для добавения поля category_id
        bundle.obj.category_id = bundle.data['category_id']
        return bundle

    def dehydrate(self, bundle):  # для распарсивания данных из базы
        bundle.data['category_id'] = bundle.obj.category_id
        bundle.data['category'] = bundle.obj.category
        return bundle

    def dehydrate_title(self, bundle):  # для распарсивания и изменения заголовка в верхний регистр
        return bundle.data['title'].upper()
