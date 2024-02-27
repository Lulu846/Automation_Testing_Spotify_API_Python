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

6. Run the command below and copy the generated code in the constant ACCESS_TOKEN from the "AUTHORISATION.py" file

pprint(request_access_token(authorization_code).json()['access_token'])

‼️ The generated token is available for 60 minutes. After the time expires, you need to follow again the steps from Authentication chapter

For more information you can follow the following URLs:

1. Spotify API authorization guide: https://developer.spotify.com/documentation/web-api/concepts/authorization

2. Google OAuth2 authorization standard: https://pkg.go.dev/golang.org/x/oauth2/google

Step 4 Running the tests

The tests can be found in the tests folder. To run any test, you can run the corresponding file.

For example, in the test_artist.py file, you can run the tests suite pressing the green triangle found to the left of the TestArtist(unittest.TestCase) class. If you want to run only one test, press the green triangle found to the left 
of the function which describes the desired test, for example the function test_artist_check_status()

![image](https://github.com/Lulu846/Automation_Testing_Spotify_API_Python/assets/129788963/ad45cbbf-ead8-4c3a-8ed3-553cd05ee9b0)

Step 5 Generating the report

To generate the report, run the Terminal command:

pytest --html=report.html
An HTML file will be created in the project main directory, which can be opened with any browser.




