The scope of this application is to test the functionalities of Spotify API. Spotify Web API

### Prerequisites <br>
To run the application, you need python 3.11, venv and pip to be installed.

<ul><li>python3.11: You need to have Python installed, at least the version 3.11 . Check if you already have Python installed running the Terminal command: python --version. If the result shows a version number, Python is already installed. 
If not, you can download it here: https://www.python.org/downloads/</li>

<li>pip: pip is the package manager for Python. It is used to install and update packages in a virtual environment. Check if you have already pip installed running the Terminal command: pip --version. 
If the result shows a version number, pip is installed and there is no need for further actions. If not, instructions for downloading the latest version of pip can be found here: https://pip.pypa.io/en/stable/cli/pip_download/</li>

<li> venv (Virtual Environment): You need to create a virtual environment (venv) before running the application. For more information on how you create one, follow this link:
https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment </li></ul>

### Implemeting Spotify Api Framework 

#### Step 1 Create a Spotify account

This app relies on Spotify API. In order to use the app, you need to create a Spotify developer account.
The following steps need to be implemented in order to define Pycharm Api Testing Project:

1. Create a folder in your computer where you'd like to store the code to run the app.

2. The libraries used are:
- requests (version 2.31)
- pytest (version 7.4.3)
- pytest-html (version 4.1.1)

 To install them, run the Terminal command: <b> pip install -r requirements.txt </b>

3. In constants.py file, replace your CLIENT_ID, CLIENT_SECRET, REDIRECT_URI values with the ones obtained after the creation of the Spotify Dashboard in the developer account.
   Replace the USER_ID value with the Spotify email account

   Scope determines what  permisions the user has the following scopes will be defined in order to grant full acces to the automation user:```user-read-private user-read-email playlist-modify-public playlist-modify-private user-library-modify ugc-image-upload user-library-read user-read-playback-position ```

API = "https://api.spotify.com/v1"

#### Step 2 Authentication

Spotify relies on OAuth2 (Open Authorization) standard for authentication and authorization.

To obtain the access token, you need to perform the following steps:

1. The following URL needs to be created: HOST + "/authorize?client_id=" + CLIENT_ID+"&response_type="+RESPONSE_TYPE+"&redirect_uri="+ENCODED_REDIRECT_URI+"&scope="+SCOPE
- HOST = https://accounts.spotify.com
- CLIENT_ID = the one generated in the dashboard
- REDIRECT_URI = the one generated in the dashboard URI encoded
- CLIENT_SECRET = the one generated in the dashboard
- SCOPE = the specified at point 3 in the previous section

2. Access the URL obtained running the command above and accept the terms. You will be redirected to a URL which contains the authorization code

3. Now an Api Request must be created in order to obtain the acces token, the Api Request will have the following components:
a) Request endpoint : https://accounts.spotify.com/api/token
b) Request body:
- content-type: x-www-form-urlencoded
- redirect_uri: the one generated in the dashboard
- client_id: the one generated in the dashboard
- client_secret: the one generated in the dashboard
- code: obtained from the previous step (it will be found in the previously generated URL, after the "=" sign)
- grant_type: authorization_code

#### Step 3 Implementing the Automation Api

1. Generate token
The generation of the token was implemented under a class called Generate_token which inherits class Browser in order to be able to open a web page and generate the authorization code
The class has the following methods implement:
- create_authorize_endpoint: create the URL that will be used in the generation of the authorization code
- load_endpoint: acceses the previously defined URL which directs the user to the spotify login page
- login_to_spotify: inserts user name and password and clicks login button
- authorize_login: validates the login as being valid and generates a new URL containing the authorization coode
- get_code: extract the code from the previuosly generated URL  
- get_token: generates the acces token 
- authorization: calls subsequently all the previously defined methods

#### Step 4 Preparing the requests

In order to be able to validate the Api from the Spotify documentation, we need to map them into the Pycharm Automation Framework
The Spotify Api documentation can be found [here](https://developer.spotify.com/documentation/web-api)
All the requests were mapped into python files and grouped under one single folder called <i>requests_folder</i>

#### Step 5 Preparing the tests

After mapping the Api requests into methods these were called into some tests methods created into separate python files and grouped under one single folder called <i>tests</i>
The following endpoints were covered throught tests
<ul>
<li> https://api.spotify.com/v1/artists/{artist_id}</li>
<li>https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market={country}</li>
<li>https://api.spotify.com/v1/markets?markets={country}</li>
<li>https://api.spotify.com/v1/playlists/{playlist_id}</li>
<li>https://api.spotify.com/v1/playlists/{playlist_id}</li>
<li>https://api.spotify.com/v1/users/{user_id}/playlists</li>
<li>https://api.spotify.com/v1/playlists/{playlist_id}/tracks</li>
<li>https://api.spotify.com/v1/users/{user_id}/playlists</li>

#### Step 6 Running the tests

In order to run the tests we can use the following command <b>pytest tests --html=test-report.html<b>
Below you can find the test report that was generated through running the test suite:

![image](https://github.com/Lulu846/Automation_Testing_Spotify_API_Python/assets/129788963/ad45cbbf-ead8-4c3a-8ed3-553cd05ee9b0)

#### Step 7 Analysing the results

Through analysing the test execution report I noticed that one of the test was failed. After debugging and manual reproduction I discovered  and reported a defect.




