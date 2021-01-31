FROM python:3-slim

ADD src/requirements.txt /opt/requirements.txt
ADD docker/entrypoint.sh /opt/entrypoint.sh
RUN apt-get update && \
    apt-get -y install cron && \
    pip install --disable-pip-version-check -r /opt/requirements.txt

ADD src/do-ddns.py /opt/do-ddns.py
RUN chmod +x /opt/do-ddns.py /opt/entrypoint.sh

ENTRYPOINT /opt/entrypoint.sh
