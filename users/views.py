from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from .models import UserModel
from rest_framework.response import Response
from .serializers import UserSerializer
from rest_framework import status

# create POST
# read GET
# update PUT/PATCH
# delete DELETE


class ListCreateView(APIView):

    def get(self, *args, **kwargs):
        db_users = UserModel.objects.all()
        users = UserSerializer(db_users, many=True).data
        print(users)
        return Response(users, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class ReadUpdateDelete(APIView):

    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # user = UserModel.objects.get(pk=pk)
        user = get_object_or_404(UserModel.objects.all(), pk=pk)  # when you request non-existent id
        data = UserSerializer(user).data
        return Response(data, status.HTTP_200_OK)


# class UserView(APIView):

    # def get(self, *args, **kwargs):
    #     return Response('hello from get')
    #
    # def post(self, *args, **kwargs):
    #     return Response('hello from post')
    #
    # def put(self, *args, **kwargs):
    #     return Response('hello from put')
    #
    # def patch(self, *args, **kwargs):
    #     return Response('hello from patch')
    #
    # def delete(self, *args, **kwargs):
    #     return Response('hello from delete')
