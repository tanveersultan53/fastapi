# fastapi
FastAPI, Building A Simple CRUD Application With FastAPI.
Introduction 
FastAPI is a modern, high-performance, web framework for building Rest/APIs/Micro services with Python 3.6+ based on standard Python type hints.
FastAPI gives you the following Features.
Based on open standards¶
OpenAPI for Rest_API creation, including declarations of path operations, parameters, body requests, security, etc.
Automatic data model documentation with JSON Schema (as OpenAPI itself is based on JSON Schema).
Designed around these standards, after a meticulous(hey do things very carefully and with great attention to detail) study. Instead of an afterthought layer on top.
This also allows using automatic client code generation in many languages.

Automatic docs¶
FastAPI provide interactive API documentation and exploration web user interfaces. As the framework is based on OpenAPI, there are multiple options, 2 included by default.
Swagger UI, with interactive exploration, call and test your API directly from the browser.

Swagger Documentation.Alternative API documentation with ReDoc.

Redoc Documentation Just Modern Python¶
It's all based on standard Python 3.6 type declarations (thanks to Pydantic). No new syntax to learn. Just standard modern Python.
If you need a 2 minute refresher of how to use Python types (even if you don't use FastAPI), check the short tutorial: Python Types.
Editor support¶
All the framework was designed to be easy and intuitive to use, all the decisions were tested on multiple editors even before starting development, to ensure the best development experience.
In the last Python developer survey it was clear that the most used feature is "autocompletion".
The whole FastAPI framework is based to satisfy that. Autocompletion works everywhere.
You will rarely need to come back to the docs.
Here's how your editor might help you:
in Visual Studio Code:

Short¶
It has sensible defaults for everything, with optional configurations everywhere. All the parameters can be fine-tuned to do what you need and to define the API you need.
But by default, it all "just works".
Validation¶
Validation for most (or all?) Python data types, including:
JSON objects (dict).
JSON array (list) defining item types.
String (str) fields, defining min and max lengths.
Numbers (int, float) with min and max values, etc.
Validation for more exotic types, like:
URL.
Email.
UUID and others.

All the validation is handled by the well-established and robust Pydantic.
Security and authentication¶
Security and authentication integrated. Without any compromise with databases or data models.
All the security schemes defined in OpenAPI, including:
HTTP Basic.
OAuth2 (also with JWT tokens). Check the tutorial on OAuth2 with JWT.
API keys in:
Headers.
Query parameters.
Cookies, etc.

Plus all the security features from Starlette (including session cookies).
All built as reusable tools and components that are easy to integrate with your systems, data stores, relational and NoSQL databases, etc.
Dependency Injection¶
FastAPI includes an extremely easy to use, but extremely powerful Dependency Injection system.
Even dependencies can have dependencies, creating a hierarchy or "graph" of dependencies.
All automatically handled by the framework.
All the dependencies can require data from requests and augment the path operation constraints and automatic documentation.
Automatic validation even for path operation parameters defined in dependencies.
Support for complex user authentication systems, database connections, etc.
No compromise with databases, frontends, etc. But easy integration with all of them.

Unlimited "plug-ins"¶
Or in other way, no need for them, import and use the code you need.
Any integration is designed to be so simple to use (with dependencies) that you can create a "plug-in" for your application in 2 lines of code using the same structure and syntax used for your path operations.
Tested¶
100% test coverage.
100% type annotated code base.
Used in production applications.

Starlette features¶
FastAPI is fully compatible with (and based on) Starlette. So, any additional Starlette code you have, will also work.
FastAPI is actually a sub-class of Starlette. So, if you already know or use Starlette, most of the functionality will work the same way.
With FastAPI you get all of Starlette's features (as FastAPI is just Starlette on steroids):
Seriously impressive performance. It is one of the fastest Python frameworks available, on par with NodeJS and Go.
WebSocket support.
In-process background tasks.
Startup and shutdown events.
Test client built on requests.
CORS, GZip, Static Files, Streaming responses.
Session and Cookie support.
100% test coverage.
100% type annotated codebase.

Pydantic features¶
FastAPI is fully compatible with (and based on) Pydantic. So, any additional Pydantic code you have, will also work.
Including external libraries also based on Pydantic, as ORMs, ODMs for databases.
This also means that in many cases you can pass the same object you get from a request directly to the database, as everything is validated automatically.
The same applies the other way around, in many cases you can just pass the object you get from the database directly to the client.
With FastAPI you get all of Pydantic's features (as FastAPI is based on Pydantic for all the data handling):
No brainfuck:
No new schema definition micro-language to learn.
If you know Python types you know how to use Pydantic.
Plays nicely with your IDE/linter/brain:
Because pydantic data structures are just instances of classes you define; auto-completion, linting, mypy and your intuition should all work properly with your validated data.
Fast:
in benchmarks Pydantic is faster than all other tested libraries.
Validate complex structures:
Use of hierarchical Pydantic models, Python typing's List and Dict, etc.
And validators allow complex data schemas to be clearly and easily defined, checked and documented as JSON Schema.
You can have deeply nested JSON objects and have them all validated and annotated.
Extendible:
Pydantic allows custom data types to be defined or you can extend validation with methods on a model decorated with the validator decorator.
100% test coverage.

Setup FastAPI Application.
Install Virtual environment .

a) pip install virtualenv
b) virtualenv venv
c) source venv/bin/activate
Start by creating a new folder to hold your project called "fastapi_CRUD":
mkdir fastapi_CRUD && cd fastapi_CRUD
Install Dependencies 
pip install fastapi uvicorn
Create a New File Call App.py and write the code below 
touch app.py
First Root
# app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def ():
  return {"Framework": "FastAPI!"}
Open Your Terminal and run the following command and run the server.
Your Server is in Running State Lets Create Fake Database to store our Framework Records.
Define Framework  model.
Complete File of app.py.
app.py List of All Framework
Post Framework.
Get by ID.
Update by id
Delete by ID
