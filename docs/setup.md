# Development Setup with virtualenv

The virtual environment was created with this, but you shouldn't have to run it. It was done using Python 3.8.6 installed via pyenv:

  python -m virtualenv .
  
Create the virtual environment:

  source bin/activate
  pip install -r requirements.txt
  
# Development Setup with Docker

You can also use Docker Compose to run this project. You will need to install those things on the host machine, but after that it should be pretty straightforward.

  docker build -t candy_machine .
  docker-compose up
  

# Running Tests

Because we are working in a virtual env, pytest will need to be invoked with:

  python -m pytest
