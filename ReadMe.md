# EasyPost Web Application 

## About the app

The [EasyPost API](https://www.easypost.com/) makes it easy to figure out your own shipping labels. This app helps to utilize the API by filling out a simple online form. Although the form is very simplistic, it does a great job at getting to the core of the task. When one runs the application, they'll be prompted with a screen to fill out a few fields:

- Source Address
- Destination Address
- Type of Package (if applicable)
- Dimensions and Weight

Then, it should lead to a screen with the shipping label, which should be convenient enough to print out.

## Instructions to Run

```
# Go to directory
cd EasyPost
# Install flask if necessary
pip install flask
# Run the main python file
python app.py

 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 169-849-268

 # Click on http://127.0.0.1:5000/ or copypaste the link

```

Voila! 

## Future Updates

- Better UI (made the app in roughly 4 hours so couldn't do it this time around :) )
- Error handling for minor edge cases
- Adding international shipping details