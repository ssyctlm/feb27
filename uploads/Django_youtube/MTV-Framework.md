# About MTV framework

MTV stands for **Model Template View**.
Here Model defines the data, Template defines how the data will be presented and View acts as the interface between Model, Template and the User.

![](https://raw.githubusercontent.com/ssyctlm/python_learning/master/Imagebed/MTV.png)

![MVT Pattern](https://github.com/ssyctlm/python_learning/blob/master/Imagebed/django_mvc_mvt_pattern.jpg?raw=true)

**Django** is using MTV framework(Pattern) too:

**View** is for handling the request and response.

​	The major function include URL Mapping mechanism, binding templates.

**Model** is for interacting with database.

​	Provide data access and modules, define and operate stuffs including data files,  metadata, data relationships

**Template** is for render&display the content.

​	A set of Django template page rendering language.

\* Other features:

**Form**: Generating HTML form by built-in data types and controllers.

**Admin**: Swiftly generate back-end data management website by register Models which need to be managed.