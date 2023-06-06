<!-- TOC -->

- [Validator Testing](#validator-testing)
    - [Python](#python)
- [Manual Testing](#manual-testing)
- [Automated testing](#automated-testing)
- [Bugs](#bugs)

<!-- /TOC -->

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

No automated tests were written for the backend.

## Bugs

* When running the admin panel on the deployed Heroku version, the CSS wouldn't show. This was a two part bug: first, `DISABLE_COLLECTSTATIC = 1` was set as an environment variable. Because of this, Heroku couldn't probably set the paths to the static files (which live on Cloudinary) and thus not load the admin panel CSS. After removing the variable, `collectstatic` would run during Heroku deployment, but would fail. After some digging around, the cause was found to be a missing static folder. However, this folder did very much exist in the development version of the project. What happened, is that git ignored the folder since it was empty. To mitigate this, a empty `.keep` file was added to the static folder, so Heroku wouldn't ignore the folder any longer. After this the deployment had no issues and the CSS loaded.
* When testing the connection from front-end to the back-end, CORS errors kept happening. The cause for this, was a simple typo in the Django settings. One of the settings necesarry to make CORS work is ```CORS_ALLOW_CREDENTIALS = True```. This was set, but not instead of 'ALLOW', 'ALLOWED' was written, which made the setting not take effect. After fixing the typo, the issue was resolved.
* Signout bug: In local development, besides samesite issues, there are http and https issues. Standard, react runs a local http version of your site, but the backend logout view only accepts https. Because of this, the logout functionality wouldn't work. To mitigate this (before switching over to Gitpod completely, which would've also solved it), when running the react server, HTTPS=true was added to the npm start command.