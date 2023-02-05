from rest_framework.views import APIView, status, Response, Request
from django.forms.models import model_to_dict

from .utils import data_processing
from .models import Team


class TeamsView(APIView):

    def get(self, request: Request) -> Response:

        teams = Team.objects.all()
        teams_dict = []

        for team in teams:
            t = model_to_dict(team)
            teams_dict.append(t)

        return Response(teams_dict, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        errors = data_processing(**request.data)
        if errors:
            return Response({"error": errors.message}, status.HTTP_400_BAD_REQUEST)

        team = Team.objects.create(**request.data)
        team_dict = model_to_dict(team)
        return Response(team_dict, status.HTTP_201_CREATED)


class TeamDetailView(APIView):

    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for key, value in request.data.items():
            setattr(team, key, value)

        team.save()
        team_dict = model_to_dict(team)

        return Response(team_dict, status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(id=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
