

# How to update dependencies for a package
Following either one of the following ways to update dependencies for a package.

* Manually edit pyproject.toml
```
> cd packages/my_pkg
# Then edit pyproject.toml to add/remove desired dependencies

# back to project root
> cd - 
> poetry update packages/my_pkg
```
* Another way, run poetry add. Note that this might generate poetry.lock in packages/my_pkg. But it is git-ignored.
```
> cd packages/my_pkg

> poetry add my_dependency
# > rm -rf poetry.lock  # optional 

# back to project root
> cd - 
> poetry update packages/my_pkg
```


