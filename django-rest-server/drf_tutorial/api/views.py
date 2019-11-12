from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PhoneSerializer
from .models import Phone

# Create your views here.

class PhoneBook(APIView):
  # 전화번호부 리스트 조회
  def get(self, request, format=None):
    queryset = Phone.objects.all()
    serializer = PhoneSerializer(queryset, many=True)
    return Response(serializer.data)

  # 전화번호부 아이템 추가
  def post(self, request, format=None):
    serializer = PhoneSerializer(data=request.data)
    flag = False

    if serializer.is_valid():
      serializer.save()
      flag = True

    return Response({flag: flag}, status=status.HTTP_201_CREATED if flag else status.HTTP_400_BAD_REQUEST)

  # 전화번호부 아이템 제거
  def delete(self, request, format=None):
    id = request.data.get('id')
    post = Phone.objects.get(id=id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)