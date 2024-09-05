# syntax=docker/dockerfile:1.3
FROM {{cookiecutter.repo_name}}-core:latest as {{cookiecutter.repo_name}}-dev
# syntax=docker/dockerfile:1.3
ENV EDITOR=vim
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV DEBIAN_FRONTEND noninteractive

ARG PIP_VERSION=23.3.2


ARG USER_NAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

RUN apt-get update && apt-get install -y sudo && \
    apt-get autoremove -y && apt-get clean && rm -rf /tmp/* /var/tmp/* && rm -rf /var/lib/apt/lists/* && \
    groupadd --gid $USER_GID $USER_NAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USER_NAME && \
    usermod -aG sudo $USER_NAME && \
    echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME && \
    chmod 0440 /etc/sudoers.d/$USER_NAME

ENV SHELL=/usr/bin/zsh
RUN chsh $USER_NAME -s $SHELL


# Install dev dependences & tools
RUN apt-get update && apt-get install -y \
    htop \
    vim \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    ssh \
    rsync \
    kmod \
    unzip \
    acl \
    zsh \
    git \
    make \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/*

WORKDIR /tmp


# Install docker
RUN curl -fsSL https://get.docker.com -o get-docker.sh \
    && sh ./get-docker.sh \
    && usermod -aG docker $USER_NAME


# install act (github actions local runner)
# https://nektosact.com/introduction.html
RUN curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/nektos/act/master/install.sh | bash && \
    mv bin/act /usr/local/bin/act


COPY ./pyproject.toml ./poetry.lock* /tmp/
RUN --mount=type=cache,target=/root/.cache/poetry \
    poetry export --format requirements.txt --without-hashes --only dev --output dev-requirements.txt && \
    pip install -r dev-requirements.txt


USER vscode
RUN poetry config virtualenvs.create false
RUN sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Custom Zsh configurations
RUN echo "autoload bashcompinit && bashcompinit" >> ~/.zshrc && \
    echo "autoload -Uz compinit && compinit" >> ~/.zshrc && \
    echo "sudo setfacl -m u:vscode:rw /var/run/docker.sock" >> ~/.zshrc && \
    echo '[ -f ".env" ] || echo -e "" > .env && export $(grep -v "^#" .env | xargs)' >> ~/.zshrc

COPY .devcontainer/entrypoint.sh /home/$USER_NAME/