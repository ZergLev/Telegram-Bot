import script
import happy_path
# Importing the bot's script and the test path.
# They are in separate files to not clutter the main file.

from dff.messengers.telegram import PollingTelegramInterface
from dff.pipeline import Pipeline
from dff.utils.testing.common import (
    is_interactive_mode,
    check_happy_path,
)

interface = PollingTelegramInterface("6906350021:AAGomOZF6ZtxcZUAoxG60k83zL0hOISyWqM")
# Note: token is exposed, only safety present is that the
# repo on github is set to private.

pipeline = Pipeline.from_script(
    script=script.script,
    # Taking the script from the script.py file.
    start_label=("global_flow", "start_node"),
    fallback_label=("global_flow", "fallback_node"),
    messenger_interface=interface,
)
# Note: Maybe the pipeline also deserves it's own file,
# but it's not that large right now


def main():
    pipeline.run()


if __name__ == "__main__" and is_interactive_mode():
    check_happy_path(pipeline, happy_path.happy_path)
    # Checking the happy_path to see if everything works as intended.
    # Comment that line to remove output or stop testing.
    main()
    # Main function of the file.
