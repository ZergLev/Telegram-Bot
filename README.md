# Telegram-Bot
A beginner level bot using Dialog Flow Framework

Requirements. 

It's not recommended to use Windows if you plan on collecting data, because Apache Superset doesn't have official support for it. So far, I haven't managed to launch data collection on Windows. Instead, you could use Linux or a virtual machine.

To use the bot you need either one of: 
1. Python 3 + Dialog Flow Framework (dff[telegram, stats])
2. Docker with Docker-Compose (Can't use data collection in this mode right now, it's TBD in the future)

Running the bot.
1. Directly with your python interpreter.

In order for the bot to work, set the bot token environment variable to your bot token:
```commandline
export TG_BOT_TOKEN=*******
```
(To get the bot token follow the 'telebot' library documentation)
For now a single bot token is in the .env file. In the future it will be hidden with Docker Secrets

To run the bot, type in the terminal when in Telegram-Bot directory:
```commandline
python bot/main.py
```
Note that all dependencies (dff[telegram, stats]) need to be installed, unlike when you use Docker-Compose.
You can check out the installation guide in the official DFF documentation:
https://deeppavlov.github.io/dialog_flow_framework/get_started.html

2. Using Docker-Compose
   
To run the bot, type in the terminal:
```commandline
docker-compose run bot python main.py
```

To run the data collector, check out the official DFF User Guide on Supersets, but don't use their example_data_provider.py, as it will save that data and I don't know how to delete it from the DB, it will clog up the results. After going through the guide's first few steps, you can import the .zip dashboard configuration file from this repo to the localhost:8088 page, the instructions in the guide show the steps to do so.

Link to the guide:
https://deeppavlov.github.io/dialog_flow_framework/user_guides/superset_guide

Issues:
1. When running the bot from Docker, OpenTelemetry can't send data to the collector. I guess I just don't know enough about the two of these things to make it work.
2. When running the bot without the data collector running, you may want to ignore Command Line output. The program will inform you that it can't collect the data with OpenTelemetry. To remove that you can comment the after_handler[] lines in main.py
   
Possible TBD:
1. Maybe switch to Compose instead of Docker-Compose (OpenTelemetry marks the latter as deprecated)
