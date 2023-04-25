from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from .models import Book
from .serializer import BookModelSerializer
from rest_framework.permissions import IsAuthenticated


class GetAllData(APIView):
    def get(self, request):
        myquery = Book.objects.all()
        myserializerr = BookModelSerializer(myquery, many=True, context={'request': request})
        return Response(myserializerr.data, status=status.HTTP_200_OK)


class GetSpecialData(APIView):
    def get(self, request):
        myquery = Book.objects.filter(fav=False)
        myserializer = BookModelSerializer(myquery, many=True, context={'request': request})
        return Response(myserializer.data, status=status.HTTP_200_OK)


class UpdateData(APIView):
    def get(self, request, pk):
        myquery = Book.objects.get(id=pk)
        myserializer = BookModelSerializer(myquery, context={'request': request})
        return Response(myserializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        myquery = Book.objects.get(pk=pk)
        myserializer = BookModelSerializer(myquery, data=request.data)
        if myserializer.is_valid():
            myserializer.save()
            return Response(myserializer.data, status=status.HTTP_201_CREATED)
        return Response(myserializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateData(APIView):
    def post(self, request):
        myserializer = BookModelSerializer(data=request.data)
        if myserializer.is_valid():
            myserializer.save()
            return Response(myserializer.data, status=status.HTTP_201_CREATED)
        return Response(myserializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CreateData2(APIView):
#     def post(self, request):
#         myserializer = serializerBook(data=request.data)
#         if myserializer.is_valid():
#             auther = myserializer.data.get('author')
#             description = myserializer.data.get('description')
#             store_name = myserializer.data.get('store_name')
#             fav = myserializer.data.get('fav')
#             image = request.FILES['image']
#
#         else:
#             return Response(myserializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#         mybook = Book(name=auther, store_name=store_name, fav=fav, description=description, image=image)
#         mybook.save()
#         return Response(myserializer.data, status=status.HTTP_400_BAD_REQUEST)


class GetSearchData(APIView):
    def get(self, request):
        search = request.GET['name']
        myquery = Book.objects.filter(name__contains=search)
        myserializer = BookModelSerializer(myquery, many=True)
        return Response(myserializer.data, status=status.HTTP_200_OK)


class DeleteData(APIView):
    def get(self, request, pk):
        myquery = Book.objects.filter(id=pk)
        myserializerr = BookModelSerializer(myquery, many=True, context={'request': request})
        return Response(myserializerr.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        myquery = Book.objects.get(id=pk)
        myquery.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def GetAllDataFunc(request):
    if request.method == 'GET':
        myQuery = Book.objects.all()
        myserializer = BookModelSerializer(myQuery, many=True)
        return Response({'pagename': 'alldata', 'data': myserializer.data}, status=status.HTTP_200_OK)
    if request.method == 'POST':
        myserializer = BookModelSerializer(data=request.data)
        if myserializer.is_valid():
            myserializer.save()
            return Response(myserializer.data, status=status.HTTP_201_CREATED)
        return Response(myserializer.data, status=status.HTTP_400_BAD_REQUEST)
# -------------------------11section------------------------------------------------
