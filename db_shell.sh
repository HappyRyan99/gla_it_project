# recreate database
python manage.py makemigrations rango
# init DB
python manage.py migrate
# create superuser
python manage.py createsuperuser
# accroding app models to generate table
python manage.py sqlmigrate rango 0001
# check your table sql
python manage.py makemigrations rango
# generate database
python manage.py migrate
# run population to filling the data
python populate_rango.py