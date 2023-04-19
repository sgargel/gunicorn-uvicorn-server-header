# gunicorn-uvicorn-server-header

This repo is related to `How to change/suppress server header with gunicorn and uvicorn worker class?` question on StackOverflow.

https://stackoverflow.com/a/76045740/5841817

To avoid the error below you need to use `uvicorn >= 0.15.0`

```
File "/usr/local/lib/python3.8/site-packages/uvicorn/workers.py", line 59, in __init__ 
self.config = Config(**config_kwargs) 
TypeError: __init__() got an unexpected keyword argument 'server_header'
```
