Learning pytest TDD principe on https://testdriven.io/blog/modern-tdd/

in folder /pytest_TDD_tutorial/blog_app
run:
python blog/init_db.py  # for create table in db
FLASK_APP=blog/app.py python -m flask run   # run flask app

and in other console run:
python -m pytest tests -m 'not e2e'
python -m pytest tests -m 'e2e'
