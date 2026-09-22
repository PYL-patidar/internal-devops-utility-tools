#base image of python
FROM python:3.14

# workdir for store code
WORKDIR /app

#copy code from local to workdir
COPY . /app

# run requirements 
RUN pip install -r requirements.txt

# port identify
EXPOSE 8000

# run the application
CMD [ "python", "main.py" ] 
