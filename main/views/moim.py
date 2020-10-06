from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import generics, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
import json

from main.models import Plan


class MoimListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ('planId', 'name', 'startTime', 'endTime', 'progressTime', 'date')


# class MoimListView(generics.ListAPIView):
#     queryset = Plan.objects.all()
#
#     def get(self, request):
#         data = json.loads(serializers('json', self.queryset))
#         dummy_data = {
#             'name': '죠르디',
#             'type': '공룡',
#             'job': '편의점알바생',
#             'age': 5
#         }
#         return JsonResponse(dummy_data)
#
#     def post(self, request):
#         return HttpResponse("Post 요청을 잘받았다")
#
#     def put(self, request):
#         return HttpResponse("Put 요청을 잘받았다")
#
#     def delete(self, request):
#         return HttpResponse("Delete 요청을 잘받았다")

# api/moim 으로 get하면 이 listview로 연결
class MoimListView(generics.ListAPIView):
    queryset = Plan.objects.all()
    serializer_class = MoimListSerializer

    def get(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)

    def post(self, request):
        if request.META['CONTENT_TYPE'] == "application/json":
            request = json.loads(request.body)
            plan = Plan(planId=request['planId'],
                        name=request['name'],
                        startTime=request['startTime'],
                        endTime=request['endTime'],
                        progressTime=request['progressTime'],
                        date=request['date'])
        else:
            plan = Plan(planId=request.POST['planId'],
                        name=request.POST['name'],
                        startTime=request.POST['startTime'],
                        endTime=request.POST['endTime'],
                        progressTime=request.POST['progressTime'],
                        date=request.POST['date'])
        plan.save()
        return HttpResponse(status=200)

