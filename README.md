# Profile Manager Backend

**Author:** Catalina Restrepo Salgado

## Summary

This repository corresponds to my solution on the technical assesment presented for applying to the Systems Engineerign Intern Position at Factored

Here, you'll fin the API for a web application designed and developed to find and manage easily the corportate profile of workers in the company. A dummy profile was added for test purposes.

## Requirements

This project was dockerized so you can use it easily. You need to install the following tools:

- Docker.
- Docker compose (optional).

## Instructions

1. **Make a clon of the repository**

First, you need to make a copy of the repository on your local machine using the following commands in a console like `cmd` or `bash`.

    ```bash
    git clone https://github.com/CatalinaRpoS/profile-manager-backend
    cd profile-manager-backend
    ```

2. **Without Docker Compose:**

If you haven't installed Docker Compose, you must perform the following steps:

- Create an `.env` file in the project with the same information you can find in the `.env.example` file that there's in the repository.

- Open a console and run the following commands:

    ```bash
    docker build -t profile-manager-backend .
    docker run -d -p 8000:8000 --name backend profile-manager-backend
    ```

3. **With Docker Compose:**

If you have already installed Docker Compose in your computer, you just need to run the following command in the console of the project.

    ```bash
    docker-compose up --build
    ```

4. **¨Running the project**

When you have executed the commands you needed, you'll can access to the API in the direction `http://localhost:8000`. The first message you will se is: "Welcome to Profile Manager API!"

Additionally, if you want to read de **documentation** of the project, in order to know everything what it contains, you can check the `http://localhost:8000/docs` route in your web browser.

## Final message

I hope you will find this project interesting and useful, let me know anything you need to know (or if you have a suggestion that helps me to improve).

Thank you, have a nice day!
