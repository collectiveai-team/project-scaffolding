{% if cookiecutter.use_cuda == "yes" %} 
FROM  {{cookiecutter.base_image}}
{% else -%}
FROM ubuntu:20.04
{% endif -%}

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

ARG PYTHON_VERSION
ARG PIP_VERSION
{% if cookiecutter.pytorch_version != "no" %}    
ARG PYTORCH_VERSION
{% endif -%}
{% if cookiecutter.use_cuda == "yes" %}
ARG CUDA_VERSION
{% endif -%}

# OS packages
RUN sed -i 's/# deb-src/deb-src/' /etc/apt/sources.list \
    && apt-get update --fix-missing

RUN apt-get install -y --no-install-recommends \
    software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa

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
    ${PYTHON_VERSION} \
    ${PYTHON_VERSION}-dev \
    ${PYTHON_VERSION}-distutils \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/tmp/* /var/lib/apt/lists/*

# Set default python version
RUN update-alternatives --install /usr/bin/python python /usr/bin/${PYTHON_VERSION} 1 \
    && update-alternatives --install /usr/bin/python3 python3 /usr/bin/${PYTHON_VERSION} 1


WORKDIR /tmp

# Install pip
RUN wget https://github.com/pypa/pip/archive/refs/tags/${PIP_VERSION}.zip --no-check-certificate \
    && unzip ${PIP_VERSION}.zip \
    && cd pip-${PIP_VERSION} \
    && python setup.py install 

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
COPY ./src/{{cookiecutter.package_name}}  /tmp/{{cookiecutter.package_name}} 

RUN --mount=type=cache,target=/root/.cache \
    pip install --no-deps ./{{cookiecutter.package_name}} 

# Clean
RUN rm -rf /tmp/*

WORKDIR /root

