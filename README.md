# Local deployment (Back-End)
```
git clone https://github.com/mrv83/tst_1.git
cd tst_1
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
cd backend && cp local_conf_example.py local_conf.py && cd ..
Setup DB and other custom settings in local_conf.py
./manage.py migrate
./manage.py runserver
```

# Local deployment (Front-End)
```
git clone https://github.com/mrv83/tst_1.git
cd tst_1/vue_js && npm install
npm run serve
```