
The workflow you created so far is Ideal for pull-requests. Continous integration aims to merge code changes as frequently as possible. Therefore DevOps teams tends to avoid running havier test suites, during a pull-request. On the other hand libraries or open-source project don't necessarely have de developemetn environement. In that case, you will have to setup and run you application inside the Job using some steps prior to executing them. The first option is better corporate solutions, the second is better for open-source projects.

```yaml
name: Python application

on:
  push:
    branches: [ main ]

jobs:
  build:
    [...]
  deploy:
    [...]
  tests:
    needs: deploy
    [...]
  gating:
    needs: tests
```


```yaml
name: Python application

on:
  push:
    branches: [ main ]

jobs:
  build:
    [...]
  tests:
    needs: deploy
    steps:
    - uses: actions/checkout@master
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Download application artifact
      uses: actions/download-artifact@v2
      with:
        name: phonebook
    - name: Install Application
      run: |
        pip install phonebook-0.0.0.tar.gz
    - name: Start MongoDB
      uses: supercharge/mongodb-github-action@1.6.0
      with:
        mongodb-version: '4.4'
    - name: Run the Application
      run: |
        export FLASK_APP=phonebook 
        flask run
    # Run the tests
    [...]
```