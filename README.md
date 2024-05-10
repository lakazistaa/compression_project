
# AI Model Compression Web Application

This is a web application designed for the compression of AI models, allowing users to upload AI models, select compression techniques, evaluate using different metrics, and download the compressed model.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- Python 3.8 or higher
- pip (Python package installer)
- Virtualenv (optional but recommended for package management)

## Installation

Follow these steps to get your development env running:

### Clone the repository

```bash
git clone https://github.com/lakazistaa/compression_project.git
cd compression_project
```

### Set up a Python virtual environment (Optional but recommended)

#### For Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```



## Running the application

### Apply migrations

```bash
python manage.py migrate
```

### Create a superuser

```bash
python manage.py createsuperuser
```

### Start the server

#### For Linux:
```bash
python manage.py runserver
```

#### For Windows:
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your web browser to see the application running.


## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/lakazistaa/compression_project.git](https://github.com/lakazistaa/compression_project.git)

