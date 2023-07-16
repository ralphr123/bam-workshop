FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gnupg2

COPY . .

ARG PASSPHRASE
RUN echo $PASSPHRASE | gpg --quiet --batch --yes --passphrase-fd 0 --output=.env .env.gpg

# Create and activate the virtual environment
RUN python -m venv venv
RUN . venv/bin/activate

# Install required packages inside the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./main.py" ]
