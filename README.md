# Routes

## Introduction

The initial view is not set up at the root so, you will have to navigate to /api or /auth to perform tasks. 

```json
{
	"BASE_URL": "https://crisis-octogon-3123.herokuapp.com/"
}
```

```json
{
	"api/": "BASE_URL/api",
	"auth/": "BASE_URL/auth",
	"admin/": "BASE_URL/admin",
}
```

These are the main routes for questions and answers

```json
{
	"questions": "api/questions/",
	"answers": "api/answers"
}
```

## CRUD Operations for Questions

### Create

> To add a question to the database, you must make a POST request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/questions/"
}
```

```json
{
	"date": "This expects a Date code like this '1551-01-01T18:06:00Z'",
	"rank": "The default is Zero (0)",
	"question": "",
}
```

### Read

> To get a list of all questions from the database, you must make a GET request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/questions/"
}
```

```json
[
    {
        "id": 1,
        "date": "1551-01-01T18:06:00Z",
        "rank": 0,
        "question": "Should I stay at home if I am sick?"
    },
    {
        "id": 3,
        "date": "1551-02-01T18:06:00Z",
        "rank": 0,
        "question": "How long should a isolation last?"
    }
]
```

### Update

> To update a question to the database, you must make a PUT request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/questions/{pk}/"
}
```

### Delete

> To delete a question from the database, you must make a DELETE request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/questions/{pk}/"
}
```

## CRUD Operations for Answers

### Create

> To add an answer to the database, you must make a POST request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/answers/"
}
```

```json
{
  "answer": "At least 10 days.",
  "rank": 1,
  "question": 3
}
```

### Read

> To get a list of all the answers from the database, you must make a GET request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/answers/"
}
```

```json
[
    {
        "id": 1,
        "answer": "At least 10 days.",
        "rank": 1,
        "question": 3
    },
    {
        "id": 2,
        "answer": "Yes, of course.",
        "rank": 1,
        "question": 1
    }
]
```

### Update

> To update an answer on the database, you must make a PUT request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/answers/{pk}/"
}
```

### Delete

> To delete an answer from the database, you must make a DELETE request with the fetch API or Axios.

```json
{
	"endpoint": "BASE_URL/api/answers/{pk}/"
}
```