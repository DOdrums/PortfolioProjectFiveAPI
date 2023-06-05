

## Validator Testing

### Python

For writing the python code Black was used for formatting. This kept the line length at the standard 79 charachters.

## Manual Testing

For the manual testing of the backend, DRF's automagically generated "front-end" was used, where you see and manipulate the data live. The models and views were tested on the following criteria:

| Model                 | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| User                  | Login      | Login the user or give proper errors                               | Pass      |
| User                  | Logout     | Logout the user or give proper errors                              | Pass      |
| Profile               | List       | List all profiles                                                  | Pass      |
| Profile               | Detail     | Show details of 1 specific profile                                 | Pass      |
| Profile               | Filter     | Filter profile by user                                             | Pass      |
| Profile               | Ordering   | Order profiles by posts_count or songs_count                       | Pass      |
| Profile               | Put        | Edit fields on given profile                                       | Pass      |
| Song                  | List       | List all songs                                                     | Pass      |
| Post                  | List       | List all posts                                                     | Pass      |
| Song                  | Detail     | Show details of 1 specific song                                    | Pass      |
| Post                  | Detail     | Show details of 1 specific post                                    | Pass      |
| Song                  | Put        | Edit fields on given song                                          | Pass      |
| Post                  | Put        | Edit fields on given post                                          | Pass      |
| Song                  | Filter     | Filter songs by user                                               | Pass      |
| Post                  | Filter     | Filter posts by user                                               | Pass      |
| Like                  | List       | List all likes                                                     | Pass      |
| Mic                   | List       | List all mic's                                                     | Pass      |
| Like                  | Detail     | Show details of 1 specific like                                    | Pass      |
| Mic                   | Detail     | Show details of 1 specific mic                                     | Pass      |
| Like                  | Delete     | Delete 1 specific like                                             | Pass      |
| Mic                   | Delete     | Delete 1 specific mic                                              | Pass      |
| Instrument            | List       | List all instruments                                               | Pass      |
| Instrument            | Detail     | Show details of 1 specific instrument                              | Pass      |
| Instrument            | Delete     | Delete 1 specific instrument                                       | Pass      |


## Automated testing

Some automated tests were written for testing views and models of both the User and Salon app. This is handy in case packages need upgrading, or major changes to the app are made. In this case, automated tests can be run first, to find obvious errors caused by the changes. After that, manual testing should still be performed.

### Running the test suite

The tests are run by entering ```python3 manage.py test``` in the terminal window (inside the project folder). This will automatically run all test. If running tests in quick succession, it's recommended to add ```--keepdb``` at the end, so the database doesn't have to be rebuild for every test cycle. The test in the suite for this project all pass, but if one would fail, it would be displayed with a clear error message, so errors can be solved.

![testing](static/images/testing.png)

## Bugs

* When running the admin panel on the deployed Heroku version, the CSS wouldn't show. This was a two part bug: first, `DISABLE_COLLECTSTATIC = 1` was set as an environment variable. Because of this, Heroku couldn't probably set the paths to the static files (which live on Cloudinary) and thus not load the admin panel CSS. After removing the variable, `collectstatic` would run during Heroku deployment, but would fail. After some digging around, the cause was found to be a missing static folder. However, this folder did very much exist in the development version of the project. What happened, is that git ignored the folder since it was empty. To mitigate this, a empty `.keep` file was added to the static folder, so Heroku wouldn't ignore the folder any longer. After this the deployment had no issues and the CSS loaded.