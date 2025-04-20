# syntax=docker/dockerfile:1
ARG PYTHON_VERSION=3.12

#
# Stage 1
#

# FROM node:21-slim AS node-build

# RUN mkdir -p /usr/src/app
# WORKDIR /usr/src/app

# COPY package*.json .
# RUN npm install
# RUN npm install tailwindcss @tailwindcss/cli
# COPY . .
# RUN npx @tailwindcss/cli -i ./staticfiles/css/input.css -o ./staticfiles/css/output.css

#
# Stage 2
#

FROM python:${PYTHON_VERSION}-slim as base

ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

RUN mkdir -p /usr/src/backend
WORKDIR /usr/src/backend

RUN pip install --upgrade pip

COPY requirements.txt .

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r ./requirements.txt

COPY . .