
I have always been intrigued by this book: https://www.pycabook.com/

however somthing was missing. In the toturial we implement 4 types of datalayer but we hard coded them in the request handler. two problem arise from that:
* The request handler is eavily couple with the data layer
* The dabase object is initialized everytime we call the request handler

I decided in this tutorial to tackle the incomplete part of this book.

This tutoral will help you discover what is the canonical way to deal with database connection.

Lest all start from the same base by forking the orignial toturial in it final stage. Now run the test

start the application

Test the application to understand it behaviour

## Refactoring the database Management

### Initializing the database

```
flask init-db
```

### Dependency injection

## References

* https://flask.palletsprojects.com/en/2.0.x/tutorial/database/
* https://www.pycabook.com/
* https://levelup.gitconnected.com/python-dependency-injection-with-flask-injector-50773d451a32