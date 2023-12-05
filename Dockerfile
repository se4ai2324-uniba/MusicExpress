FROM python:3.11.6
RUN pip install --upgrade pip
COPY . .
RUN pip install -r requirements.txt
WORKDIR /src
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]