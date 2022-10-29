from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Product
from .serializers import ProductSerializer
from permissions import IsOwnerOrReadOnly


# Create your views here.


class Home(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        persons = Product.objects.all()
        ser_data = ProductSerializer(instance=persons, many=True)
        return Response(data=ser_data.data)


class ProductListView(APIView):

    def get(self, request):
        questions = Product.objects.all()
        srz_data = ProductSerializer(instance=questions, many=True).data
        return Response(srz_data, status=status.HTTP_200_OK)


class ProductCreateView(APIView):
    permission_classes = [IsAuthenticated, ]
    serializer_class = ProductSerializer

    def post(self, request):
        srz_data = ProductSerializer(data=request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_201_CREATED)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdateView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, pk):
        question = Product.objects.get(pk=pk)
        self.check_object_permissions(request, question)
        srz_data = ProductSerializer(instance=question, data=request.data, partial=True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data, status=status.HTTP_200_OK)
        return Response(srz_data.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDeleteView(APIView):
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def delete(self, request, pk):
        question = Product.objects.get(pk=pk)
        question.delete()
        return Response({'message': 'question deleted'}, status=status.HTTP_200_OK)
