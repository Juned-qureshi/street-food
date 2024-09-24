echo "BUILD START"
Python 3.10.8 -m pip install -r requirements.txt
Python 3.10.8 manage.py collectstatic --noinput --clear
echo "BUILD END"