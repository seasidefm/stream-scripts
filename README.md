# stream-scripts
Python scripts that run during the stream. Used to check stream activity, long played songs, and update on screen information.

## Setup
This is a typical python project at its core, so setup your virtual env as normal.

For example, I use venv, so I'd run:

```shell
python -m venv venv
```

Afterwards install your deps. Using `pip` that's:

```shell
pip install -r requirements.txt
```

## Running the app
Since this application is intended to be run easily and deployed frequently, the config is JSON instead of `.env`. This is to reduce user error
when downloading this repo as a zip file.

Copy `example-config.json` to `config.json` and populate the values as required. NOTE: The api tokens referenced are NOT public. If you need access to this information
for some reason (such as a companion app to SeasideFM), please open an issue explaining your needs.

```shell
cp example-config.json config.json
```

Then run the app:

**Linux**
```shell
source venv/bin/activate
python main.py
```

**Windows**
```powershell
# (it's easier to run using the exe in my experience)
.\venv\Scripts\python.exe main.py # or something like this
```


