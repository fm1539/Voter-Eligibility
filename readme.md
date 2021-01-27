

## Running the App<a id="run"></a>

Run this app by navigating to the directory where it is housed and running `flask run`. Then click the IP address in terminal to be redirected to the location where the app is running.

## Anatomy of the app<a id="anatomy"></a>

Here's everything inside our Flask template. 

<pre>
flaskproject
├── .gitignore - shows which files (like .pyc) for git to ignore.
├── Procfile - Ignore. Used for deployment.
├── app.py - This is the main file for our app.
├── model.py - This is where we will write the logic of our app.
├── readme.md - That's this file!
├── requirements.txt - Used for deployment to say what packages are needed.
├── runtime.txt - Ignore. Used for deployment.
├── static - This is where we house assets like images and stylesheets.
│   ├── css - Put stylesheets here.
│   │   └── style.css
│   └── images - Put images here.
│       └── micropig.jpg
└── templates - Put templates (views) in this folder.
    └── index.html - This will be the first template we render.
</pre>
