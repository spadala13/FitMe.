# FitMe.

#### Video Demo: https://youtu.be/IlgHUlWGJh4

#### Description:

** Hi! Welcome to _FitMe._ **


** FitMe. is a website that allows users to record and track their personal fitness activities in a database, and also look at their past activities.**

** When you arrive at the homepage of FitMe., if you're a new user, you are able to register by clicking on the "Sign Up" button.
   If you're a returning user, you can simply log in to your account by clicking the "Log In" button. Once you're logged in, you'll be welcomed by an aesthetic
   dashboard which shows the user's basic information. Total calories of the user is shown in the top black bar while a count of exercises which are categorized
   are shown below. Each of the categories is background colors were chosen to be pastel colors to provide a simple yet classy visual.
   Clicking on "Add a Exercise" would prompt you to another page where you are able to enter the name of the exercise, number of calories, the time it took,
   the number of reps, and in which category this belongs in such as Cardio, Muscle Strengthrning, Yoga, Swimming, Weight Lifting, Walking, or Other.
   Lastly, clicking on dashboard would allow you to see a history of all your exercises, and also allows you to search for a specific
   exercise based on its name in the search bar.

   To implement this web application, I have created two databases in sql.py, one which stores the data about the exercise while one which stores the username
   and password. This web application also save cookies so users can conveniently stay logged in. In helper.py, I have implemented a message function and
   a login_requried function which does not allow the user to access the add an exercise and dashboard pase without login. The message function alerts the user
   whether the username already exists, if they have entered the wrong password, or they have entered wrong credentials.

   The templates folder incorporates all the html files which creates structure, user interface, and allows users to fill up forms.
   application.py includes the main code which allows this web application to run. It uses Flask and app.route to allow the users to switch between webpages.
   I have also included a EXERCISES array in this file so the user cannot edit the exercise category themselves using the inspect feature and register an exercise
   that is not in the categories. The login function directs the user to the login page and checks whether they have entered the right information
   such as the correct username and password. If the login is successful, the session number is stored and the user is directed to the home page of the web application.
   The register function registers user using the new username and correct reiterated password, and stores these values in the database. It then redirects the user to the
   login page. The dashboard function directs the user to the dashboard webpage and creates the dashboard using the exercise categories. If you notice, each category of exericse
   has separate background in the table to easily distinguish them. The add a exercise function gets the user's exercise information and stores it into the database.
   Lastly, clicking on home redirects the user to the homepage which shows the total number of calories and number of exercises they did.

   In the templates file, there are the HTML files for each page. The layout.html is used to facilitate writing the other HTML files. The layout.html simply contains
   the contents such as nav_bar, bootstrap, and javascript links, and includes a empty body where I could input the code based on the web page. The homepage.html includes
   the features such as the typing words using javascript and also includes sign up and log in button. The homepage.html is what the user sees when they first enter the web
   application. home.html however includes the components which show the total number of calories and the exercise category, and I ahve meticulously chosen specific
   box sizes to account for the aesthetics, which is why the total calories and the other box in Home are the same size for symmetry. Login.html includes the components of using
   a form to request the username and password. Register.html includes the components where the user could register using a form. Addexercise.html includes a huge form which asks
   the user for input such as exercise name, number of calories, day and time, exercise category, and the number of reps of the exercise. Lastly, dashboard.html creates the table
   that you can see in the dashboard webpage.

   Last but not least, in the static folder, there are two CSS files which both describe the presentation of the website, including colors, and layout of each page. Homepage.css
   creates the aesthetics for the welcome page such as the font and backgroun cover with workout tools. Home.css includes the layout of the 8 boxes in the homepage you enter after
   you have logged in. Additionally, style.css includes the design choices I have chosen for every webpage, such as a light nav-bar, a modern font, and each color of the boxes.

   Some design choices I have debated while implementing this web application was whether I should include a welcome page or not. In the end, I have decided to create one
   to create a welcoming feeling and also to make the website more pleasing. Another design choice I have debated about was whether I should use flashy colors or gradients for the
   exercise category boxes in the homepage. However, I have realized including too many vibrant colors or different colors of gradients for each box was very distracting. So, I have
   used subtle colors to make the website more appealing.




