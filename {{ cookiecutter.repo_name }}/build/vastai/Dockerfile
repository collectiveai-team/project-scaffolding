ARG JUPYTER_IMAGE

FROM ${JUPYTER_IMAGE}

RUN apt-get update; exit 0
RUN apt-get install -y --no-install-recommends \
    vim \
    rsync \
    git \
    git-lfs \
    && git lfs install \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root

COPY .env .

COPY ./build/vastai/vastai_setup.sh .
RUN chmod +x ./vastai_setup.sh

# Clean
RUN rm -rf /tmp/*
