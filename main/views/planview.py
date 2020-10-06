from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from main.views.moim import MoimListSerializer


class PlanView(APIView):
    def get(self, request):
        return Response("ok", status=200)

    def post(self, request):
        plan_serializer = MoimListSerializer(data=request.data)

        if plan_serializer.is_valid():
            plan_serializer.save()
            return Response(plan_serializer, status=status.HTTP_201_CREATED)
        else:
            return Response(plan_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        return Response("ok", status=200)

    def delete(self, request):
        return Response("ok", status=200)  
