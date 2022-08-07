# Spotify Twitter Banner

Dynamic Twitter banner to display your spotify status, elegantly.

## Installation and Usage

### Install the dependencies

The project uses pipenv for dependencies. Here's how to install the dependencies.

```sh
pipenv sync -d
```

### Setting up Spotify API for the project

- Go to the developer panel at spotify. [Panel URL](https://developer.spotify.com).
- Create an app, Specify the name, and description.
- Add `http://localhost:8888/callback` or any local URL to the callback URLs.
- **(Optional step)** If the callback URL is not `http://localhost:8888/callback`, set the `.env` variable
  `SPOTIFY_REDIRECT_URI` to the callback URL.
- Take a note of the Client ID, and Client Secret for setting up `.env`

### Setting up Twitter API

- Go to the developer panel [here](https://developer.twitter.com/).
- Create an app and set it up.
- Go to the app, navigate to Keys and Tokens and generate the keys.
- Get the Consumer Key, Consumer Secret, and Access Token, and Access Token Secret. Note them for `.env` setup.

### Environmental variables

To run this project, you will need to properly configure environmental variables. Configure them by renaming
the `.env.example` file to `.env` and setting the values.

### Authentication with Spotify

Callback based authentication has been built into the app. If you're running for the first time, or the refresh
token stored in the configuration file (`~/.spotify_refresh_token`) could not be discovered, you will be prompted
to authenticate with Spotify. You will be asked to open a URL, which redirects to the callback URL setup. Copy the
code from the URL and paste it in the terminal.

### Configuration.

All the configuration for the app is located in the `config.py` file. To maintain clean configuration, They
have been split into 3 classes. All the core configuration needed to customize and run the app is loaded
from the environmental variables.

Here is the workflow on setting up:

- Install the dependencies.
- Set up the Spotify API.
- Set up the Twitter API.
- Configure the environmental variables to your liking.

### 🚀 Run the app!

Great! You're all set. Now, run the app using,

```sh
pipenv run start
```

And, you're good to go!

## 🛠 Development

There are scripts located in the `scripts` directory meant for use during development stage, such as
testing the generation of image, or uploading banner to twitter. Make sure of using them when developing
the app. Use these to test the specific feature you have made change in.

There are scripts available for user usage, or development purposes.

Here are the scripts that you can use for development:

- **Generate Image** - `python -m scripts.generate_image`
- **Update banner** - `python -m scripts.update_banner`

NOTE: The `update_refresh_token` script is is meant for user usage to get their refresh token.

If you're interested in contributing, scroll down to the contributing section. You can find more information
about getting started.

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can
just submit a PR to this repo, and it will be deployed once it's accepted.

⚠ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your
commit or the PR Created. Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before
making the commit message.

Find out more about our contributing guidelines [here](CONTRIBUTING.md).

## Show your support

We love people's support in growing and improving. Be sure to drop a 🌟 if you like the project and
also be sure to contribute, if you're interested!

<div align="center">Made by Sunrit Jana with ❤</div>
