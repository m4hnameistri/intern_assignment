# intern_assignment
Hi interviewer
I want to say something about the application:

  1. Why did I deploy the application on Pythonanywhere ? I have met some troubles with DigitalOcean registration. They declined my VISA card so I can't register a free account to deploy the application.     Importantly, the deadline is approaching so I will find the solutions later.
  2. The design and animations are still somewhat poor hehe, but overall, I have completed most of the 'Must have' features.

This is the instruction for running the project locally:
Open cmd 
1. git clone https://github.com/m4hnameistri
2. cd golden_sneaker
3. python -m venv venv  # Create a virtual environment
   venv/bin/activate  # Activate the virtual environment (Windows)
   pip install -r requirements.txt
4. This project using MySQL: so you need to create schema in MySQL first.
   python manage.py migrate
5. Run the project:
   python manage.py runserver
   The project should now be running at http://127.0.0.1:8000/.

Thank you for your time. Have a good day!
