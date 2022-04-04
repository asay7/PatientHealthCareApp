# Healthy: A Patient Health Application
___

## Branching Strategy
- A new branch is created for each feature and is merged with the main branch if it is complete
and passes testing. Since this is a single developer project, the GitHub strategy is fairly 
simple.
___

## Testing

### REST API Testing Strategy
- Postman is used for test [PUSH, GET, DELETE] requests instead of just using
cURL. 
  - curl -X  POST http://localhost:5000/devices/D001/data -H "Content-Type: application/json" -d @Good.json

- Some unit testing will be used in addition to MockServers
Should the data server be on the same AWS flask server of on a separate DB server?


### Model Testing Strategy
 - pytest and coverage

___

## Documentation
- API documentation is generated by using sphinx, and will be hosted on readthedocs website
soon.

- Try to get the flask api up and running asap and work on the chat
- get screenshot of AWS services
```commandline
sphinx-quickstart docs
sphinx-build -b html
sphinx-autodoc -o source/ ../
make html
```
edit the conf.py and index.rst files