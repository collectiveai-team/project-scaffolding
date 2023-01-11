# syntax=docker/dockerfile:1.3
FROM {{cookiecutter.repo_name}}-core:latest
ENV EDITOR=vim

ARG USER_NAME=vscode
ARG USER_UID
ARG USER_GID

RUN groupadd --gid $USER_GID $USER_NAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME \
    && apt-get update \
    && apt-get install -y sudo \
    && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME \
    && chmod 0440 /etc/sudoers.d/$USER_NAME \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

ENV SHELL=/usr/bin/zsh
RUN chsh $USER_NAME -s $SHELL

# persistent history
RUN SNIPPET="export PROMPT_COMMAND='history -a' && export HISTFILE=/commandhistory/.zsh_history" \
    && mkdir /commandhistory \
    && touch /commandhistory/.zsh_history \
    && chown -R $USER_NAME /commandhistory \
    && echo $SNIPPET >> "/home/$USER_NAME/.zshrc"


# Install dev dependences & tools
RUN apt update && apt install -y \
    htop \
    vim \
    git-lfs \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    ssh \
    rsync \
    kmod \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*


# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
COPY .devcontainer/requirements.txt .devcontainer/entrypoint.sh /home/$USER_NAME/

RUN --mount=type=cache,target=/root/.cache,id=pip \
    pip install -r /home/$USER_NAME/requirements.txt \
    && rm -rf /home/$USER_NAME/requirements.txt


USER $USER_NAME
WORKDIR /tmp
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
