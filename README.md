# UPGRADE Dining University Leaderboard

A Django web application that ranks US universities on their plant-based dining progress. Built by Harper Dunn as part of the [UPGRADE Dining](https://upgradedining.org/) campaign.
Visit the site here: https://pbrating.onrender.com/


## What It Does

The leaderboard scores universities across metrics like vegan meal offerings, formal sustainability commitments, culinary training, and purchasing practices. Students can sign in with Google and submit reviews of their university's plant-based dining. Universities are assigned a letter grade (F through A-) based on a point system with a maximum of 740 points.

## Tech Stack

- **Backend:** Django 4.2, Python 3.11
- **Database:** PostgreSQL (via `dj-database-url`)
- **Auth:** Google OAuth via `django-allauth` (Google sign-in only — no email/password signup)
- **File Storage:** AWS S3 + CloudFront CDN for media uploads
- **Static Files:** AWS S3
- **Deployment:** Render (via Gunicorn + WhiteNoise)
- **Frontend:** Bootstrap 5, Font Awesome, Alpine.js

## Project Structure

```
pbrProject/
├── leaderboard/            # Main Django app
│   ├── models.py           # University, Review, UniversityImage, UniversityTestimonial
│   ├── views.py            # Page views (leaderboard, university detail, profile, etc.)
│   ├── urls.py             # URL routing
│   ├── forms.py            # ReviewForm
│   ├── admin.py            # Admin panel config
│   ├── adapters.py         # Allauth adapters (Google-only signup)
│   ├── signals.py          # Auto-update university rating on review save/delete
│   └── templates/          # HTML templates
│       ├── master.html     # Base layout with navbar
│       ├── unis.html       # Leaderboard table
│       ├── unidetails.html # University detail page
│       ├── profile.html    # User profile + review submission
│       ├── about.html      # About the campaign
│       └── methodology.html# Scoring methodology
├── pbrProject/
│   └── settings.py         # Django settings
├── urls.py                 # Root URL config
├── manage.py
├── requirements.txt
└── Procfile                # For Render deployment
```

## Scoring System

Universities are scored across three tiers:

| Tier | Max Points | Examples |
|------|-----------|---------|
| High Impact | 300 | % animal-based purchases, formal commitments, vegan meals per day |
| Medium Impact | 300 | Culinary training, default-veg program, breakfast options, student satisfaction |
| Low Impact | 140 | Labeling, naming, plant-based desserts, salad bar protein options |

Grades are assigned on a scale from **F** (< 75 pts) to **A-** (400+ pts).


## Key Models

- **`University`** — Stores all scoring data fields and computes its own `overallScore` and `overallGrade` automatically on save.
- **`Review`** — User-submitted reviews linked to a `University` and a `User`. Triggers a signal to update the university's cached average rating.
- **`UniversityImage`** — Images uploaded via the admin panel, stored on S3/CloudFront.
- **`UniversityTestimonial`** — Manually added testimonials (moderated via `approved` flag).


## Authentication Notes

- Only Google sign-in is supported 

## Contributing

This project is part of an active campaign. If you're a student who wants to submit data for your university, visit the live leaderboard and use the Google sign-in to leave a review.
