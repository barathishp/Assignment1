from django.shortcuts import render


from django.http import JsonResponse
from asgiref.sync import sync_to_async
from .models import AsyncExample

async def create_async_data(request):
    new_data = await sync_to_async(AsyncExample.objects.create)(
        name="Async Example",
        description="This is an asynchronous example"
    )
    return JsonResponse({'message': 'Data created successfully'})

async def get_async_data(request):
    async_data = await AsyncExample.objects.all()
    data_list = [{'name': obj.name, 'description': obj.description} for obj in async_data]
    return JsonResponse({'data': data_list})

async def update_async_data(request, object_id):
    async_obj = await sync_to_async(AsyncExample.objects.get)(id=object_id)
    async_obj.name = "Updated Async Example"
    await sync_to_async(async_obj.save)()
    return JsonResponse({'message': 'Data updated successfully'})
