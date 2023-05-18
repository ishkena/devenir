Source tutorial: https://docs.djangoproject.com/en/4.2/intro/
# Django Project Initiation
##### Understanding Django
 - Django follows an MVC architecture:
   - Model: the information that your website/application will be working with
      - Takes data from where it's stored and processes it before sending it to the View
      - Example: when signing in, the client will send a request to the Controller, which calls the Model to apply logic on the form. The Model responds with the applied logic to the Controller, which passes the response back to the client.
   - View: the presentation of the Model on the website/application; a type of webpage
      - Contains the UI logic for viewing information provided by the Model; communicates between the Model and the Template
   - Controller: the code that connects the Model and the View; where most of the code will go
      - Has the power to manipulate the View and how data is displayed to the client via the View
 - Model-View-Template (MTV) pattern:
   - Template: contains the front-end components of the website/application

##### Installation steps:
1. Install Django using PIP: ```pip install django```

Django is structured with two units:
 - A Django project is a high-level unit of organization that contains logic that governs your whole web application.
    - ```django-admin startproject <project-name> .```
    - A ```manage.py``` is created.
    - A lower-level folder is created that inherits the project name and represents the management app.
 - A Django app is a lower-level unit of your web application. You can have zero to many apps in a project.
    - ```django-admin startapp <app-name>```
    - ```__init__.py``` is used to declare a folder as a package, allowing Django to compile the web app.
    - ```models.py``` contains the app's modules, allowing Django to interface with the databases of the web app.
    - ```views.py``` is where most of the web app's logic will go.
    
##### Start with the View
Create an initial View by writing the index function:
```python
from django.http import HttpResponse
def index(request):
   return HttpResponse("Hello, world!")
```
Create a URLconf file, urls.py in the app
```python
from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='index')
]
```
Point the root URLconf to the app's URL conf
```python
from django.urls import include, path

urlpatterns = [
   path('myApp', include('myApp.urls'))
]
```
```include()``` allows Django to append a directory to the root path. The code above appends the directory ```myApp/``` to the root directory of the web server. ```path()``` is passed two required and two optional arguments:
1. ```route```: a string that contains a URL pattern, like a certain folder on the website
   - For example: in a request to ```https://www.example.com/myapp/```, the URLconf will look for the ```myapp/```
2. ```view```: if the above URL pattern is matched, a specified view function is called with an ```HttpRequest``` object as the first argument
3. ```kwargs```: Arbitrary keyword arguments can be passed in a dictionary to the target view
4. ```name```: the global name of a URL, allowing one to refer to it unambiguously in the website code, like from within templates

##### Configure the database
By default Django will use SQLite. If one wants to use another database, they'll need to install the appropriate database bindings and change the keys in the ```DATABASES default``` item to match the connection settings. Start by changing the ```TIME_ZONE``` parameter and executing ```py manage.py migrate``` in order to have Django look at the ```INSTALLED_APPS``` setting. It'll create necessary datatables according to the database settings.

##### Create models
Models are essentially the databse layout with additional metadata.
In the example app, two models are created: ```Question``` that has a question and a publish date and ```Choice``` that has the text of the choice and a vote tally. Choices are associated with questions. Python classes are used to represent a model.

```python
from django.db import models
 # each Model is created as a sub-class of Django's Model class
class Example(models.Model):
   text_field = models.CharField(max_length=200)
   date_field = models.DateTimeField('name')
   other_model = models.ForeignKey(OtherModel)
 ```

With this code, Django is able to 1) create a database schema (```CREATE TABLE```) for this app; 2) create a Python database-access API for accessing Model objects. The app now must be included in the project by adding it to the ```INSTALLED_APPS``` setting, for instance: ```myApp.apps.MyappConfig```. Finally, execute ```py manage.py makemigrations myApp``` in order to register the new Models. ```makemigrations``` tells Django that changes were made to the Models and that the changes should be stored as a _migration_. The migration is a script that runs SQL code to make the desired changes to the schema. ```py manage.py sqlmigrate myApp 0001``` will show the SQL code that would be run. Execute the migration using ```py manage.py migrate```. Note:
 - Output will depend on the database used.
 - Table names are automatically generated by combining the app name and the lowercase name of the model
 - Primary keys are added automatically
 - Django appends ```_id``` to a foreign key field name
 - The foreign key relationship is made explicit by a ```FOREIGN KEY``` constraint
 - ```sqlmigrate``` doesn't actually run the migration; it's just printed to the terminal
 - ```py manage.py check``` checks for any problems in the project without making migrations/touching the database

Thus there are three steps to making model changes:
1. Change the models in ```models.py```
2. Execute ```py manage.py makemigrations myApp```
3. Execute ```py manage.py migrate```

##### Playing with the API
In a Python shell, you can access the different Model parts:
```Python
>>> from polls.models import Choice, Question  # Import the model classes we just wrote.

# No questions are in the system yet.
>>> Question.objects.all()
<QuerySet []>

# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
>>> from django.utils import timezone
>>> q = Question(question_text="What's new?", pub_date=timezone.now())

# Save the object into the database. You have to call save() explicitly.
>>> q.save()

# Now it has an ID.
>>> q.id
1

# Access model field values via Python attributes.
>>> q.question_text
"What's new?"
>>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=datetime.timezone.utc)

# Change values by changing the attributes, then calling save().
>>> q.question_text = "What's up?"
>>> q.save()

# objects.all() displays all the questions in the database.
>>> Question.objects.all()
<QuerySet [<Question: Question object (1)>]>
```
And, after adding a self-reference string component to the class:
```python
>>> from polls.models import Choice, Question

# Make sure our __str__() addition worked.
>>> Question.objects.all()
<QuerySet [<Question: What's up?>]>

# Django provides a rich database lookup API that's entirely driven by
# keyword arguments.
>>> Question.objects.filter(id=1)
<QuerySet [<Question: What's up?>]>
>>> Question.objects.filter(question_text__startswith="What")
<QuerySet [<Question: What's up?>]>

# Get the question that was published this year.
>>> from django.utils import timezone
>>> current_year = timezone.now().year
>>> Question.objects.get(pub_date__year=current_year)
<Question: What's up?>

# Request an ID that doesn't exist, this will raise an exception.
>>> Question.objects.get(id=2)
Traceback (most recent call last):
    ...
DoesNotExist: Question matching query does not exist.

# Lookup by a primary key is the most common case, so Django provides a
# shortcut for primary-key exact lookups.
# The following is identical to Question.objects.get(id=1).
>>> Question.objects.get(pk=1)
<Question: What's up?>

# Make sure our custom method worked.
>>> q = Question.objects.get(pk=1)
>>> q.was_published_recently()
True

# Give the Question a couple of Choices. The create call constructs a new
# Choice object, does the INSERT statement, adds the choice to the set
# of available choices and returns the new Choice object. Django creates
# a set to hold the "other side" of a ForeignKey relation
# (e.g. a question's choice) which can be accessed via the API.
>>> q = Question.objects.get(pk=1)

# Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

# Create three choices.
>>> q.choice_set.create(choice_text="Not much", votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text="The sky", votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text="Just hacking again", votes=0)

# Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

# And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
>>> Choice.objects.filter(question__pub_date__year=current_year)
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>

# Let's delete one of the choices. Use delete() for that.
>>> c = q.choice_set.filter(choice_text__startswith="Just hacking")
>>> c.delete()
```


##### Introducing the Django Admin
The Django admin portal allows admin users to view and edit Models. Steps to use:
 - Create an admin user
   - Execute ```py manage.py createsuperuser```
   - Enter the desired username
   - Enter the desired email address
   - Enter the desired password
- Visit ```http://127.0.0.1:8000/admin/```
   - The default ```groups``` and ```users``` types are provided by ```django.contrib.auth```
- Add models
   - ```python
      # in myApp/admin.py
      from django.contrib import admin
      from .models import Question
      admin.site.register(Question)
     ```

##### The View
###### Basic Operation
A view is a "type" of webpage in the web app that serves a specific function and uses a specific template. For instance, a blog homepage, comment action, entry detail page, or archive pages would all be implemented using views. Content is delivered by views via the URLconf, that links the views to a visitable URL. Each view is defined by a function that takes at least the ```request``` argument:
```python
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)
```
That view function is then connected to the app's URLconf by adding the path to the ```urlpatterns``` list:
```python
# Example: /polls/results/
path('<int:question_id>/results/', views.results, name='results')
```
When somebody requests a page from your website – say, “/polls/34/results”, Django will load the ```mysite.urls``` Python module because it’s pointed to by the ```ROOT_URLCONF``` setting. It finds the variable named ```urlpatterns``` and traverses the patterns in order. After finding the match at 'polls/', it strips off the matching text ("polls/") and sends the remaining text – "34/" – to the ```polls.urls``` URLconf for further processing. There it matches ```<int:question_id>/```, resulting in a call to the ```results()``` view.
###### Expanding Functionality
One can use the Django database API to fetch the web app's information:
```python
from django.http import HttpResponse
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
```
The page's design is now hard-coded into the view. Django's template system alleviates this. A directory will need to be created: ```myProject/myApp/templates/myApp/index.html```. Django will assume your template is in ```myProject/myApp/templates```, so it's necessary to specify the app again. In the template you can place the code below. Ideally, [complete HTML documents](https://developer.mozilla.org/en-US/docs/Learn/HTML/Introduction_to_HTML/Getting_started#anatomy_of_an_html_document) are used.
```html
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
In order to use the template, we'll need to pass it a context using a dictionary:
```python
from django.http import HttpResponse
from django.template import loader
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("myApp/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```
###### View Shortcuts
However, this template, context, ```HttpResponse``` combination is very common. Thus, ```render(request, template_name, optional=dictionary)``` is provided as a shortcut. With this, only render is needed as opposed to loading both HttpResponse and loader.
```python
from django.shortcuts import render
def index(request):
   latest_question_list = Question.objects.order_by("-pub_date")[:5]
   context = {"latest_question_list": latest_question_list}
   return render(request, "polls/index.html", context)
```
In order to raise a 404 error, the import statement ```from django.html import Http404``` is needed along with a try-except structure with the except containing ```raise Http404("Error text here")```. However, the shortcut ```get_object_or_404()``` is provided via ```from django.shortcuts import get_object_or_440```. 
##### The Template System
The template system uses [dot-lookup syntax](https://docs.djangoproject.com/en/1.8/ref/templates/api/#variables-and-lookups) to access variable attributes. Method calling happens in the ```{% for %}``` loop.
By using the {% url %} template tag, one can remove reliance on specific URL paths:
```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/myApp/{{question.id}}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
Versus below, which allows one to make all necessary changes in urls.py:
```python
{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```
###### Namespacing
Namespacing allows one to use the same url name for several apps within a project. In the URLconf ```myApp/urls.py```, add ```app_name = 'myApp'```, setting the app namespace. In any template, names need to be invoked using ```{% url 'myApp:myUrl' question.id %}```.
###### Forms (?)
```html
<form action="{% url 'myApp:myView' question.id %}" method="post"> <!-- Invokes POST HTML method and links in URL -->
{% csrf_token %} <!-- This protects against Cross-Site Request Forgeries -->
    <fieldset>
        <legend><h1>{{ question.question_text }}</h1></legend> <!-- Writes out the question -->
        {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
        {% for choice in question.choice_set.all %}
            <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
            <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
        {% endfor %}
    </fieldset>
    <input type="submit" value="Vote">
</form>
```
##### Generic Views
Generic views abstract common patterns in order to reduce redundant views. Steps to convert to generic views are:
1. Convert the URLconf
   - Before: ```python path('<int:question_id>/', views.detail, name='detail')```
   - After: ```python path('<int:pk>/', views.DetailView.as_view(), name='detail')```
2. Delete unneeded views
3. Introduce the new, generic views
    - Use a class form for the view, where ```model``` must be passed, and ```template_name``` overrides the default path expected
    - ```python
      class ResultsView(generic.DetailView):
        model = Question
        template_name = "polls/results.html"
      ```

##### Testing
One can either spend their time hand-testing an app, or one can build a test sub-class that does it automatically:
```python
import datetime

from django.test import TestCase
from django.utils import timezone
from .models import Question

class QuestionModelTests(TestCase):
    def test_test_case_name(self):
        '''
        Description of the test case.
        '''
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_pub_recently(), False)
```
To use this test case, execute ```py manage.py test myApp```, which will return testing output into the console. The process:
 - ```manage.py test myApp``` looks for tests in the ```myApp``` application
 - Finds a subclass of ```django.test.TestCase``` class
 - Creates a special database for testing the function
 - Looks for test methods (methods that begin with 'test')
 - It executes the test method, creating a ```Question``` instance with ```pub_date``` 30 days in the future
 - Uses the ```assertIs()``` method to check whether the test method will return the desired output

##### Static Files
Web applications generally need to server static files to the client aside from the dynamic HTML generated by the server. ```django.contrib.staticfiles``` collects the static files (such as images, JS, and CSS) into a single location.
1. Create a directory ```static``` in the ```myApp``` folder
2. Create a ```myApp``` directory in the new ```static``` folder
3. Add the static files there
