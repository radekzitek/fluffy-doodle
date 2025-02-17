# Django Project Setup

Let's break down how to structure your Django project directories for a web application backend, especially considering Django authentication and custom data models. A well-organized structure is crucial for maintainability, scalability, and collaboration.

Here's a recommended directory structure, along with explanations for each part:

```python
myproject/             (Project Root - You choose this name)
├── manage.py
├── myproject/          (Inner Project Directory - Same name as root, but Python package)
│   ├── __init__.py
│   ├── settings.py       (Project-level settings)
│   ├── urls.py           (Project-level URL configurations)
│   ├── asgi.py           (ASGI configuration for asynchronous support)
│   └── wsgi.py           (WSGI configuration for web server)
├── apps/                (Container for your Django Applications)
│   ├── users/            (Example: User authentication and profile app)
│   │   ├── __init__.py
│   │   ├── models.py       (User-related data models - could extend Django User)
│   │   ├── views.py        (Views for user-related functionality)
│   │   ├── serializers.py  (For API responses, if using REST Framework)
│   │   ├── forms.py        (Forms for user-related actions, if needed)
│   │   ├── urls.py         (URLs specific to the 'users' app)
│   │   ├── admin.py        (Admin configurations for 'users' models)
│   │   ├── tests.py        (Tests for the 'users' app)
│   │   └── migrations/   (Database migrations for 'users' app)
│   ├── products/         (Example: App for product management - could be anything like 'blog', 'tasks', etc.)
│   │   ├── __init__.py
│   │   ├── models.py       (Product-related data models)
│   │   ├── views.py        (Views for product-related functionality)
│   │   ├── serializers.py  (For API responses, if using REST Framework)
│   │   ├── forms.py        (Forms for product-related actions, if needed)
│   │   ├── urls.py         (URLs specific to the 'products' app)
│   │   ├── admin.py        (Admin configurations for 'products' models)
│   │   ├── tests.py        (Tests for the 'products' app)
│   │   └── migrations/   (Database migrations for 'products' app)
│   ├── ... more apps ...  (Add more Django apps here as your project grows)
├── templates/           (Project-level templates - if you are serving HTML with Django)
│   └── ...             (Template files)
├── static/              (Project-level static files - CSS, JavaScript, images)
│   └── ...             (Static files organized by app or category)
├── utils/               (Project-level utilities and helper functions)
│   ├── __init__.py
│   ├── helpers.py        (General utility functions)
│   ├── exceptions.py     (Custom exception classes)
│   └── ...             (Other utility modules)
├── config/              (Configuration files beyond settings.py - e.g., environment vars)
│   ├── __init__.py
│   ├── environments.py (Environment-specific settings overrides)
│   └── ...             (Other configuration modules)
├── docs/                (Project documentation - using Sphinx, Markdown, etc.)
│   └── ...             (Documentation files)
├── tests/               (Project-level tests - integration tests, etc.)
│   ├── __init__.py
│   └── ...             (Test files)
├── requirements.txt     (Python dependencies)
├── .gitignore           (Git ignore file)
└── README.md            (Project README file)
```

## Explanation of Each Directory/File

- myproject/ (Project Root): This is the top-level directory for your entire project. You can name this whatever you like (e.g., webapp_backend, api_server, etc.).

- manage.py: A Django-generated script that lets you run administrative commands for your project (like runserver, migrate, createsuperuser, etc.). Keep this at the project root.

- myproject/ (Inner Project Directory/Python Package): This directory, also named the same as your project root, is the actual Python package containing your project's core settings and URL configurations. It's crucial to have this inner directory with an **init**.py to make it a Python package.

  - **init**.py: Makes the directory a Python package.

  - settings.py: Contains all your Django project's settings. You'll configure your database, installed apps, middleware, static/media file settings, and much more here.

  - urls.py: The project-level URL configuration. This is where you connect URLs to your Django apps' URL configurations.

  - asgi.py and wsgi.py: Configuration files for deploying your Django project using ASGI (Asynchronous Server Gateway Interface) and WSGI (Web Server Gateway Interface) respectively. ASGI is generally preferred for modern applications, especially if you plan to use asynchronous features.

- apps/: This is a container directory where you will organize your Django applications. Django apps are modular components of your project, each responsible for a specific part of your application's functionality. This is a key organizational element.

  - users/ and products/ (Example Apps): These are examples of Django apps. You should create apps based on the logical features of your web application. For instance:

    - users/ or accounts/: For user authentication, registration, profiles, password management, etc. This is where you'll often work with Django's built-in authentication system or extend it with custom user models.

    - products/, items/, content/: For managing the core data of your application. This is where you'll define your custom data models (as you mentioned).

    - orders/, payments/, shopping_cart/: For e-commerce related features.

    - blog/, forum/, comments/: For content and interaction features.

    - api/, endpoints/: If you're building a purely API backend, you might have an app dedicated to API specific logic.

- Inside Each App Directory:

  - **init**.py: Makes the app directory a Python package.

  - models.py: Define your data models here. This is where you create classes that inherit from django.

  - db.models.Model to represent your database tables. For user authentication, you might extend Django's AbstractUser or AbstractBaseUser in your users/models.py.

  - views.py: Write your view functions or class-based views here. Views handle requests and return responses (like JSON for APIs, or rendered HTML if serving templates).

  - serializers.py: (If using Django REST Framework or similar) Define serializers to convert your Django model instances into JSON or other data formats for API responses, and vice versa.

  - forms.py: (If using Django Forms) Define forms for handling user input, validation, and rendering HTML forms (if needed in your backend admin, or if you serve some frontend with Django).

  - urls.py: Define URL patterns specific to this app. You'll include these app-level URLs in your project-level myproject/urls.py.

  - admin.py: Configure how your app's models are displayed in the Django Admin interface. This is very helpful for backend management.

  - tests.py: Write unit tests for your app. Test your models, views, serializers, etc., to ensure they work as expected.

  - migrations/: Django automatically generates migration files here when you make changes to your models. These migrations are used to update your database schema.

- templates/: If you are using Django to render HTML templates (even in a backend context for admin panels or internal tools), you'll store your project-level templates here. Django will look for templates within the templates directory in each app and then in this project-level directory if not found in apps.

- static/: Project-level static files (CSS, JavaScript, images, etc.) that are served directly by the web server. You can further organize static files within this directory, perhaps by app name or category.

- utils/: A directory for project-wide utility modules, helper functions, custom exceptions, and reusable code that doesn't belong to any specific app.

- config/: For configuration files that are not directly part of Django settings. For example:

  - environments.py: You might have different settings based on environments (development, staging, production). This file can contain environment-specific settings overrides.
  
  - API keys, secrets, and other sensitive configuration that you might want to manage separately, potentially using environment variables or secure configuration management tools.

- docs/: For project documentation. You might use Sphinx, Markdown files, or other documentation tools to document your API, models, codebase, etc.

- tests/: For project-level tests. This could include:

  - Integration tests that test the interaction between different apps or components.

  - End-to-end tests.

  - Broader system-level tests.

  - Note: App-level unit tests are typically placed within each app's directory (apps/users/tests.py, apps/products/tests.py, etc.).

- requirements.txt: A file listing all Python package dependencies for your project. You can generate this using pip freeze > requirements.txt. It's used for easy setup of your project in different environments.

- .gitignore: A file for specifying intentionally untracked files that Git should ignore. This is crucial for version control to avoid committing things like .pyc files, **pycache** directories, local databases, etc.

- README.md: A Markdown file providing a description of your project, instructions for setup, usage, and any other important information.

### Key Principles and Best Practices

- Modularity and Reusability: Django apps promote modularity. Break your application into logical, self-contained apps. This makes it easier to develop, test, and maintain individual features.

- Separation of Concerns: Each app and directory should have a clear purpose. Keep models, views, serializers, tests, etc., within their respective apps. Keep project-level utilities and configurations separate.

- Convention over Configuration: Django encourages following conventions. This structure is a widely accepted convention, and adhering to it will make your project easier for other Django developers to understand.

- Scalability: Starting with a good structure from the beginning makes it much easier to scale your project as it grows in complexity and features.

- Testability: This structure makes it easy to write and organize tests.

### How to Use Django Authentication in this Structure

1. users/ App: Create a users app (or accounts or similar)

2. users/models.py:

  - You can extend Django's built-in User model using a OneToOneField in your users/models.py to add profile information:

```python
from django.contrib.auth.models import User
     from django.db import models

     class UserProfile(models.Model):
         user = models.OneToOneField(User, 
            on_delete=models.CASCADE, 
            related_name='profile')
         bio = models.TextField(blank=True)
         profile_picture = models.ImageField(
            upload_to='profile_pics/', blank=True
            )

         def __str__(self):
             return self.user.username

```

   - Or, you can create a completely custom User model by inheriting from AbstractUser or AbstractBaseUser in users/models.py. This gives you more control but requires more initial setup.

3. users/views.py, users/serializers.py, users/urls.py, etc.: Implement views, serializers, and URLs for user registration, login, logout, password management, profile updates, etc., within the users app.

4. settings.py: Configure authentication settings, potentially specifying your custom user model if you created one (e.g., AUTH_USER_MODEL = 'users.CustomUser').

5. Use Django's Authentication Features: Utilize Django's built-in authentication views, decorators (@login_required), and functions (authenticate, login, logout, User model access) throughout your project as needed.

### How to Create Additional Data Models

- Choose the Right App: Determine which Django app your new data models logically belong to. If it's a core part of your product data, it might go in the products/ app. If it's user-related, it might go in users/. If it's a new feature area, create a new app.

- models.py in the App: Define your new models as classes inheriting from django.db.models.Model within the models.py file of the appropriate app.
  Run Migrations: After defining your models, run python manage.py makemigrations <app_name> and then python manage.py migrate to create the database tables for your models.
  Use Models in Views, Serializers, etc.: Import your models into your views, serializers, admin configurations, and tests to work with your data.
  Flexibility:

This is a recommended structure. You can adapt it based on the specific needs and complexity of your project. For very small projects, you might have fewer apps or a flatter structure. However, for most web applications, especially those that will grow, adopting a structured approach like this from the beginning will pay off significantly in the long run.
