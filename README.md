
<!-- README template from: https://github.com/othneildrew/Best-README-Template -->
<a name="readme-top"></a>


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/HE-Arc/neurona">
    <img src="https://github.com/HE-Arc/neurona/assets/84662037/e611b1de-c188-4610-915e-0e7bfdf34de8" alt="Logo" width="400">
  </a>

<h3 align="center">Neurona</h3>

  <p align="justify">
    Neurona is a dynamic exchange platform tailored for the HE-Arc community. It facilitates vibrant discussions across various topics through a structured system of spaces, posts, and comments. This document details the already existing initial specifications, giving more context and information for each task.

  <br>
  <a href="https://github.com/HE-Arc/neurona/wiki"><strong>Explore the docs »</strong></a>
  <br>
  <br>
  <a href="https://neurona.k8s.ing.he-arc.ch/">View Demo</a>

  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* [Django](https://www.djangoproject.com/)
* [VueJS](https://vuejs.org/)
* [Vuetify](https://vuetifyjs.com/en/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple example steps.

### Prerequisites


### Installation
#### Clone the repository
> With SSH
   ```sh
   git clone git@github.com:HE-Arc/neurona.git
   ```
> With HTTP
   ```sh
   git clone https://github.com/HE-Arc/neurona.git
   ```

If you are working with Docker, skip to the <a href="#docker">Docker</a> section  

#### Docker
In a terminal in the project's current folder
   ```sh
   docker compose up -d
   ```

Once the images have been built, the containers will launch automatically. The application is available at http://localhost:3000.

#### Without docker

Before you start, ensure you have the following installed on your machine:

- `Python (3.8 or later)`

- `Node.js (14.x or later)`

- `PostgreSQL (12.x or later)`

- `Git`

##### 1. Clone the Project

First, clone the project repository from GitHub to your local machine.

```sh
git clone https://github.com/HE-Arc/neurona.git
cd neurona
```

##### 2. Set Up the Backend

###### Install Python:
Download and install Python from [python.org](https://www.python.org/downloads/).

###### Set up a virtual environment:
Navigate to the project's root directory in your terminal and run the following commands:

```sh
pip install pipenv
```

###### Install project dependencies

```sh
pipenv install
```

###### Activate the virtual environment :

```sh
pipenv shell
```

###### Execute migrations (database must be configured, otherwise ignore): 

```sh
python manage.py migrate
```

##### 3. Configure PostgreSQL

Download and install PostgreSQL from [PostgreSQL official site](https://www.postgresql.org/download/windows/).

###### Create a database:
Open the PostgreSQL command line client, psql, and run:

```sql
CREATE DATABASE neuronaApp;
CREATE USER admin WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE neuronaApp TO admin;
```

###### Configure the Django project's settings:
Open the Django project's settings file (settings.py) and configure the DATABASES setting:

```py

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'neuronaApp',
            'USER': 'admin',
            'PASSWORD': 'yourpassword',
            'HOST': 'localhost',
            'PORT': '',  # Default is 5432
        }
    }
```

###### Make Migrations

Generate the database schema by running these commands:

```sh
python manage.py migrate neuronaApp
python manage.py migrate neuronaLogs --database logs
```

##### 4. Set Up the Frontend

Download and install Node.js from Node.js official site.

Navigate to the directory containing the Vue project (frontend folder) and install the necessary packages:

```sh
cd frontend
npm install
```

##### 4. Run the Project

###### Run the Django Development Server

In the directory of the Django project, activate the virtual environment if it's not already activated and run:

```sh
python manage.py runserver
```

###### Run the Vue Development Server

Open a new command line window, navigate to the Vue project directory, and run:

```sh
npm run dev
```

This will start the Vite development server, usually accessible at http://localhost:3000.

##### 5. Access the Application

With both servers running, you can access the frontend of your application by opening http://localhost:3000 in a web browser. The backend will be accessible at http://localhost:8000.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap
See the [RoadMap](https://github.com/HE-Arc/neurona/wiki/Roadmap)

See the [open issues](https://github.com/HE-Arc/neurona/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

* Nima Dekhli - [github@ylked](https://github.com/ylked) - [nima@dekhli.ch](mailto:nima@dekhli.ch?subject=[GitHub]%20Neurona)
* Sami Nouidri - [github@lugopi](https://github.com/saminouidri) - [sami.nouidri@he-arc.ch](mailto:sami.nouidri@he-arc.ch?subject=[GitHub]%20Neurona)
* Mathias Salmon - [github@ClawdeenFleury](https://github.com/Nicomatox) - [mathias.salmon@he-arc.ch](mailto:mathias.salmon@he-arc.ch?subject=[GitHub]%20Neurona)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/HE-Arc/neurona.svg?style=for-the-badge
[contributors-url]: https://github.com/HE-Arc/neurona/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/HE-Arc/neurona.svg?style=for-the-badge
[forks-url]: https://github.com/HE-Arc/neurona/forks
[stars-shield]: https://img.shields.io/github/stars/HE-Arc/neurona.svg?style=for-the-badge
[stars-url]: https://github.com/HE-Arc/neurona/stargazers
[issues-shield]: https://img.shields.io/github/issues/HE-Arc/neurona.svg?style=for-the-badge
[issues-url]: https://github.com/HE-Arc/neurona/issues
[license-shield]: https://img.shields.io/badge/license-MIT-green?style=for-the-badge
[license-url]: https://github.com/HE-Arc/neurona/blob/main/LICENSE
[Laravel.com]: https://img.shields.io/badge/Laravel-10.28.0-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Tailwind.com]: https://img.shields.io/badge/Tailwind%20CSS-3.3.7-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white
[Tailwind-url]: https://tailwindcss.com/
[Flowbite.com]: https://img.shields.io/badge/Flowbite-3B82F6?style=for-the-badge&logo=flowbite-css&logoColor=white
[Flowbite-url]: https://flowbite.com

