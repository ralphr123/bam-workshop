## Introduction (see manual.pdf for full instructions)

As part of this lab, students are guided through a series of four exercises, to be completed in order. The exercises consist of four Python APIs that the students are expected to complete. As they complete them, the frontend will become functional and the next exercises will light up, becoming available to complete. The frontend is already built for the students; they need only to complete the backend code to finish the lab.

Once each exercise is completed, the next one will unlock. Every time an exercise page is opened, students will have a test area in the center, a Run tests button on the bottom right, and a Back button on the top left. 

![image](https://github.com/ralphr123/bex-workshop-sol/assets/29685125/87f83a6a-bd4f-4f6e-a39f-ee9d8a8fa882)


**Back button**: Takes students back to the home page
**Test area**: Test Python code by interacting with the test area.
**Run tests button**: Once students are ready to verify their code, they click on _Run tests_. It will light up green if the backend implementation is correct, and the exercise is completed. Otherwise students can retry as many times as they’d like.

Once students successfully complete an exercise, they can go back to the home page and start the next one whenever they’re ready. 

![image](https://github.com/ralphr123/bex-workshop-sol/assets/29685125/920ecebd-ba6d-4dab-a502-a1210b4fbb18)

There are four exercises in this lab, each one being a Python API students have to complete:
1. (POST /exercise1) Send a single message to GPT
![image](https://github.com/ralphr123/bex-workshop-sol/assets/29685125/68762092-cb31-4f8d-9c4e-6af631de38e1)
2. (POST /exercise2) Maintain a conversation history with GPT
![image](https://github.com/ralphr123/bex-workshop-sol/assets/29685125/d80bf9e8-16f0-41eb-a814-5fff6d365349)
3. (POST /exercise3) Send a system prompt to GPT before a conversation.
![image](https://github.com/ralphr123/bex-workshop-sol/assets/29685125/6692d283-bc19-44c6-ae06-4db07989af78)
4. (GET /exercise4) Develop a prompt to get GPT to translate maze codes into readable instructions
![image](https://github.com/ralphr123/bex-workshop-sol/assets/29685125/391f964f-5def-4f4a-b2c6-2ee84553f62e)

## Installation

To be able to run this app locally, you will need both Docker and Git installed on your machine.

#### Mac with intel chip

1. **Docker:** [link](https://desktop.docker.com/mac/main/amd64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-amd64)
2. **Git:** If not preinstalled, running `git --version` in the command line will guide you through installing it.

#### Mac with M1/M2 chip

1. **Docker:** [link](https://desktop.docker.com/mac/main/arm64/Docker.dmg?utm_source=docker&utm_medium=webreferral&utm_campaign=docs-driven-download-mac-arm64)
2. **Git:** If not preinstalled, running `git --version` in the command line will guide you through installing it.

#### Windows

1. **Docker:** [link](https://desktop.docker.com/win/main/amd64/Docker%20Desktop%20Installer.exe)
2. **Git:** [link](https://github.com/git-for-windows/git/releases/download/v2.41.0.windows.1/Git-2.41.0-32-bit.exe)

## Quick start

1. **Clone the app:** Run `git clone https://github.com/ralphr123/bam-workshop && cd bam-workshop`
2. **Run the app:** In your project directory root, run `export PASSPHRASE=<passphrase> && docker-compose up`
3. **Stop the app:** CTRL + C in the terminal window where the app is running
