## Findi Heroku Example

This is an example of how to record the location of your phone with
[findi](https://github.com/pearkes/findi), a python library for
interacting with Apple's Find My iPhone API.

## Instructions

You can follow these instructions to create a service that will
periodically connect to the Find My iPhone API and store your location
in a database.

### Getting Setup

First, You'll need a terminal and the [Heroku Toolbelt](https://toolbelt.heroku.com/).

Once that's installed, change to a new directory and clone the source
of this project:

    $ git clone git@github.com:pearkes/findi-heroku-example.git
    $ cd findi-heroku-example/

### Creating the Heroku Application

Now we want to create a heroku app, and install some necessary addons:

    $ heroku create
    ...
    $ heroku addons:add heroku-postgresql:dev
    ...
    Attached as HEROKU_POSTGRESQL_BROWN_URL

Pay attention to what your database "color" was. In this case, mine was
"brown".

Now, promote that database to be your primary:

    $ heroku heroku pg:promote HEROKU_POSTGRESQL_BROWN_URL

And add one more addon:

    $ heroku addons:add scheduler:standard
    ...

### Configuring the Application

Now, you'll need to store your Apple ID and password in plain text as
environment variables in Heroku's system. **This is, of course, a security
risk, as you are storing your password on a 3rd party system**.

Confirm you still want to do this, and then add it as a config variable, replacing
Steve's credentials with yours:

    $ heroku config:add APPLE_EMAIL=steve@apple.com APPLE_PASSWORD=applerox
    ...

### Deploying

Now that we've got the Heroku app created and configured, you should
simply be able to:

    $ git push heroku master
    ...

Now, we want to create the database. You'll need to confirm this action:

    $ heroku run python bootstrap.py
    ...

### Setting up the Scheduler

    $ heroku addons:open scheduler

Your browser will open, and you may have to log in to Heroku.

In the scheduler mangagement interface, add a hourly job called
`python record_location.py`.

![Scheduler Interface](https://f.cloud.github.com/assets/846194/102117/de8641c0-690f-11e2-9725-e6b4a18df0a9.png)

### Test Drive

    $ heroku run python record_location.py
    ...

You should see a message letting you know the location was sucesfully
stored. If not, feel free to [open an issue](https://github.com/pearkes/findi-heroku-example/issues/new).

## Check Your Work

It'd be worth checking back in and making sure you're storing the data
properly in a few days, and that the locations seem correct.

## License

Copyright (c) 2013 Jack Pearkes.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
