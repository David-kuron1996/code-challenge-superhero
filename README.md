# **project Name**

`Superheroes API` it is a Flask-based RESTful API to track superheroes and their powers.

## **Project Description**

The Superheroes API is a Flask-based RESTful API designed to track superheroes and their powers. It allows users to manage heroes, powers, and the relationships between them (HeroPower). This project demonstrates proficiency in **Flask, Flask-SQLAlchemy, Flask-Migrate**, and **RESTful API design**.

**Key Features:**

* Retrieve a list of heroes and powers
* Retrieve a single hero or power by ID
* Update a power’s description
* Create new hero-power relationships
* Includes validations for power descriptions and hero-power strength

**The Technologies Used:**

* **Flask**: Lightweight framework suitable for building APIs
* **SQLAlchemy**: ORM to manage database relationships easily
* **Flask-Migrate**: To handle database migrations efficiently


## **Table of Contents**

1. [Installation](#installation)
2. [Usage](#usage)
3. [API Endpoints](#api-endpoints)
4. [Credits](#credits)
5. [License](#license)

## **Installation**

Follow these steps to run the project locally:

1. **Clone the repository**

```bash
git clone <your-repo-url>
cd code-challenge-superheros
```

2. **Create a virtual environment with pipenv**

```bash
pipenv install
pipenv shell
```

3. **Install required dependencies (if not using pipenv)**

```bash
pip install Flask Flask-SQLAlchemy Flask-Migrate
```

4. **Set the Flask app environment variable**

```bash
export FLASK_APP=app.py

5. **Initialize the database**

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. **Seed the database** (if you have a seed file)

```bash
python seed.py
```

7. **Run the Flask server**

```bash
flask run
```

Your API should now be running at `http://127.0.0.1:5000`.

## **Usage**

You can test the API using **Postman**, **cURL**, or any HTTP client.

### **Sample Requests**

**GET all heroes**

```
GET /heroes
```

**GET hero by ID**

```
GET /heroes/1
```

**GET all powers**

```
GET /powers
```

**GET power by ID**

```
GET /powers/1
```

**PATCH a power**

```
PATCH /powers/1
Body: { "description": "Updated description with at least 20 characters" }
```

**POST a hero-power**

```
POST /hero_powers
Body:
{
  "hero_id": 3,
  "power_id": 1,
  "strength": "Average"
}
```

**Notes:**

* `strength` must be `"Strong"`, `"Weak"`, or `"Average"`
* `description` must be at least 20 characters

You can view results of POST requests by using **GET endpoints** like `/heroes/<id>`.


