Module is written in python. Some parts of code were derived from python-calais project.
Module uses demjson (You may download it from http://deron.meranda.us/python/demjson/)

---

This module is intended to be as simple, straighforward and standards-compliant as possible. To use the library:
- instantiate Calais class and call analyze() method with your text as an argument.
- returned result is a native python dictionary

---

Example:
```
API_KEY = "your-api-key"
calais = CalaisJSON.Calais(API_KEY)

calais_response = calais.analyze('your text goes here')  #calais_response is a dictionary
```

