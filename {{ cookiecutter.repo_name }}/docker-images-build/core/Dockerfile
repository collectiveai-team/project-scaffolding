{% if cookiecutter.use_cuda == "yes" %} 
FROM  {{cookiecutter.base_image}}
{% else -%}
FROM python:{{cookiecutter.python_version}}
{% endif -%}

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

ARG PYTHON_VERSION=python{{ cookiecutter.python_version}}
ARG PIP_VERSION=23.3.2

{% if cookiecutter.pytorch_version != "no" -%}  
ARG PYTORCH_VERSION={{ cookiecutter.pytorch_version }}
{% endif -%}
{% if cookiecutter.use_cuda == "yes" -%}
ARG CUDA_VERSION={{ cookiecutter._pythorch_cuda_version_map.get(cookiecutter.pytorch_version, '') }}

# OS packages
RUN sed -i 's/# deb-src/deb-src/' /etc/apt/sources.list \
    && apt-get update --fix-missing

RUN apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa
{% endif %}

# OS packages
RUN apt-get update --fix-missing; exit 0
RUN apt-get install -y --no-install-recommends \
    curl \
    wget \
    git-core \
    htop \
    unzip \
    zsh \
    vim \
    parallel \
    gcc \
    python3-setuptools \
{% if cookiecutter.use_cuda == "yes" -%}
    ${PYTHON_VERSION} \
    ${PYTHON_VERSION}-dev \
    ${PYTHON_VERSION}-distutils \
{% endif %}
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/tmp/* /var/lib/apt/lists/*


{% if cookiecutter.use_cuda == "yes" -%}
# Set default python version
RUN update-alternatives --install /usr/bin/python python /usr/bin/${PYTHON_VERSION} 1 \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/${PYTHON_VERSION} 1
{% endif %}

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python - --version 1.8.4 && \
  cd /usr/local/bin && \
  ln -s /opt/poetry/bin/poetry && \
  poetry config virtualenvs.create false


WORKDIR /tmp

# Install pytorch
{% if cookiecutter.pytorch_version != "no" -%}
{% if cookiecutter.use_cuda == "yes" -%}
RUN --mount=type=cache,target=/root/.cache \
    pip install torch==${PYTORCH_VERSION}+${CUDA_VERSION} \
    -f https://download.pytorch.org/whl/${CUDA_VERSION}/torch_stable.html
{% else -%}
RUN --mount=type=cache,target=/root/.cache \
    pip install torch==${PYTORCH_VERSION}
{% endif -%}
{% endif %}

# Install {{cookiecutter.package_name}} 
COPY ./{{cookiecutter.package_name}}  /tmp/{{cookiecutter.package_name}} 
COPY ./pyproject.toml /tmp/pyproject.toml

RUN --mount=type=cache,target=/root/.cache \
    poetry lock && poetry install --no-dev
# Clean
RUN rm -rf /tmp/*

WORKDIR /root

