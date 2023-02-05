from rest_framework.views import APIView, status, Response
from django.forms.models import model_to_dict

from .utils import data_processing
from .models import Team


class TeamsView(APIView):

    def get(self, request):

        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)

        return Response(teams_dict, status.HTTP_200_OK)

    def post(self, request):
        errors = data_processing(**request.data)
        if errors:
            return Response({"error": errors.message}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)
