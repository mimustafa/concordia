FROM ubuntu:18.04

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app
ENV DJANGO_SETTINGS_MODULE=concordia.settings_prod

ENV DEBIAN_FRONTEND="noninteractive"

# Pillow/Imaging: https://pillow.readthedocs.io/en/latest/installation.html#external-libraries
RUN apt-get update -qy && apt-get install -o Dpkg::Options::='--force-confnew' -qy \
    git curl \
    python3 python3-dev python3-pip \
    libtiff-dev libjpeg-dev libopenjp2-7-dev libwebp-dev zlib1g-dev \
    graphviz

COPY requirements_importer.txt ./
COPY requirements_devel.txt ./
COPY requirements.txt ./
COPY vendor /vendor
RUN pip3 install -r requirements_devel.txt

WORKDIR /app
COPY . .
RUN pip3 install --no-cache-dir -e .

EXPOSE 80
CMD [ "/bin/bash", "entrypoint.sh" ]
