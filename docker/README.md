# Docker

**Docker** is a containerization platform that enables the **packaging**, **distribution**, and **execution** of applications within **lightweight**, **isolated environments** called **containers**.

This tool is very useful because it ensures **consistency** across **different environments**.

## How we created a Docker Container

Firstly, we installed the Docker library and initialized it in our repository using the command:

```bash
docker init
```

This command generated the following files: Dockerfile and docker-compose.yaml.

In the Dockerfile, we defined the container's behavior as follows:

```bash
FROM python:3.11.6
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
WORKDIR /src
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
```

Following a concise explanation of the content of the Dockerfile:

We specify the **base image** as Python 3.11.6 available on [Python's Docker Hub page](https://hub.docker.com/_/python). Following that, we **upgrade pip**, **copy the entire current directory** into the container, and **install project dependencies** (requirements.txt). The working directory is switched to "/src" and, to enable external connections, we **expose port 8000** within the container. Finally, we state the **command** that executes the **UVicorn server to run our API**.

With the following command, we create **a Docker image** named "**musicexpress**" with version "**1.0**," utilizing the current directory as the build context.

```bash
docker build -t musicexpress:1.0 .
```

The resulting image is visible in [Docker Desktop](https://www.docker.com/products/docker-desktop/), as illustrated below:

![plot](/figures/docker_image.png?raw=true)

Subsequently, we **launch the built image**, establishing a **mapping** between **host port 8000** and **container port 8000** for external application access.

```bash
docker run -p 8000:8000 musicexpress:1.0
```

![plot](/figures/docker_container.png?raw=true)

This procedure grants access to the Swagger UI, providing a user-friendly interface for interacting with our API. In our specific case, you can access the Swagger UI at:

```bash
http://localhost:8000/docs
```

or

```bash
http://127.0.0.1:8000/docs
```

![plot](/figures/docker_result.png?raw=true)

More information about this tool can be found [here](https://docs.docker.com/). Other images can be found on [Docker Hub](https://hub.docker.com/).
