FROM python:3.7

WORKDIR /opt/project

# Install requirements first
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Install project
RUN python setup.py install

# Run bot
ENTRYPOINT run_bot