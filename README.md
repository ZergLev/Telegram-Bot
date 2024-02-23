# Telegram-Bot
A beginner level bot using Dialog Flow Framework

Requirements. 
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

To run the bot, type in the terminal:
```commandline
python main.py
```
Note that all dependencies (dff[telegram, stats]) need to be installed, unlike when you use Docker-Compose.
You can check out the installation guide in the official DFF documentation:
https://deeppavlov.github.io/dialog_flow_framework/get_started.html

2. Using Docker-Compose
To run the bot, type in the terminal:
```commandline
docker-compose run bot python main.py
```
When running the bot without the data collector running, you may want to ignore Command Line output.
The program will inform you that it can't collect the data with OpenTelemetry. To remove that you can comment the get_current_label() line in main.py

To run the data collector, check out the official DFF User Guide on Supersets:
https://deeppavlov.github.io/dialog_flow_framework/user_guides/superset_guide.html
