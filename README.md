# Heroku Selenium Worker

This web application is based as an introduction to background worker processes in Heroku, which can be found at the [Heroku Devcenter](https://devcenter.heroku.com/articles/python-rq).

Example: https://herokuseleniumworker.herokuapp.com/

Just add /?website=thewebsiteurl

This project started when Heroku decided to add H12 errors which prevented any Selenium Webdriver from performing a large task that took more than 30 seconds. The solution to this issue is using Heroku's free REDISTOGO Python background workers which work with flask to take in a website url and return it's code. This approach can be modified to your needs so that you can run any Selenium process without the fear of a Timeout exception.
What also makes this project special is that it is setup to use [Undetected Chromedriver](https://github.com/ultrafunkamsterdam/undetected-chromedriver) as it's webdriver, making it possible to bypass Captcha systems and Cloudfare protection on any site.
This project is also specifically tailored to integrate Flask with Selenium so you can use your deployment as an API/Proxy.

## How to use it:

All of the code is setup so that the only files that matter in running your process are the app.py file (the Flask web interface) and the utils.py file (runs all of your selenium code).
One important thing to notice is that you must have your Selenium process running within a function that returns a value/result back to Flask.

I've also added app.json and this readme so you can:

## Deploy to Heroku
By clicking the button below.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
