   Hospital Management System (Django)

A modern, responsive web application for managing hospital operations, built with Django. This system allows staff to manage doctors, patients, and appointments efficiently, with a beautiful UI and exportable data tables.

     Features

-   Admin Dashboard:  
  - View counts of doctors, patients, and appointments in a visually appealing dashboard.
  - Animated cards and icons for a modern look.
-   Doctor Management:  
  - Add, view, and delete doctors.
  - Specialization and contact info fields.
-   Patient Management:  
  - Add, view, and delete patients.
  - Gender, contact, and address fields.
-   Appointment Management:  
  - Add, view, and delete appointments.
  - Select doctor and patient, set date and time.
-   Authentication:  
  - Staff login required for admin features.
  - Secure session management.
-   DataTables Integration:  
  - Export patient, doctor, and appointment tables to Excel, CSV, PDF, or copy.
  - Search, sort, and paginate tables.
-   Beautiful UI:  
  - Bootstrap 5 and Font Awesome for responsive, modern design.
  - Custom CSS for animations (fade-in, hover, button effects).
  - Animated alerts and confirmation dialogs.
-   About & Contact Pages:  
  - Informative about page with animated icons.
  - Contact page with email, phone, and address info.

     Technologies Used

- Python 3.13+
- Django 5.2+
- Bootstrap 5
- Font Awesome
- DataTables JS
- Custom CSS animations

     Setup Instructions

1.   Clone the repository:  
         
   git clone https://github.com/devyanshm/django-project.git
   cd django-project
         
2.   Create and activate a virtual environment:  
         
   python -m venv venv
   .\venv\Scripts\Activate
         
3.   Install dependencies:  
         
   pip install -r requirements.txt
         
4.   Apply migrations:  
         
   python manage.py migrate
         
5.   Create a superuser (admin):  
         
   python manage.py createsuperuser
         
6.   Run the development server:  
         
   python manage.py runserver
         
7.   Access the app:  
   - Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

     File Structure

        
hospmgmt/
├── hospmgmt/              Django project settings
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── hosp/                  Main app
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   │   ├── navbar.html
│   │   ├── index.html
│   │   ├── about.html
│   │   ├── login.html
│   │   ├── contacts.html
│   │   ├── add_patient.html
│   │   ├── add_doctor.html
│   │   ├── add_appointment.html
│   │   ├── view_patient.html
│   │   ├── view_doctor.html
│   │   ├── view_appointment.html
│   ├── static/
│   │   └── css/
│   │       └── custom.css
│   └── ...
├── db.sqlite3             SQLite database
├── requirements.txt       Python dependencies
├── .gitignore
└── manage.py
      

     Customization & Extensibility
- Easily add new fields to models for more data.
- Add new pages or features by creating new templates and views.
- Customize CSS in   static/css/custom.css   for branding.

     Deployment
- For production, set   DEBUG = False   and configure   ALLOWED_HOSTS   in   settings.py  .
- Use   STATIC_ROOT   and   collectstatic   for static files.
- Consider using Gunicorn and a web server (e.g., Nginx) for deployment.

     License
This project is for educational/demo purposes. You may use and modify it as needed.

     Author
- GitHub: [devyanshm](https://github.com/devyanshm)


