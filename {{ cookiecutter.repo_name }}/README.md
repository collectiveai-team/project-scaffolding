{{cookiecutter.project_name}}
==============================

{{cookiecutter.description}}


Project Organization
------------

```
.
├── .devcontainer                           -> Docker devcontainer building files & utils
├── notebooks                               -> Notebooks with experimentes and examples
│   └── ...
├── reports                                 -> Reports generated by results from experiments
│   └── ...
├── resources                               -> general resources: models, datasets, cache, etc
│   ├── cache
│   ├── models
│   ├── datasets
│   └── ...
├── scripts                                 -> utils
└── {{cookiecutter.package_name}}           -> main root of package  
```


<p><small>Project based on the <a target="_blank" href="https://github.collective.com/DataScience/project-scaffolding/">cookiecutter data science collective template</a>. #cookiecutterdatasciencecollective</small></p>



### Installation
1. Clone the repository:
   ```
   git clone {{ cookiecutter.git_repo_url }}
   ```


### VS Code development environment
1. Install the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension for [VS Code](https://code.visualstudio.com/).
2. Open the project in VS Code.
3. Click on the green button in the bottom left corner of the VS Code window and select the `Reopen in Container` option. Alternatively, you can run the `Remote-Containers: Reopen in Container` command from the Command Palette (`Ctrl+Shift+P`).
4. VS Code will automatically build the Docker images and start the containers. This may take a few minutes. Once the containers are up and running, you can start developing in the VS Code development environment.

## Contributors
- {{ cookiecutter.author_name }} - [@{{ cookiecutter.author_user }}](https://github.com/{{ cookiecutter.author_user }}) at [collective.ai](https://collectiveai.io) ([email](mailto:{{ cookiecutter.author_email }}))


## Contributing
We welcome contributions to {{ cookiecutter.project_name }} Feel free to submit a pull request with your changes or open an issue if you have any questions or suggestions.