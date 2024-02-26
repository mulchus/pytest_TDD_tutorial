Learning pytest TDD principe on https://testdriven.io/blog/modern-tdd/

in folder `/pytest_TDD_tutorial/blog_app`  
run:  
```commandline
pip install -r ../requirements.txt
python blog/init_db.py  
FLASK_APP=blog/app.py python -m flask run   
```

and in other console in folder `/pytest_TDD_tutorial/blog_app` run:  
```commandline
python -m pytest tests -m 'not e2e'
python -m pytest tests -m 'e2e'
```

