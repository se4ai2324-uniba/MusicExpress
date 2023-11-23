# API

To produce the API for our system we used:

- **FastAPI**: a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.

## FastAPI

FastAPI is employed in the [main](../main.py) in which, after initializing the FastAPI framework, we create endpoints for our system functionalities, such as:

- data extraction,
- music recommendations.

Running the command:

```bash
uvicorn main:app --reload
```

will start the FastAPI server, and, thanks to the Swagger UI, you can interact with and explore the defined endpoints. The Swagger UI provides a user-friendly interface for testing and understanding the API functionalities. Below is a screenshot of the Swagger UI showcasing the available endpoints and their details:

![plot](/figures/fastapi_swagger.png?raw=true)

To access the Swagger UI, open your web browser and navigate to:

```bash
http://127.0.0.1:8000/docs
```

This interface dynamically documents the available endpoints, their input parameters, and allows you to make requests directly from the browser. Below

More information about this tool can be found [here](https://fastapi.tiangolo.com/).
