from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer


class ProductView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            queryset = Product.objects.all()
            serializer = ProductSerializer(queryset, many=True)
        else:
            queryset = Product.objects.get(id=pk)
            serializer = ProductSerializer(queryset)

        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method put is not allowed"})

        try:
            instance = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Object does not exist"})

        serializer = ProductSerializer(instance=instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"product": serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response({"error": "Method delete is not allowed"})
        try:
            queryset = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response({"error": "Object does not exist"})

        queryset.delete()

        return Response({"product": "deleted " + str(pk)})
