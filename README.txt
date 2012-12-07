--- Group Members ---

cschloss (Colin Schloss)
kaipeng (Kai Peng)
bfisc (Brandon Fischer)

--- Overview of Application ---

As you mentioned in your response to our project report, this was a much more amibitious project than we first realized. After spending hours trying to debug seemingly simple lines of code and implement basic features, we were forced to cut numerous features. We did not spend much time on the GUI, so it still looks like the typical blocky HTML page. We were unable to get certain operations on the database to work properly, so we have not yet implemented the "social" aspect of this project where users should be able to see other users' trades. We did not implement the capability to short-sell a stock, and we were unable to handle correctly the scenario when a user sells more stock than he currently owns.

We were still able to implement numerous features though:
- Profile Creation
- Email Account Activation
- Password Recovery
- Buy/Sell stocks and have the portfolio update accordingly
- View transactions
- View positions

--- Running the Application ---

Go to the website, git.to/pytrader192
Click "Get Started"
Click "Register Here"

You can create your own profile with your own google account and password if you would like, or you can create a new profile with our dummy google account "pytrader.tester@gmail.com" with password "python192". There is also an admin account (Username: admin, password: password) that you can use to see and manage the backend, including user trader profiles. We have customized this page to include the additional data fields within a profile.

Go through the email verification process to get your profile working. Once you get your profile working, you can view positions, view transactions, or place an order.

--- Layout of the Code ---

All of our code is on Amazon's ec2. It's running on one micro-instance with a Django stack. The machine is configured with Django 1.4, a PostgreSQL database, and an Apache server.

Within the Project folder, we have 5 Django apps - pytrader, table_test, auth, templates, and Project. Each app has a urls.py file that contains a set of regular expression rules to recognize specific URLs and direct the user to the appropriate page, which is rendered by a Python function under views.py.

In addition, we used some other packages to help us out:
	gdata_2.0.16 - a python library for Google Data and Finance APIs
	django_tables2 - to help us out with table formatting
	south - a sql database migrator to help us manage our db

*** pytrader ***

pytrader has all of our major data structures, such as user and profile. This is where we would keep track of users' portfolios and transactions as well as the social aspect of the program (follows, likes, news feed, etc.). These models are inside models.py.

*** table_test ***

Within the finance folder, there are prewritten functions to help us interact with Google Data and Google Finance. The sample_run file was a holdover from our progress report which establishes more functions to help with Google Finance and provides the class that helps us link our app with Google's portfolio management. The forms2.py file contains the form definitions for the "Place Order" functionality. The views.py file creates the views for the "View Positions", "View Transactions", and "Place Order" pages.

*** auth ***

Within admin.py, auth has code to customize our admin interface to handle the extra fields that we have for each user, such as Google Password. Within forms.py, there are the forms for registration, login, and password recovery. These forms are injected into our templates (which we will talk about below). The views.py file creates the views for registration, registration success, logout success, and user activation.

*** Templates ***

Django has an HTML templating language that allowed us to create an interface between python code and HTML code. It allows you to interact with python variables (which are passed in through dictionaries) while scripting HTML. So, each page has its own template in the Templates folder.

*** Project ***

The views.py file contains the view for the homepage. The settings.py file establishes the settings for all of the apps, including which database to use.

--- Full Disclosure ---

Brandon did not help with this project at all. We still probably wouldn't have been able to implement all of the features that we would've wanted, but another brain would've certainly helped.