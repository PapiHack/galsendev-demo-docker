# GalsenDEV Docker Demo

[![Open Source Love png1](https://badges.frapsoft.com/os/v1/open-source.png?v=103)](https://github.com/ellerbrock/open-source-badges/)
![Issues](https://img.shields.io/github/issues/PapiHack/galsendev-demo-docker)
![PR](https://img.shields.io/github/issues-pr/PapiHack/galsendev-demo-docker)
[![python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
[![python](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

This is a basic `Django` dev environment setup with `docker` and `docker-compose` for a [GalsenDev](https://github.com/Galsen-Dev-LAB) Meetup.
The main purposes was to make a simple presentation of `docker` and its capabilities.

## Installation

- First, you need to install `docker` and `docker-compose` in your system. Checkout the official docs:

    [docker official docs](https://docs.docker.com/get-docker/)

    [docker-compose official docs](https://docs.docker.com/compose/install/)

- After having cloned this repo, go to it using your terminal and enter the following command:

    `docker-compose up`

- If you have issues related to permission or write rights, you can run : 

    `sudo chown -R $USER:$USER .`

- If everything goes well, congratulations, you can start coding! You can visit <http://localhost:8000>

## Environment variable usage

If you take a good look at the docker compose file, I hardened the database credentials, which is not a good practice. To remedy this, it is better to use environment variables instead of hardening these values in the configurations.
You'll fine the updated `docker-compose` and `.env` file on [docker official docs](https://github.com/PapiHack/galsendev-demo-docker/tree/set-env-variables)

- Pull the branch [set-env-variables](https://github.com/PapiHack/galsendev-demo-docker/tree/set-env-variables)

- Rename `.env.example` file by `.env` and set values for variables defined in it

- Run the following command: `docker-compose --env-file .env up`

- Happy code!

## Contributing

Feel free to make a PR or report an issue 😃

Oh, one more thing, please do not forget to put a description when you make your PR 🙂

## Contributors

- [M.B.C.M](https://itdev.herokuapp.com)
[![My Twitter Link](https://img.shields.io/twitter/follow/the_it_dev?style=social)](https://twitter.com/the_it_dev)