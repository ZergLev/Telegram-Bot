from conditions import (
    asked_how_bot_is_doing,
    topic_unknown,
)
from dff.script import Context, Message
from dff.pipeline import Pipeline


def ask_for_topic_custom_response(ctx: Context, _: Pipeline, *args, **kwargs) -> Message:
    if topic_unknown(ctx, _):
        return Message(text="Sorry, I don't know much about that topic."
                            " Is there any other topic you would talk about?")
    # This function triggers in this node only, where we know for a fact,
    # that the user didn't choose a known topic like sports or food.
    # In case the user says "I want to talk about something",
    # the bot will account for that.

    if asked_how_bot_is_doing(ctx, _):
        return Message(text="I'm doing well. What do you want to talk about?"
                            " I know some sports trivia and I love food.")
    # If the user wants to know how the bot is doing, it will answer,
    # otherwise it won't.
    return Message(text="What do you want to talk about?"
                        " I know some sports trivia and I love food.")
    # If the user asked to talk about "something" and not a particular topic
    # this would be the answer.
