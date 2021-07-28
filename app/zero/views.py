import json
from django.shortcuts import render

from django.http import JsonResponse

from adapters.django_storage import DjangoStorage
from notes.use_cases import UseCases 

storage = DjangoStorage()
use_cases = UseCases(storage)
def create_board(request):
    req_data = json.loads(request.body) 
    board = use_cases.create_board(
        title=req_data['title'],
        body=req_data['body'] )
    return JsonResponse({'board': board.to_dict()}, status=200
)