# Fast API Tutorial
## Environment 
Below is an example of creating a python environment
> pipenv install

Add packages use 
> pipenv install <package>.

Activate Pipenv shell
> pipenv shell
> python --version

More information at https://pipenv-fork.readthedocs.io/en/latest/basics.html

### Uvicorn Server
To start server use: 
>  uvicorn myapi:app --reload

Copy the link provided, add /docs to use FastAPI's UI.