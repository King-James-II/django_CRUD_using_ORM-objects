# CRUD on Django Model Objects

## Description
This project contains Django models for managing users, learners, instructors, courses, lessons, and enrollments.

## Models Overview

### User Model
- Fields:
  - `first_name`: First name of the user.
  - `last_name`: Last name of the user.
  - `dob`: Date of birth of the user.

### Learner Model
- Inherits from `User`.
- Additional Fields:
  - `occupation`: Occupation of the learner.
  - `social_link`: Social media link of the learner.

### Instructor Model
- Inherits from `User`.
- Additional Fields:
  - `full_time`: Boolean indicating if the instructor is full-time.
  - `total_learners`: Total number of learners taught by the instructor.

### Course Model
- Fields:
  - `name`: Name of the course.
  - `description`: Description of the course.
- Relationships:
  - Many-to-Many relationship with `Instructor`.
  - Many-to-Many relationship with `Learner` via `Enrollment`.

### Lesson Model
- Fields:
  - `title`: Title of the lesson.
  - `course`: Foreign key relationship with `Course`.
  - `content`: Content of the lesson.

### Enrollment Model
- Fields:
  - `learner`: Foreign key relationship with `Learner`.
  - `course`: Foreign key relationship with `Course`.
  - `date_enrolled`: Date of enrollment.
  - `mode`: Enrollment mode (audit or honor).

## Usage
You can use these models to manage users, learners, instructors, courses, lessons, and enrollments in your Django project.