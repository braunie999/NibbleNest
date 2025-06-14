# About the Project

Nibble Nest is an aspiring go-to platform for effortless restaurant reservations, helping you discover and book the perfect spot to enjoy great food with friends and family—fast, easy, and hassle-free.

## Restaurant Booking System

A Django-based full-stack web application for restaurant reservations, enabling users to browse the menu, book tables, and manage their bookings online. The application integrates with Cloudinary for media storage and uses Django Allauth for secure user authentication.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Agile Methodology & Planning](#agile-methodology--planning)
3. [UX Design & Wireframes](#ux-design--wireframes)
4. [Features](#features)
5. [Technologies Used](#technologies-used)
6. [Database Design](#database-design)
7. [Testing](#testing)
8. [Deployment](#deployment)
9. [Security & Best Practices](#security--best-practices)
10. [Credits & Acknowledgements](#credits--acknowledgements)

## Project Overview

The Restaurant Booking System is a full-stack web application built using Django (MVC framework). It allows users to sign up, log in, browse the menu, book tables, and manage their reservations. Administrators can manage tables, bookings, and menu items via a secure admin panel. The application is designed to be responsive, accessible, and user-friendly, following modern UX and accessibility standards.

---

## Agile Methodology & Planning

- Agile methodology with GitHub issues for project tracking.
- User stories and sprints to organize development.
- Git for version control.

### User Stories

- **As a user**, I want to register and log in securely so that I can manage my bookings.
- **As a user**, I want to browse the menu so that I can see what dishes are available.
- **As a user**, I want to book a table for a specific date and time so that I can dine at the restaurant.
- **As an admin**, I want to manage bookings and tables so that I can ensure smooth operations.
- **As an admin**, I want to manage the menu items so that I can keep the offerings up-to-date.
- **As a user**, I want to view my booking history so that I can keep track of my reservations.
- **As a user**, I want to edit or cancel my bookings so that I can manage my plans easily.
- **As a user**, I want to have a responsive and accessible interface so that I can use the application on any device.
- **As a user**, I want to have a clear and intuitive navigation system so that I can find what I need quickly.

### Sprints

- **Sprint 1**: User authentication (registration, login, logout).
- **Sprint 2**: Menu browsing and table booking functionality.
- **Sprint 3**: User profile management and booking history.
- **Sprint 4**: Admin features for managing bookings, tables, and menu items.
- **Sprint 5**: UX enhancements, accessibility improvements, and responsive design.

### Project Board

You can follow all features and tasks on our [Project Board](https://github.com/braunie999/NibbleNest/projects/1).

### Issues

You can view all issues and their statuses on our [Issues Page](https://github.com/braunie999/NibbleNest/issues).

---

## UX Design & Wireframes

### User Experience (UX)

- **Accessibility**: Neutral colors, semantic HTML, ARIA labels, and alt text for images.
- **Responsive Design**: Built with Bootstrap’s grid system for seamless experience on all devices.
- **Navigation**: Clear, consistent navigation bar on all pages.
- **User Flows**: Intuitive booking and account management processes.

### Wireframes & Mockups

- **Home Page**: Features a hero image, search bar, and links to menu and booking sections.
- **Menu Page**: Displays menu items with images, descriptions, and prices.
- **Booking Page**: Allows users to select date, time, and number of guests, with a calendar for easy selection.
- **Profile Page**: Displays user information and booking history.

---

## Features

### User Features

- **Registration & Login**: Secure authentication via Django Allauth.
- **Table Booking**: Search for available tables by date/time, make reservations, view, edit, or cancel bookings.
- **Menu Browsing**: View detailed menu items with images and descriptions.
- **Profile Management**: View and manage personal bookings.

### Admin Features

- **Booking Management**: View, confirm, or reject bookings.
- **Table Management**: Add, edit, or delete tables.
- **Menu Management**: Add, edit, or remove menu items.

### Accessibility & UX

- Semantic HTML - High-contrast color palette for readability.
- Responsive layouts for mobile and desktop.
- Alt text for all images.
- Keyboard navigable forms and buttons.

### Future Enhancements

- Enhanced admin dashboard with analytics.

---

## Technologies Used

- Backend: Django, PostgreSQL (production), SQLite (development)
- Frontend: HTML, CSS, JavaScript, Bootstrap
- Media: Cloudinary for image storage still to be implemented
- Authentication: Django Allauth
- Deployment: Heroku
- Other: Git/GitHub for version control

---

## Database Design

A custom data model was designed to fit the restaurant booking domain, following Django’s ORM conventions.

### Entity-Relationship Diagram (ERD)

- **Booking**: Stores user, table, date, time, and guest count.
- **MenuItem**: Stores menu details.
- **Table**: Stores table information and capacity.

---

## Testing

---

### Manual Testing

### Automated Testing

### Bugs & Fixes

---

## Deployment

### Local Deployment

1. Clone the repository.
2. Create and activate a virtual environment.
3. Install dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations:

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Start the development server:

   ```bash
   python manage.py runserver
   ```

### Heroku Deployment

- The application is configured for deployment on Heroku. Environment variables (including Cloudinary and Django Allauth settings) are managed via Heroku's dashboard.
- Continuous delivery is enabled using GitHub integration and Heroku pipelines.
- For detailed deployment instructions, refer to the [Heroku Deployment Guide](https://devcenter.heroku.com/articles/getting-started-with-django).

---

## Security & Best Practices

---

## Credits & Acknowledgements

---

### Resources

- [Django Project](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Cloudinary](https://cloudinary.com/)
- [Django Documentation](https://docs.djangoproject.com/)
- [Bootstrap Documentation](https://getbootstrap.com/)
- [Cloudinary Documentation](https://cloudinary.com/documentation)
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/en/latest/)
