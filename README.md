# company_architecture

## Feauters:
-  Authentication
- Admin panel at /admin/
- Advanced filtering 
- Fixture file
- tree structure of employees
- CRUD of employees
- Pagination
- Creating data by command ```python
python manage.py seed --number 500 
```

## Installing using GitHub:
```python
git clone https://github.com/DevSpaciX/company_architecture.git
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata company_app/fixtures/fixture_data.json 
python manage.py runserver 
```
## Getting access:
- Admin user credetnials : admin / pass : 123123 



## Screenshots:
![image](https://user-images.githubusercontent.com/102595649/235426175-b8fc0a67-6c17-4979-bf9a-f37e13ce9d6a.png)
![image](https://user-images.githubusercontent.com/102595649/235426342-a334c6dc-cf85-45c5-a8d3-4db467d4c77a.png)
![image](https://user-images.githubusercontent.com/102595649/235426359-7918bbb9-d5c6-4d98-b1db-3f58d3620a92.png)
![image](https://user-images.githubusercontent.com/102595649/235426376-09270acb-a9d6-41a8-a6f3-cbfcd794ab5e.png)
![image](https://user-images.githubusercontent.com/102595649/235426428-64666f38-f329-4302-96f9-fb6f766e5459.png)
![image](https://user-images.githubusercontent.com/102595649/235426443-90fa77c1-95f7-4227-9254-c45b32806959.png)
![image](https://user-images.githubusercontent.com/102595649/235426463-4f08e3f3-5adf-4d92-99d8-03af63322ae0.png)

