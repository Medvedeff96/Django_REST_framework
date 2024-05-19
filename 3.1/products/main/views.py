from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    """реализуйте получение всех товаров из БД
    реализуйте сериализацию полученных данных
    отдайте отсериализованные данные в Response"""
    products = Product.objects.all()
    pr_lst = ProductListSerializer(products, many=True)
    return Response(pr_lst.data)

class ProductDetailsView(APIView):
    def get(self, request, product_id):
        """реализуйте получение товара по id, если его нет, то выдайте 404
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=404)
        pr_det = ProductDetailsSerializer(instance=product)
        return Response(pr_det.data)


# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        mark = request.GET.get('mark')
        reviews = Review.objects.filter(product_id=product_id)
        if mark:
            reviews = reviews.filter(mark=mark)
        ser = ReviewSerializer(reviews, many=True)
        return Response(ser.data)
