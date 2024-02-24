import os
# Used for taking telegram bot token as an environment variable
from core import script, happy_path
# Importing the bot's script and the test path.
# They are in separate files to not clutter the main file.

from dff.messengers.telegram import PollingTelegramInterface
from dff.pipeline import Pipeline, Service, ACTOR
from dff.stats import (
    OtelInstrumentor,
    default_extractors,
)
from dff.utils.testing.common import (
    is_interactive_mode,
    check_happy_path,
)

dff_instrumentor = OtelInstrumentor.from_url("grpc://localhost:4317", insecure=True)
dff_instrumentor.instrument()

interface = PollingTelegramInterface(token=os.environ["TG_BOT_TOKEN"])
# Note: token is exposed in .env file, there is no safety present.
# To-do: Docker Secrets

pipeline = Pipeline.from_dict(
    {
        "script": script.script,
        # Taking the script from the script.py file.
        "start_label": ("global_flow", "start_node"),
        "fallback_label": ("global_flow", "fallback_node"),
        "messenger_interface": interface,
        "components": [
                    Service(
                        handler=ACTOR,
                        after_handler=[
                            default_extractors.get_current_label,
                            default_extractors.get_last_request,
                        ],
                    ),
        ],
    }
)
# Note: Maybe the pipeline also deserves its own file,
# but it's not that large right now


def main():
    pipeline.run()


if __name__ == "__main__" and is_interactive_mode():
    check_happy_path(pipeline, happy_path.happy_path)
    # Checking the happy_path to see if everything works as intended.
    # Comment that line to remove output or stop testing.
    main()
    # Main function of the file.
