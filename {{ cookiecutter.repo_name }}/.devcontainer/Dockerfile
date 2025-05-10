FROM ubuntu:24.04 AS devcontainer


ENV EDITOR=vim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive
ENV PATH=/usr/local/cuda/bin/:$PATH

# Install UV & python
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Install basic tools
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    # utils
    ssh \
    rsync \
    acl \
    zsh \
    htop \
    make \
    vim \
    curl \
    sudo \
    lsof \
    git-core \
    ca-certificates \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

ARG DEVCONTAINER_USER=ubuntu
RUN usermod -aG sudo $DEVCONTAINER_USER \
    && passwd -d $DEVCONTAINER_USER

ENV SHELL=/usr/bin/zsh
RUN chsh $DEVCONTAINER_USER -s $SHELL

# Install docker
RUN curl -fsSL https://get.docker.com | sh && \
    usermod -aG docker $DEVCONTAINER_USER

#######################################################################################
# Customizations
#######################################################################################
USER $DEVCONTAINER_USER
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Custom Zsh configurations
RUN echo "autoload bashcompinit && bashcompinit" >> ~/.zshrc && \
    echo "autoload -Uz compinit && compinit" >> ~/.zshrc && \
    echo "sudo setfacl -m u:ubuntu:rw /var/run/docker.sock" >> ~/.zshrc

# Global envs
ENV UV_CACHE_DIR=/workspace/resources/cache/uv


WORKDIR /workspace
COPY .devcontainer/entrypoint.sh /home/$DEVCONTAINER_USER/
