from dff.script import Context
from dff.pipeline import Pipeline


def is_topic_sports(ctx: Context, _: Pipeline, *args, **kwargs):
    request = ctx.last_request
    keywords = ["sports", "trivia"]
    for word in keywords:
        if word in request.text.lower():
            return True
    return False
# If any keyword found in request, bot assumes that "sports" is the topic.


def is_topic_food(ctx: Context, _: Pipeline, *args, **kwargs):
    request = ctx.last_request
    return "food" in request.text.lower()
# If "food" is said in the request, bot assumes that it's the topic.


def user_wants_to_talk(ctx: Context, _: Pipeline, *args, **kwargs):
    request = ctx.last_request
    return "talk about something" in request.text.lower()
# If user only asks to "talk about something" instead of some particular topic
# the bot recognizes that instead of just saying that it doesn't
# know much about that topic.
# This function is used only internally for now


def asked_how_bot_is_doing(ctx: Context, _: Pipeline, *args, **kwargs):
    request = ctx.last_request
    return "how are you" in request.text.lower()
# Returns True if the user asked the bot how it's doing in the last request.


def topic_unknown(ctx: Context, _: Pipeline, *args, **kwargs):
    request = ctx.last_request
    if "talk about" in request.text.lower():
        if not is_topic_sports(ctx, _) and not is_topic_food(ctx, _) and\
                not user_wants_to_talk(ctx, _):
            return True
            # User asked about some unknown topic.
    return False
    # User asked about something else.


"""def check_request_for_topics(topics: list[str]):
    def internal_func(ctx: Context, _: Pipeline, *args, **kwargs) -> bool:
        request = ctx.last_request
        for topic in topics:
            if topic.lower() in request.text.lower():
                return True
        return False
    return internal_func
# Checks the request for all the topics in the given list, ignores case.
# Could be easily done with 'conditions()' from dff.script, especially cnd.any(),
# but, if I recall correctly, in the tutorials conditions() are
# only used in the TRANSITIONS{}, so I thought maybe they're not supposed
# to be used outside that."""

# Function unused. It's kept here in case I need it for later use.
# It doesn't need to be nested, but the tutorials do this,
# and I could change it later.
