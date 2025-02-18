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

## Migrations

Preparing migrations in Django is a fundamental part of managing your database schema as your application evolves. Django migrations allow you to make changes to your models (your Python code that defines your database structure) and then apply those changes to your actual database schema in a structured and reversible way.

Here's a comprehensive guide on how to prepare and use Django migrations:

1. Understanding Django Migrations: Why and What

Purpose: Django migrations are designed to synchronize your Django models (the Python representation of your database structure) with your actual database schema. When you change your models (add fields, remove fields, rename fields, etc.), migrations provide a way to update the database schema to match those changes without losing data (in most cases).
Key Concepts:
Migrations as Files: Migrations are stored as Python files within migrations/ directories in your Django apps. Each migration file represents a set of changes to your models.
Migration Operations: Inside migration files, you'll find "operations" that describe the database changes. These operations can include:
CreateModel: Creating a new database table.
AlterField: Modifying a field in a table (e.g., changing data type, constraints).
AddField: Adding a new field to a table.
RemoveField: Removing a field from a table.
RenameField: Renaming a field.
DeleteModel: Deleting a table.
RenameModel: Renaming a table.
RunPython: Running custom Python code during migration (for data migrations, etc.).
And more...
Migration History: Django keeps track of which migrations have been applied to your database in a special table (usually django_migrations). This history allows Django to apply only the migrations that haven't been applied yet, and to understand the current state of your database schema.
2. Core Commands for Migrations

There are two primary commands you'll use to work with Django migrations:

python manage.py makemigrations [app_label(s)]:  This command is used to create new migration files based on changes you've made to your models.

Purpose: makemigrations inspects your models and compares them to the last applied migration for each app. If it detects changes, it will generate new migration file(s) in the migrations/ directory of the affected app(s).
[app_label(s)] (Optional):
If you run python manage.py makemigrations without any app labels, it will check for changes in all apps in your project that have migrations enabled.
You can specify one or more app labels (e.g., python manage.py makemigrations users products) to create migrations only for specific apps. This is useful when you've made changes only in certain apps and want to generate migrations just for them.
When to Run makemigrations: Run this command after you have made changes to your models.py files in your Django apps. This includes:
Creating new models.
Modifying existing models (adding, removing, or changing fields, changing model options, etc.).
Renaming models or fields.
Adding or removing model relationships (ForeignKey, OneToOneField, ManyToManyField).
python manage.py migrate [app_label] [migration_name]: This command is used to apply migrations to your database schema.

Purpose: migrate applies migrations that have not yet been applied to your database. It reads the migration files and executes the operations defined in them to update your database schema.
[app_label] (Optional):
If you run python manage.py migrate without an app label, it will apply all pending migrations across all apps in your project.
You can specify an app label (e.g., python manage.py migrate users) to apply migrations only for a specific app.
[migration_name] (Optional):
You can also target a specific migration by providing its name (e.g., python manage.py migrate users 0002_add_profile_bio). This is less common in typical workflows but can be useful for rolling back to a specific point or applying migrations in a specific order.
You can also use special names like zero to unapply all migrations for an app (python manage.py migrate users zero).
When to Run migrate:
After running makemigrations: After you've created migration files using makemigrations, you need to run migrate to actually apply those changes to your database.
During initial project setup: When you first set up your Django project, you need to run python manage.py migrate to apply the initial migrations for Django's built-in apps (like auth, contenttypes, admin, etc.) and any initial migrations you create for your own apps.
When deploying code changes: When you deploy code changes to a staging or production environment that include new migrations, you must run python manage.py migrate in those environments to update the database schema.
After pulling code changes from version control: If you're working in a team and pull code changes that include new migrations, you need to run python manage.py migrate locally to update your development database schema.
3. Creating Initial Migrations for a New App

When you create a new Django app (using python manage.py startapp my_new_app), it will have a migrations/ directory, but it will initially be empty except for an __init__.py file.  To create the initial migrations for your app based on your models.py file, you need to run makemigrations for that app:

Bash

python manage.py makemigrations my_new_app
This will generate the first migration file (usually named something like 0001_initial.py) in your my_new_app/migrations/ directory. This initial migration file will contain operations to create the database tables corresponding to the models defined in your my_new_app/models.py.

After running makemigrations, you then need to apply this initial migration to your database:

Bash

python manage.py migrate my_new_app
Or, to apply all pending migrations across all apps (including the new app's initial migration and Django's built-in migrations, if not already applied):

Bash

python manage.py migrate
4. Making Migrations After Model Changes

Whenever you modify your models.py file (after the initial setup), you need to repeat the makemigrations and migrate process:

Make changes to your models.py file. For example, add a new field to a model, change a field type, etc.

Run makemigrations:

Bash

python manage.py makemigrations  # Or python manage.py makemigrations my_app if changes are only in 'my_app'
Django will detect the changes you've made to your models since the last migration and create a new migration file (e.g., 0002_add_new_field.py).

Run migrate:

Bash

python manage.py migrate  # Or python manage.py migrate my_app if you want to apply only app-specific migrations.
Django will apply the newly created migration, updating your database schema to reflect the changes in your models.

5. Inspecting Migrations: showmigrations

The showmigrations command is helpful to see the status of your migrations: which migrations have been applied and which are pending.

Bash

python manage.py showmigrations [app_label(s)]
[app_label(s)] (Optional): You can specify app labels to see migrations for specific apps or run it without app labels to see all migrations for all apps.
The output will typically look something like this:

 app_name
  [X] 0001_initial
  [ ] 0002_add_new_field
[X]: Indicates that the migration has been applied to the database.
[ ]: Indicates that the migration is pending and has not been applied yet.
6. Unapplying Migrations: unmigrate (Use with Caution!)

The unmigrate command is used to unapply migrations, essentially rolling back database schema changes. Use this command with caution, especially in production, as it can potentially lead to data loss or inconsistencies if not used correctly.

Bash

python manage.py unmigrate [app_label] [migration_name]
[app_label] (Optional): Specify the app to unmigrate.
[migration_name] (Optional): Specify a particular migration to unapply. If not specified, it will unapply the last applied migration for the app. You can use zero to unapply all migrations for an app (python manage.py unmigrate my_app zero).
Example of Rolling Back a Single Migration:

To unapply the last migration for the users app:

Bash

python manage.py unmigrate users
To unapply a specific migration (e.g., 0002_add_profile_bio) for the users app:

Bash

python manage.py unmigrate users 0002
7. Faking Migrations: migrate --fake and migrate --fake-initial

migrate --fake [app_label] [migration_name]:  This command marks migrations as applied in Django's migration history table without actually running the database operations in the migration file.

Use Cases:

Resolving issues when migrations have been applied manually or outside of Django's migration system. If your database schema is already in the state that a migration would create (e.g., tables are already there), you can use --fake to tell Django that the migration is considered applied, without trying to re-apply it (which might cause errors).
Setting up a database from an existing schema. If you're starting with an existing database schema that already matches your models, you can use --fake --initial (see below) to mark the initial migrations as applied without re-creating tables that are already there.
Troubleshooting Migration Issues: In some complex migration scenarios, you might use --fake to temporarily bypass a problematic migration to get your application running and then investigate the issue separately.
Caution: Using --fake incorrectly can lead to inconsistencies between Django's migration history and the actual database schema. Use it only when you understand its implications and when you are sure the database is already in the expected state.

migrate --fake-initial:  This is a special option used when you are applying migrations for the very first time to an existing database that already has tables matching your initial models.

Use Case: When you're adding Django migrations to an existing project with a database that was previously managed manually or by a different ORM. If you've designed your Django models to match your existing database schema, you can use --fake-initial to apply the initial migrations for Django's built-in apps and your own apps. Django will check if tables with the same names as in your initial migrations already exist in the database. If they do, it will mark the initial migrations as applied (faked) without attempting to create tables that are already there. If tables don't exist, it will create them.
Caution: Requires that your existing database schema is very closely aligned with what your initial Django models and migrations would create. Database schema mismatches can still cause issues later. It's often safer to start with a fresh database when introducing Django migrations to an existing project, if possible.
8. Squashing Migrations: squashmigrations (for large projects)

As your project grows and you accumulate many migration files, it can sometimes be beneficial to "squash" them. Squashing migrations combines a sequence of migrations into a single, new migration that represents the same database schema state. This can simplify your migration history and potentially speed up migration application in large projects, especially when setting up new environments.

Bash

python manage.py squashmigrations <app_label> [<migration_name>]
<app_label>: The app for which you want to squash migrations.
[<migration_name>] (Optional): The name of the migration up to which you want to squash. If not provided, it will squash all migrations for the app.
Example: To squash all migrations for the users app:

Bash

python manage.py squashmigrations users
This will create a new "squashed" migration file (e.g., 0003_squashed_0001_initial_0002_add_profile_bio.py) and update your migration history. You would typically then delete the older migration files that were squashed (e.g., 0001_initial.py, 0002_add_profile_bio.py) after verifying the squashed migration works correctly.

9. Checking Database Schema: check --database

The check --database command is used to validate if your current Django models are consistent with your database schema, without applying or creating any migrations. It's a useful way to proactively detect potential schema mismatches.

Bash

python manage.py check --database
This command will perform various checks to see if your models match what Django expects based on the applied migrations. It can help catch issues like missing tables, missing columns, or incorrect data types before you encounter errors at runtime.

10. Migration File Structure and Content

When you create a migration file, you'll see a Python file in your app's migrations/ directory.  A typical migration file looks something like this (simplified example):

Python

# Generated by Django ...

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'), # Dependency on a previous migration in the 'users' app
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        # ... other operations ...
    ]
dependencies: Lists migrations that must be applied before this migration can be applied. This ensures migrations are applied in the correct order, especially when you have relationships between models in different apps or within the same app.
operations: A list of operations that define the database schema changes. Each operation is an instance of a class like migrations.CreateModel, migrations.AddField, etc., and describes a specific change to be made to the database.
11. Migration Dependencies and App Order

Django migrations handle dependencies between apps and models automatically. If you have a ForeignKey relationship from a model in app_A to a model in app_B, Django will ensure that the migrations for app_B are applied before the migrations for app_A that create the ForeignKey field. Django automatically manages these dependencies based on your model definitions and the relationships between them.

However, if you have more complex scenarios or manual database operations, you might need to understand migration dependencies and app order. In settings.py, the INSTALLED_APPS order can sometimes matter if you have circular dependencies between apps' models or migrations.

Best Practices for Migrations

Run makemigrations and migrate regularly during development: Make it a habit to create migrations after making model changes and apply them to your development database. This keeps your schema in sync and helps catch issues early.
Commit migration files to version control: Treat migration files as part of your codebase. Commit them to Git or your version control system along with your model changes. This ensures that everyone on your team and your deployment environments can apply the same database schema changes.
Test migrations in a development/staging environment before production: Always test your migrations in a non-production environment first (like a development database, staging database, or CI/CD pipeline) to identify and resolve any issues before applying them to your production database.
Be cautious with schema-altering operations in production: Operations like DeleteModel, RemoveField, and changing field types can be data-destructive. Back up your production database before running migrations that could potentially cause data loss. Consider running schema-altering migrations during maintenance windows.
Consider data migrations for more complex data updates: For more complex data transformations or initial data loading, use "data migrations" (migrations with RunPython operations) to manage data changes as part of your migration process in a controlled way, rather than directly manipulating data outside of migrations.
Troubleshooting Common Migration Issues

"No changes detected" when running makemigrations: Double-check that you have actually saved your changes to models.py. Ensure your app is listed in INSTALLED_APPS in settings.py. Sometimes restarting your development server can help if Django is not correctly detecting file changes.
Migration conflicts: If multiple developers make conflicting changes to models and create migrations concurrently, you might encounter migration conflicts. Django will usually try to detect and highlight conflicts. You might need to resolve these conflicts manually by editing migration files, carefully considering the intended changes from different migrations.
"ProgrammingError: column ... does not exist" or similar database errors: This often means your Django models and database schema are out of sync. Run python manage.py migrate to apply pending migrations and synchronize your database schema. If you're sure migrations are applied, double-check your model definitions, migration history, and database schema for inconsistencies.
By following these guidelines and understanding the Django migration commands, you can effectively manage your database schema changes throughout your Django project's lifecycle.