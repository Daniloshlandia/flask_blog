if [ ! -d "venv" ]; then
    echo --------------------
    echo Creating virtualenv
    echo --------------------
# add path for u virtualenv if use pyenv 
    virtualenv venv


fi
source venv/bin/activate

pip install -r requirements.txt

export FLASK_APP=main.py
if [ ! -d "migrations" ]; then
    echo --------------------
    echo INIT THE migrations folder
    echo --------------------
    export FLASK_APP=main.py; flask db init
fi
#migration for SQLite maybe work with postgrest and Mysql i don't know
echo --------------------
echo Generate migration DDL code
echo --------------------
flask db migrate
echo --------------------
echo Run the DDL code and migrate
echo --------------------
echo --------------------
echo This is the DDL code that will be run
echo --------------------
flask db upgrade
echo --------------------
echo Generating test data
echo --------------------
#data test bey pydata extesion flask 
flask test-data


