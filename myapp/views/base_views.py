from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

# Import the ICF and RCF algorithms
from .icf_algorithm import icf_algorithm
from .rcf_algorithm import rcf_algorithm

# Import the scrm_algorithm and Word2Vec model
from .scrm_algorithm import scrm_algorithm


def index(request):
    return HttpResponse("This is for ICF, RCF and SCRM algorithm")


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for simplicity
def icf_view(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request body
            data = json.loads(request.body.decode('utf-8'))
            sentences = data.get('sentences', [])

            # Ensure sentences are provided
            if not sentences:
                return JsonResponse({'error': 'No sentences provided'}, status=400)

            # Call the ICF algorithm function
            processed_sentences = icf_algorithm(sentences)

            # Return the processed sentences as a JSON response
            return JsonResponse({'processed_sentences': processed_sentences})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for simplicity
def rcf_view(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request body
            data = json.loads(request.body.decode('utf-8'))
            sentences = data.get('sentences', [])
            delta = data.get('delta', 1)  # Default value for delta

            # Ensure sentences are provided
            if not sentences:
                return JsonResponse({'error': 'No sentences provided'}, status=400)

            # Call the RCF algorithm function
            processed_sentences = rcf_algorithm(sentences, delta)

            # Return the processed sentences as a JSON response
            return JsonResponse({'processed_sentences': processed_sentences})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@method_decorator(csrf_exempt, name='dispatch')  # Disable CSRF for simplicity
def scrm_view(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON request body
            data = json.loads(request.body.decode('utf-8'))
            sentences = data.get('sentences', [])
            delta = data.get('delta', 0.8)  # Default value for delta

            # Ensure sentences are provided
            if not sentences:
                return JsonResponse({'error': 'No sentences provided'}, status=400)

            # Call the scrm_algorithm function
            processed_sentences = scrm_algorithm(sentences, delta)

            # Return the processed sentences as a JSON response
            return JsonResponse({'processed_sentences': processed_sentences})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
