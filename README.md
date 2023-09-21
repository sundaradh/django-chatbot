Django Chatbot Project
Introduction
This repository provides a simple example of deploying a chatbot using Django. The chatbot is powered by PyTorch and designed to respond to various intents and messages. You can customize the chatbot's behavior by modifying the intents.json file.

Initial Setup
To get started, follow these steps:

Clone the repository and navigate to the project directory:

shell
Copy code
$ git clone https://github.com/sundaradh/django-chatbot.git
$ cd django-chatbot
Create a virtual environment and activate it:

shell
Copy code
$ python3 -m venv venv
$ source venv/bin/activate  # On Windows, use: venv\Scripts\activate
Install the required dependencies:

shell
Copy code
(venv) $ pip install Django torch torchvision nltk
Install the NLTK package and download the necessary data:

shell
Copy code
(venv) $ python
>>> import nltk
>>> nltk.download('punkt')
Customization
You can customize the chatbot's behavior by modifying the intents.json file. Add different intents and responses to make the chatbot respond to a variety of user queries and messages.

Training the Chatbot
To train the chatbot, run the following command:

shell
Copy code
(venv) $ python train.py
Save to grepper
This will generate a data.pth file containing the chatbot's training data.

Testing the Chatbot
To test the chatbot in the console, run:

shell
Copy code
(venv) $ python chat.py
Save to grepper
This will allow you to interact with the chatbot and see how it responds to different inputs.

Running the Django Application
To run the Django application and access the chatbot via a web interface, follow these steps:

Migrate the database:

shell
Copy code
(venv) $ python manage.py migrate
Create a superuser (admin):

shell
Copy code
(venv) $ python manage.py createsuperuser
Start the Django development server:

shell
Copy code
(venv) $ python manage.py runserver
Access the admin panel at http://localhost:8000/admin/ and log in with the superuser credentials you created earlier.

Add intents and responses via the Django admin panel or by modifying the intents.json file and retraining the chatbot.

Access the chatbot API at http://localhost:8000/api/chat/ to interact with the chatbot.

Feel free to modify and customize the chatbot and its behavior according to your project requirements within the Django framework.