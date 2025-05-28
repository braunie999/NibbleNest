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
- Wireframes created with Figma.

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
- Media: Cloudinary for image storage
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

### Heroku Deployment

---

## Security & Best Practices

---

## Credits & Acknowledgements

---

### Resources
