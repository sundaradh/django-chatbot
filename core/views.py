import random
import json
import torch
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .model import NeuralNet
from .nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load intents from the JSON file
with open('intents.json', 'r') as json_data:
    intents = json.load(json_data)

FILE = "data.pth"
data = torch.load(FILE)
input_size = data["input_size"]
hidden_size = data["hidden_size"]
output_size = data["output_size"]
all_words = data['all_words']
tags = data['tags']
model_state = data["model_state"]

# Initialize the neural network model
model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

bot_name = "Sam"


def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to(device)

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.75:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])

    return "Sorry 😣, I do not understand..."


class ChatView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        try:
            raw_data = request.body.decode('utf-8')
            if not raw_data:
                return JsonResponse({"message": "Empty request body"}, status=400)

            data = json.loads(raw_data)
            print("Received JSON data:", data)  # Add this line for debugging

            if 'message' in data:
                user_message = data['message']
                response = get_response(user_message)
                return JsonResponse({"message": response})
            else:
                return JsonResponse({"message": "Invalid request format"}, status=400)

        except json.JSONDecodeError as e:
            print("Error parsing JSON data", e)
            return JsonResponse({"message": "Invalid JSON data"}, status=400)
