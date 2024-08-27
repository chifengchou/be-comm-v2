
# Demo of multi-package project structure

* Each package is a standalone python project. Each has its own `pyproject.toml` and **its own set of dependencies**.
* Each package is namespaced[*1] under **gzw**. So there must be NO `__init__.py` directly under **gzw**.
* A package may depend on other packages.
* In root, there is a `pyproject.toml` and `poetry.lock` to set up a dev virtual env.
* Tests for each package is managed in the root project.
* **ALL** packages are listed as dev-dependencies in root `pyproject.toml`. Aside from testing, this ensures that dependency conflicts between packages will be captured early during development.


We envisage be-comm-v2 will a submodule of applications instead of being 
released to PyPi.

Using PyPi to distribute packages means that versions of packages must be 
properly managed because the version will be part of a dependency.
While version-dependency does offer a great flexibility, we don't find it 
particularly useful in our use cases.

On the another hand, using submodule instead of PyPi has some benefits:
1. reduces the friction of setting up tooling to access a private PyPi.
2. no need for versioning of packages.
3. allow path-dependency between packages.

In this demo project, all package-to-package or root-to-package dependencies
are path-dependencies. Path-dependency allows one to access a dependency 
directly from the local folder, a.k.a. **editable install**. This greatly 
accelerates the development cycle. 


Having said that, we can always switch in the future if we find PyPi useful[*2].

[*1] https://packaging.python.org/en/latest/guides/packaging-namespace-packages/

[*2] That entails to change path-dependency to version-dependency on-the-fly. 
Poetry does not support it out-of-box but there are some plugins available.

# Install

```shell
❯ python --version
Python 3.11.5
❯ python -m venv .venv
❯ source .venv/bin/activate
❯ poetry install --sync --no-root --with dev
❯ poetry run pytest
```


# How to update dependencies for a packages/my_pkg
```
> cd packages/my_pkg
> poetry add my_dependency
> rm -rf ./poetry.lock  # optional 

# back to project root
> cd - 
> poetry remove my_pkg
> poetry add -e packages/my_pkg
```


