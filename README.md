# Spotify Twitter Banner

Dynamic Twitter banner, to show off your spotify status. Banner updated every 5 minutes.

## Installation and Usage

### Install the dependencies

The project uses pipenv for dependencies. Here's how to install the dependencies.

```sh
pipenv sync -d
```

### Setting up Spotify API for the project

- Go to the developer panel at spotify. [Panel URL](https://developer.spotify.com).
- Make an App, Specify the name, and description.
- Add `http://localhost:8888/callback` to the Callback URLs.
- Take a note of the Client ID, and Client Secret for setting up `.env`

### Setting up Twitter API

- Go to the developer panel [here](https://developer.twitter.com/).
- Create an App and set it up.
- Go to the app, navigate to Keys and Tokens and generate the keys.
- Get the Consumer Key, Consumer Secret, and Access Token, and Access Token Secret. Note them for `.env` setup.

### Environmental variables

To run this project, you need to properly configure environmental variables. Configure the environmental
variables by renaming the `.env.example` file to `.env` with the respective values.

### Authentication with Spotify

Callback based authentication has been built into the App. If you're running for the first time, or the refresh
token stored in the configuration file (`~/.spotify_refresh_token`) could not be discovered, you will be prompted
to authenticate with Spotify. You'll be asked to open an URL, which redirects to the callback URL setup. Copy the
code from the URL and paste it in the terminal.

### Configuration.

All of the configuration for the app is located in the `config.py` file. To maintain clean configuration, They
have been split into 3 classes. You can configure the settings in the config file, as you wish and also ensure
that the variables are set properly, and they work.

Along with that, you can also change the interval of the banner update, in `__main__.py` where the `sleep` is run.

To sum it up, Here is the workflow on setting up:
- Install the dependencies.
- Set up the Spotify API.
- Set up the Twitter API.
- Configure settings and interval as you like.

### 🚀 Run the app!

Great! You're good to go. Now, Just run the app using,

```sh
pipenv run start
```

And, you're all set!

## 🤝 Contributing

Contributions, issues and feature requests are welcome. After cloning & setting up project locally, you can just submit
a PR to this repo and it will be deployed once it's accepted.

⚠ It’s good to have descriptive commit messages, or PR titles so that other contributors can understand about your
commit or the PR Created. Read [conventional commits](https://www.conventionalcommits.org/en/v1.0.0-beta.3/) before
making the commit message.

Find out more about our contributing guidelines [here](CONTRIBUTING.md).

## Show your support

We love people's support in growing and improving. Be sure to leave a 🌟 if you like the project and
also be sure to contribute, if you're interested!

<div align="center">Made by Sunrit Jana with ❤</div>
