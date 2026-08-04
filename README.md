# BlogCMS

DAY 3 

## Requirements

- Python 3.12+
- pip

## Setup

1. Clone the repository

   ```bash
   git clone https://github.com/ritesharyal666/Texas_101
   ```

2. Create and activate a virtual environment

   ```bash
   python -m venv venv
   ```

   Windows:
   ```bash
   venv\Scripts\activate
   ```

   macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

3. Install dependencies

   ```bash
   pip install django
   ```

4. Apply migrations

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
   If no changes detected
   
    ```bash
   python manage.py makemigrations blog 
   python manage.py migrate
   ```

6. Create a superuser (to access `/admin/`)

   ```bash
   python manage.py createsuperuser
   ```

7. Add multiple Posts from Admin Panel (To prevent error on loading home page ) 


8. Run the development server

   ```bash
   python manage.py runserver
   ```

   The site will be available at http://127.0.0.1:8000/ and the admin panel at http://127.0.0.1:8000/admin/.
