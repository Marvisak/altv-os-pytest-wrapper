# altv-os-pytest-wrapper

This is a resource adds commands wrapper for [pytest](https://docs.pytest.org/)

# Installation

Create a virtual environment and run this command inside it
```
pip install -r requirements.txt
```

## Usage

The command should be used like this:
```
pytest [options] [resource_name] 
```

So if you want to run tests on resource named `tests`

```
pytest tests
```

You can also pass options
```
pytest -v tests
```

If you don't pass the resource name, every resource will get tested
