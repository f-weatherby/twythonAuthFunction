# twythonAuthFunction

This is a function that is designed to be incorporated with the Twython library, a pure Python wrapper for the twitter API. Developers who wish to create applications or software that accesses twitter (perhaps they want users to be able to see their timeline) can use Twython to make calls to the API and through this their users can access certian Twitter features. For a user to be able to use an apps Twitter features, they'll have to authenticate themselves and prove that they actually own an account before they can use twitter through the app. The authentication service that Twython uses is called Open Authorization (OAuth), and from the perpective of the user, it involves entering their Twitter credentials. However, not everyone who uses Twython is looking to create user applications, and instead might be interested in writing an Python program that makes repeated API calls, or that is designd to make them automatically. For these individuals, it may be tedious to have to enter your credentials every time your program wants to interact with the API.

To address this issue, I developed an authentication function that uses Selenium and a Firefox webdriver to complete this process automatically. Its function is as follows: 

(1) Using HTML tags, Selenium finds the username and password fields and the webdriver enters your credentials.
(2) You are then directed to a page as specified by the callback page where the driver extracts the oauth verifier.
(3) The function returns a fully authenticated twitter object through which API calls can be made.
