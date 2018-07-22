FROM python:3.6

WORKDIR /opt/project

# Install requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Install project
RUN python setup.py install

# Run bot
CMD python esgi_bot/run.py