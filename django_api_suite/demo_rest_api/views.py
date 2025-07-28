from django.http import JsonResponse
from django.views import View

class LandingAPI(View):
    name = "Landing API"
    collection_name = "your_collection_name"  # Replace with your actual collection name

    def get(self, request):
        # Example response, modify as needed
        return JsonResponse({"message": f"Welcome to the {self.name}!"})