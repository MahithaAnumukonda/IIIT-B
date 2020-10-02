Foodie Restaurant Bot

'Foodie conversational bot' (chatbot) can help users discover restaurants across several Indian cities.The main purpose of the bot is to help users discover restaurants quickly and efficiently and to provide a good restaurant discovery experience.

Prerequisites : python 3.7.x, Visual studio for python development

What to Install : Rasa

Steps to install rasa in WINDOWS OS:
Step 1: Create virtual environment (here environment name is 'chat')
>> conda create -n chat
Step 2: Activate virtual environment
>> conda activate chat
step 3: Install rasa 
>> pip install rasa
step 4: Install rasa-nlu with spacy using 
>> pip install rasa[spacy]
Step 5 : Download spacy model and link it 
>> python -m spacy download en_core_web_md
>> python -m spacy link en_core_web_md en
Step 6: Train rasa on basic models(defaut) to check if rasa is working fine.
>> rasa init

Steps to install rasa in MAC OS:

Step 1: brew install python
Step 2: Create virtual environment (here environment name is 'chat')
>> python3 -m venv --system-site-packages ./venv
Step 3: Activate virtual environment
>> source ./venv/bin/activate
Step 4: Install rasa 
>> pip install rasa 
Step 5: Download spacy model and link it 
>> python -m spacy download en_core_web_md
>> python -m spacy link en_core_web_md en

Versions_Requirements:

absl-py==0.9.0
aiofiles==0.5.0
aiohttp==3.6.2
alabaster==0.7.12
anaconda-client==1.7.2
anaconda-navigator==1.9.7
anaconda-project==0.8.3
appdirs==1.4.4
APScheduler==3.6.3
asn1crypto==1.0.1
astor==0.8.1
astroid==2.3.1
astropy==3.2.1
async-generator==1.10
async-timeout==3.0.1
atomicwrites==1.3.0
attrs==19.3.0
Babel==2.7.0
backcall==0.1.0
backports.functools-lru-cache==1.5
backports.os==0.1.1
backports.shutil-get-terminal-size==1.0.0
backports.tempfile==1.0
backports.weakref==1.0.post1
beautifulsoup4==4.8.0
bitarray==1.0.1
bkcharts==0.2
bleach==3.1.0
blinker==1.4
blis==0.2.4
bokeh==1.3.4
boto==2.49.0
boto3==1.14.47
botocore==1.17.47
Bottleneck==1.2.1
cachetools==4.1.1
certifi==2019.9.11
cffi==1.12.3
chardet==3.0.4
Click==7.0
cloudpickle==1.2.2
clyent==1.2.2
colorama==0.4.1
colorclass==2.2.0
coloredlogs==10.0
colorhash==1.0.2
comtypes==1.1.7
conda==4.7.12
conda-build==3.18.9
conda-package-handling==1.6.0
conda-verify==3.4.2
contextlib2==0.6.0
cryptography==2.7
cycler==0.10.0
cymem==2.0.3
Cython==0.29.13
cytoolz==0.10.0
dask==2.5.2
decorator==4.4.0
defusedxml==0.6.0
distlib==0.3.1
distributed==2.5.2
dnspython==1.16.0
docopt==0.6.2
docutils==0.15.2
en-core-web-md==2.1.0
entrypoints==0.3
et-xmlfile==1.0.1
fastcache==1.1.0
fbmessenger==6.0.0
filelock==3.0.12
Flask==1.1.1
fsspec==0.5.2
future==0.17.1
gast==0.2.2
gevent==1.4.0
glob2==0.7
google-auth==1.20.1
google-auth-oauthlib==0.4.1
google-pasta==0.2.0
greenlet==0.4.15
grpcio==1.31.0
h11==0.8.1
h2==3.2.0
h5py==2.9.0
HeapDict==1.0.1
hpack==3.0.0
hstspreload==2020.8.18
html5lib==1.0.1
httplib2==0.18.1
httptools==0.1.1
httpx==0.9.3
humanfriendly==8.2
hyperframe==5.2.0
idna==2.8
imageio==2.6.0
imagesize==1.1.0
importlib-metadata==0.23
ipykernel==5.1.2
ipython==7.8.0
ipython-genutils==0.2.0
ipywidgets==7.5.1
isort==4.3.21
itsdangerous==1.1.0
jdcal==1.4.1
jedi==0.15.1
Jinja2==2.10.3
jmespath==0.10.0
joblib==0.13.2
json5==0.8.5
jsonpickle==1.4.1
jsonschema==3.2.0
jupyter==1.0.0
jupyter-client==5.3.3
jupyter-console==6.0.0
jupyter-core==4.5.0
jupyterlab==1.1.4
jupyterlab-server==1.0.6
kafka-python==1.4.7
Keras-Applications==1.0.8
Keras-Preprocessing==1.1.0
keyring==18.0.0
kiwisolver==1.1.0
lazy-object-proxy==1.4.2
libarchive-c==2.8
llvmlite==0.29.0
locket==0.2.0
lxml==4.4.1
Markdown==3.2.2
MarkupSafe==1.1.1
matplotlib==3.1.1
mattermostwrapper==2.2
mccabe==0.6.1
menuinst==1.4.16
mistune==0.8.4
mkl-fft==1.0.14
mkl-random==1.1.0
mkl-service==2.3.0
mock==3.0.5
more-itertools==7.2.0
mpmath==1.1.0
msgpack==0.6.1
multidict==4.7.6
multipledispatch==0.6.0
murmurhash==1.0.2
navigator-updater==0.2.1
nbconvert==5.6.0
nbformat==4.4.0
networkx==2.4
nltk==3.4.5
nose==1.3.7
notebook==6.0.1
numba==0.45.1
numexpr==2.7.0
numpy==1.16.5
numpydoc==0.9.1
oauth2client==4.1.3
oauthlib==3.1.0
olefile==0.46
openpyxl==3.0.0
opt-einsum==3.3.0
packaging==20.4
pandas==0.25.1
pandocfilters==1.4.2
parso==0.5.1
partd==1.0.0
path.py==12.0.1
pathlib2==2.3.5
patsy==0.5.1
pep8==1.7.1
pickleshare==0.7.5
pika==1.1.0
Pillow==6.2.0
pkginfo==1.5.0.1
plac==0.9.6
pluggy==0.13.0
ply==3.11
preshed==2.0.1
prometheus-client==0.7.1
prompt-toolkit==2.0.10
protobuf==3.13.0
psutil==5.6.3
psycopg2-binary==2.8.5
py==1.8.0
pyasn1==0.4.8
pyasn1-modules==0.2.8
pycodestyle==2.5.0
pycosat==0.6.3
pycparser==2.19
pycrypto==2.6.1
pycurl==7.43.0.3
pydot==1.4.1
pyflakes==2.1.1
Pygments==2.4.2
PyJWT==1.7.1
pykwalify==1.7.0
pylint==2.4.2
pymongo==3.8.0
pyodbc==4.0.27
pyOpenSSL==19.0.0
pyparsing==2.4.2
pyreadline==2.1
pyrsistent==0.15.4
PySocks==1.7.1
pytest==5.2.1
pytest-arraydiff==0.3
pytest-astropy==0.5.0
pytest-doctestplus==0.4.0
pytest-openfiles==0.4.0
pytest-remotedata==0.3.2
python-crfsuite==0.9.7
python-dateutil==2.8.0
python-engineio==3.12.1
python-socketio==4.5.1
python-telegram-bot==12.8
pytz==2019.3
PyWavelets==1.0.3
pywin32==223
pywinpty==0.5.5
PyYAML==5.1.2
pyzmq==18.1.0
QtAwesome==0.6.0
qtconsole==4.5.5
QtPy==1.9.0
questionary==1.5.2
rasa==1.10.11
rasa-sdk==1.10.2
redis==3.5.3
regex==2020.6.8
requests==2.24.0
requests-oauthlib==1.3.0
requests-toolbelt==0.9.1
rfc3986==1.4.0
rocketchat-API==1.3.1
rope==0.14.0
rsa==4.6
ruamel-yaml==0.15.46
ruamel.yaml==0.16.10
ruamel.yaml.clib==0.2.0
s3transfer==0.3.3
sanic==19.12.2
Sanic-Cors==0.10.0.post3
sanic-jwt==1.4.1
Sanic-Plugins-Framework==0.9.3
scikit-image==0.15.0
scikit-learn==0.22.2.post1
scipy==1.5.2
seaborn==0.9.0
Send2Trash==1.5.0
simplegeneric==0.8.1
singledispatch==3.4.0.3
six==1.12.0
sklearn-crfsuite==0.3.6
slackclient==2.8.0
sniffio==1.1.0
snowballstemmer==2.0.0
sortedcollections==1.1.2
sortedcontainers==2.1.0
soupsieve==1.9.3
spacy==2.1.9
Sphinx==2.2.0
sphinxcontrib-applehelp==1.0.1
sphinxcontrib-devhelp==1.0.1
sphinxcontrib-htmlhelp==1.0.2
sphinxcontrib-jsmath==1.0.1
sphinxcontrib-qthelp==1.0.2
sphinxcontrib-serializinghtml==1.1.3
sphinxcontrib-websupport==1.1.2
spyder==3.3.6
spyder-kernels==0.5.2
SQLAlchemy==1.3.9
srsly==1.0.2
statsmodels==0.10.1
sympy==1.4
tables==3.5.2
tabulate==0.8.7
tblib==1.4.0
tensorboard==2.1.1
tensorflow==2.1.1
tensorflow-addons==0.7.1
tensorflow-estimator==2.1.0
tensorflow-hub==0.8.0
tensorflow-probability==0.9.0
termcolor==1.1.0
terminado==0.8.2
terminaltables==3.1.0
testpath==0.4.2
thinc==7.0.8
toolz==0.10.0
tornado==6.0.3
tqdm==4.36.1
traitlets==4.3.3
twilio==6.26.3
typing-extensions==3.7.4.2
tzlocal==2.1
ujson==2.0.3
unicodecsv==0.14.1
urllib3==1.24.2
virtualenv==20.0.31
wasabi==0.7.1
wcwidth==0.1.7
webencodings==0.5.1
webexteamssdk==1.3
websockets==8.1
Werkzeug==0.16.0
widgetsnbextension==3.5.1
win-inet-pton==1.1.0
win-unicode-console==0.5
wincertstore==0.2
wrapt==1.11.2
xlrd==1.2.0
XlsxWriter==1.2.1
xlwings==0.15.10
xlwt==1.3.0
yarl==1.5.1
zict==1.0.0
zipp==0.6.0

---> Generated ZOMATO API key is configured directly in Rasa_basic_folder/city_checck.py and Rasa_basic_folder/zomato_slots.py
----> The model has already been trained and provided in the Rasa_basic_folder/models/

Steps to test :

Step 1: enter command 'rasa run actions' in one terminal and wait for session to activate

Steps 2: After the session has been activated in terminal 1, open terminal 2 and give 'rasa shell' command to test the bot.

Here you go... Happy Testing!!!!! Play around with the bot :)

