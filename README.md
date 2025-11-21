# GeNet AI
https://genetai.onrender.com/
Welcome to **GeNet AI**, a personal learning project focused on programming, Git, GitHub collaboration, and best practices like documentation and project organization. This repository features a key module called **WikiBot**, showcasing basic web development, Python scripting, project structuring, and integrating with local LLMs through Ollama's Llama 3.2.

---

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Project Structure](#project-structure)
- [How to Use](#how-to-use)
- [Installation Guide](#installation-guide)
- [Ollama & Llama 3.2 Setup](#ollama--llama-32-setup)
- [Contributing](#contributing)

---

## Introduction

**GeNet AI** started as a way to learn and experiment with programming, version control using Git, and sharing projects on GitHub. Here, you’ll find early experiments, learning notes, and code samples intended to grow with you as you develop your skills.

The main application is **GeNet Ai**, a Python-based web app that uses a locally-running Llama 3.2 language model via [Ollama](https://ollama.com/), allowing easy experimentation and development with large language models on your computer.

---

## Features

- 💡 Beginner-friendly Python code for learning and tinkering
- 🦙 Local language model inference with Ollama and Llama 3.2
- 📄 Organized folder structure for easy understanding
- 🌐 Simple web app (WikiBot) featuring Flask-based routes and rendering
- 🗂 Static and template directories for web organization
- 📝 This README as a living document for practice and explanation

---

## Project Structure

```
GenNet/
├── README.md               # Project documentation
└── WikiBot/
    ├── app.py              # Main Python application (Flask web server/script)
    ├── static/             # Static files (CSS, JS, images)
    └── templates/          # HTML templates for rendering web pages
```

---

## How to Use

Follow these steps to try out WikiBot or expand the project:

### 1. Clone the Repository

```bash
git clone https://github.com/MabelMoncy/GenNet.git
cd GenNet/WikiBot
```

### 2. Install Requirements

- Make sure Python 3.7+ is installed.
- (Optional but recommended) Create a virtual environment:

  ```bash
  python -m venv venv
  # Activate on Linux/macOS:
  source venv/bin/activate
  # Activate on Windows:
  venv\Scripts\activate
  ```

- Install Flask (and other potential dependencies):

  ```bash
  pip install flask
  ```

  *(If requirements.txt is present, use `pip install -r requirements.txt` instead.)*

### 3. Set Up Ollama and Llama 3.2

See the [Ollama & Llama 3.2 Setup](#ollama--llama-32-setup) section below.

### 4. Run the Application

Make sure Ollama is running with the Llama 3.2 model (see next section), then start the app:

```bash
python app.py
```

- Open your browser at [http://127.0.0.1:5000/](http://127.0.0.1:5000/) or as directed in the terminal output.

---

## Installation Guide

**Prerequisites:**
- Python 3.7 or later. [Download Python](https://www.python.org/downloads/)
- Git for version control. [Download Git](https://git-scm.com/)
- Flask (install via pip as shown above)

**Steps:**
1. Clone this repository.
2. Install Python libraries as instructed.
3. Set up Ollama and Llama 3.2 (see below).
4. Run the app!

---

## Ollama & Llama 3.2 Setup

This project connects to [Ollama](https://ollama.com/), which is an open-source framework to run language models locally.

### 1. Install Ollama

Follow instructions on [Ollama’s installation page](https://ollama.com/download) for your OS (Windows, macOS, or Linux).

Example for macOS with Homebrew:
```bash
brew install ollama
ollama serve
```

Or download the installer directly from [Ollama’s official site](https://ollama.com/download).

### 2. Download the Llama 3.2 Model

Run this in your terminal:

```bash
ollama run llama3:latest
```
or run
```bash
ollama run llama3.2
```
Or if you specifically want version 3.2:
```bash
ollama pull llama3:3.2
```
- Verify available versions with:
  ```bash
  ollama list
  ```

This will download the model onto your system via Ollama.

### 3. Start the Ollama Service

Usually, Ollama runs as a background service (daemon) after installation. If not, you can start it with:
```bash
ollama serve
```

### 4. Verify Llama 3.2 Is Running

You can test with:
```bash
ollama run llama3:3.2
```
- If you see an interactive prompt or you receive model outputs, it’s working!

### 5. Project Integration

- The WikiBot code will expect Ollama to be running locally and accessible at `http://localhost:11434` (default).
- Make sure to start Ollama **before** running the Flask app.

---

## Contributing

This repository is a space for personal learning, but contributions, forks, and suggestions are always welcome. If you find an issue or want to make improvements, feel free to open an issue or submit a pull request.

---

## License

This project is for educational and demonstration purposes. Refer to the license file (if present) for usage details, or treat as "all rights reserved" unless otherwise specified.

---

**Happy Coding!**
