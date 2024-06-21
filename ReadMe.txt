### Basic Features of The App
    
* Send Emails – Users can send email to the host through Contact Us page



To get this project up and running locally on your computer follow the following steps.
1. Set up a python virtual environment
2. Run the following commands
```
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
   
3. Open a browser and go to http://localhost:8000/
4. Send a message
5. Check your terminal


How it was created

Step 1: Create a new project (django-admin startproject contact_form)
Step 2: cd login
Step 3: Create a new app (django-admin startapp app)
Step 4: Register the app in the project (#login/settings.py add 'app',)
Step 5: Create the following dir (#app/templates/app/contact.html,success.html)
                                (#app/urls.py)
                                (#app/forms.py)
Step 6: Include the path of the app urls to the project urls
Step 7: Create views for the two html files and urls path for each of them
Step 8: Migrate the project db (python manage.py migrate)
Step 9: Create superuser (python manage.py createsuperuser)
Step 10: In the app views.py import the following (redirect, sendmail, settings,all function created in forms.py i.e (ContactForm))
Step 11: In views.py write the function to retrive data inputed by the user and send it as an email
Step 12: Redirect user to sucess.html
Step 13: Create the logout function
Step 14: Create the ContactForm function in forms.py
Step 17: Write your contact and success html and css code