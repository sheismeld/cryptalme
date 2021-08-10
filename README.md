##Hackathon

* Roadmap
1. Create virtual environnement `python3 -m venv .venv`
2. Activate venv `source .venv/bin/activate`
3. Install django `pip install django`
4. Django project creation `django-admin startproject app`
5. Move to app folder `cd app`
6. Cryptalme application creation `python manager startapp`
7. Install DRF project https://www.django-rest-framework.org

* PS: Make sure you've activate your venv and you're present in app folder before executing this command `pip install -r requirements.txt`

##Project structure
- The project's name is Cryptalme. This application will inform the user about stock's rates. It will depends on how the alerts have been defined.

###Clean architecture
- Clean architecfture is implemented for this project strongly because of source code reusability reasons. 

###Redis publish/subcribe
- Redis is used on this project in case to suscribe to channels and listen to api more to publish message. 

###COINAPI Watcher
- This Api helps on listening to events and publish them.

####Streaming data  with a websocket
- To stream data, we'll use a websocket. 
