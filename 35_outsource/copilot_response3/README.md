# Collaborative Storytelling Game

## Description

A collaborative storytelling game where users can start new stories or contribute to existing ones. Once a user adds to a story, they cannot add again. Users can view stories they have contributed to on their homepage.

## Features

- User registration and login
- Start a new story with a title and initial content
- Add to an existing story but only once
- View stories the user has contributed to on their homepage

## Setup

1. Clone the repository:

```bash
git clone https://github.com/yourusername/collaborative_storytelling.git
```

2. Change to the project directory:

```bash
cd collaborative_storytelling
```

3. Create a virtual environment:

```bash
python -m venv venv
```

4. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

5. Install the required packages:

```bash
pip install -r requirements.txt
```

6. Initialize the database:

```bash
python -c "from app.models import init_db; init_db()"
```

7. Run the application:

```bash
python run.py
```

8. Open a web browser and go to `http://127.0.0.1:5000/` to access the application.

## License

This project is licensed under the MIT License.