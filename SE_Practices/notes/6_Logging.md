# Logging

Ref: https://classroom.udacity.com/courses/ud090/lessons/3b9b9174-e1ed-4121-a9d5-ac46a70e8bb6/concepts/3517e282-66c4-42a2-baa7-ef5f27f1dfa4

Logging is valuable for understanding the events that occur while running your program. 

For example, if you run your model over night and see that it's producing ridiculous results the next day, 
log messages can really help you understand more about the context in which this occurred. Lets learn about 
the qualities that make a log message effective.

- Be professional.

```sh
Bad: omg not workin!
Good: Couldn't parse file.
```

-  Be concise and use normal capitalization

```sh
Bad: Start Product Recommendation Process
Good: Generating product recommendations.
```

- Choose the appropriate level for logging

```sh
DEBUG - level you would use for anything that happens in the program.
ERROR - level to record any error that occurs
INFO - level to record all actions that are user-driven or system specific, such as regularly
```

- Provide any useful information

```sh
Bad: Failed to read location data
Good: Failed to read location data: store_id 8324971
```


Ref: https://docs.python.org/3/howto/logging.html

logging.info() or logging.debug():
 
    Report events that occur during normal operation of a program (e.g. for status monitoring or fault investigation)
    
Issue a warning regarding a particular runtime event: logging.warning():
    
    if there is nothing the client application can do about the situation, but the event should still be noted
    
logging.error(), logging.exception() or logging.critical() as appropriate for the specific error and application domain:
   
    Report suppression of an error without raising an exception: 