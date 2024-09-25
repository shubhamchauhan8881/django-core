from django.shortcuts import render


from rest_framework.views import APIView
from rest_framework.response import Response

from app1.models import DailyThoughts
from .serializer import DailyThoughtsSerializer

# Create your views here.
class ThoughtsApiView(APIView):
    def get(self, req):
        
        # fetcha list of thoughts
        t = DailyThoughts.objects.all()
        serilized_data = DailyThoughtsSerializer(t, many=True)

        return Response(data = serilized_data.data )


class GetSpecificThought(APIView):
    def get(self, req, pk):


        # get  filter
        # filter -> return QuerySet (LISt)
        # get -> object of models
        try:
            n = DailyThoughts.objects.get(pk=pk)
            sr = DailyThoughtsSerializer(n)
            return Response(data= sr.data)

        except:
            return Response(status=404)