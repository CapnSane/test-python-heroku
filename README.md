# test-python-heroku

Testing new things on Heroku

## Devcenter Heroku

[Getting Started on Heroku with Node.js](https://devcenter.heroku.com/articles/getting-started-with-nodejs?singlepage=true)

### Creating the `Profile`

This file is important to control what we want to execute on Heroku.

For example, we can create a `Procfile` like this:

```python
web: npm start
run: python run.py
```

This will open two possibilities on Heroku for controlling, as we can see in the following picture:

<img src="/assets/procfile.png"/>
