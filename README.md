# Mobile App Backend

This is the backend for the react-native mobile job application.
All functionality inside this package is as is, and there is no stable release package as of yet.

## Getting Started

Following these instructions will get you a working version of the mobile-app-backend running on localhost.

**Note:** The Authentication Server, and Rest API are two separate applications. You can run one without the other,
but will likely run into issues with the client (mobile-app-frontend) without both of them running simultaneously

Create a Virtual Environment (Python 3+)
```commandline
virtualenv --python=/usr/bin/python3 venv
```
Activate your Virtual Environment
```commandline
source venv/bin/activate
```
Install project requirements
```commandline
pip install -r requirements.txt
```

Run the authentication server
```commandline
python authentication-server.py
```

Run Ngrok (Tunneling, Dev Only; New CLI Tab / Window) for our Authentication Server
```commandline
ngrok http 5001
```
Use your ngrok server url inside the frontend-settings.


TODO FINISH DOCUMENTING.

NOTE ABOUT NGROK AND FORWARDING FOR LOCAL DEVELOPMENT

### Prerequisites

Requires Python 3.4+ and a SqlAlchemy compatible database.

### Installing

A step by step series of examples that tell you how to get a development env running

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Running tests for the authentication server
```commandline
python -m unittest tests/test_authentication_server.py
```

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With
Expo CLI, React-Native, and more.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.
## Authors

* **Brandon Curtis** - *Initial Prototype* - [TechnicalBro](https://github.com/TechnicalBro)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.