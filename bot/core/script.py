from . import responses
# Used to generate a custom response at ("greeting_flow", "request_topic")
from . import conditions as custom_cond
# Used for checking for topics in the user request

import re
from dff.script import conditions as cnd
from dff.script import labels as lbl
from dff.script import (
    GLOBAL,
    LOCAL,
    TRANSITIONS,
    RESPONSE,
    Message,
)

script = {
    GLOBAL: {
        TRANSITIONS: {
            lbl.forward(): cnd.all(
                [
                    cnd.regexp(r"\b(next)\b", re.I),
                    cnd.any(
                        [
                            cnd.has_last_labels(
                                labels=[("sports_flow", node) for node
                                        in ["ask_node", "fact1_node", "fact2_node"]]),
                            cnd.has_last_labels(
                                labels=[("food_flow", node) for node
                                        in ["ask_node", "fact1_node", "fact2_node"]]),
                        ],
                    ),
                ],
            ),
            # Going to the next node on user's request if possible.
            # In both flows "fact3_node" has it's own reaction for "next".
            # Note: Applicable now, could pose a problem if nodes
            # are reordered in any way later.

            lbl.repeat(): cnd.regexp(r"repeat", re.I),
            # Repeating the node's RESPONSE on user's request.
            # Note: In case the node increases in functionality, it will all be repeated too.

            ("greeting_flow", "greeting_node"):
                cnd.regexp(r"\b(restart|hello|hi|hey there)\b", re.I),
            # Going back to the start of the script and greeting the user.

            ("greeting_flow", "goodbye_node"):
                cnd.regexp(r"(bye|next time|see you)", re.I),
            # Saying goodbye to the user if there is nothing more to talk
            # about or if they say goodbye first.

            ("sports_flow", "ask_node"): custom_cond.is_topic_sports,
            ("food_flow", "ask_node"): custom_cond.is_topic_food,
            ("greeting_flow", "request_topic_node"): cnd.regexp(r"talk about", re.I),
            # Trying to determine if the user wants to talk about something,
            # then sending them where they want.
            # Could be done better by putting the topics in a list somewhere.
        },
    },
    "global_flow": {
        "start_node": {
            RESPONSE: Message(text="Please, type /start to start talking."),
            TRANSITIONS: {
                ("greeting_flow", "greeting_node"): cnd.exact_match(Message(text="/start")),
            },
        },
        # Starting the bot-user interaction.

        "fallback_node": {
            RESPONSE: Message(text="Oops, sorry. Didn't understand what you were saying."),
            TRANSITIONS: {
                lbl.previous(): cnd.regexp(r"(previous|go back)", re.I),
                # Going back to the previous node on user's request.
            },
        },
    },
    "greeting_flow": {
        "greeting_node": {
            RESPONSE: Message(text="Hello! How are you today?"),
            TRANSITIONS: {
                ("greeting_flow", "request_topic_node", 0.5): cnd.true(),
                # This transition moves the conversation forward, whatever the user replies
            },
        },
        # Naming nodes randomly, since I don't know the relevant standards.
        # But I figure that giving unique names is good,
        # since node numbers and order could change in the future.

        "request_topic_node": {
            RESPONSE: responses.ask_for_topic_custom_response,
            TRANSITIONS: {
                "no_requests_node": cnd.regexp(r"(nothing|I don't know)", re.I),
                ("sports_flow", "ask_node"): cnd.regexp(r"anything", re.I),
            },
        },
        # If the user doesn't know what to talk about the bot will suggest sports
        # Most TRANSITIONS from this node are in the GLOBAL node.

        "no_requests_node": {
            RESPONSE: Message(text="Well then. Is there anything else you'd like?"),
            TRANSITIONS: {
                "goodbye_node": cnd.regexp(r"\b(no)\b", re.I),
            },
        },
        # The user gets here, if he stops interacting with the 'topic' flows.
        # For now this node only knows how to react to a "No".
        # Note: this node could allow the user to do something else
        # rather than just talk, e.g. upload a picture from the internet.

        "goodbye_node": {
            RESPONSE: Message(text="Ok, goodbye."),
        },
        # If the user wants to talk further, they can say "hi" or something else.
    },
    "sports_flow": {
        LOCAL: {
            TRANSITIONS: {
                ("greeting_flow", "no_requests_node"):
                    cnd.regexp(r"\b(stop|enough)\b", re.I),
            },
        },
        # Using LOCAL since it's only appropriate in the main topics.

        "ask_node": {
            RESPONSE: Message(text="Would you like to hear some facts about sports?"),
            TRANSITIONS: {
                "fact1_node": cnd.regexp(r"\b(yes|ok|alright|sure)\b", re.I),
                ("greeting_flow", "no_requests_node"): cnd.regexp(r"\b(no)\b", re.I),
            },
        },
        # Start of the sports flow.

        "fact1_node": {
            RESPONSE: Message(text="Olympic gold medals are 93% silver, six percent copper "
                                   "and 1 percent gold for the finish."),
        },
        "fact2_node": {
            RESPONSE: Message(text="Tennis pro Maria Sharapova's grunt "
                                   "is louder than an aircraft."),
        },
        "fact3_node": {
            RESPONSE: Message(text="The name for three consecutive strikes in bowling"
                                   " is called a turkey."),
            TRANSITIONS: {
                ("greeting_flow", "no_requests_node"): cnd.regexp(r"\b(next)\b", re.I),
            },
        },
    },
    "food_flow": {
        LOCAL: {
            TRANSITIONS: {
                ("greeting_flow", "no_requests_node"):
                    cnd.regexp(r"\b(stop|enough)\b", re.I),
            },
        },

        "ask_node": {
            RESPONSE: Message(text="Would you like to hear some facts about food?"),
            TRANSITIONS: {
                "fact1_node": cnd.regexp(r"\b(yes|ok|alright|sure)\b", re.I),
                ("greeting_flow", "no_requests_node"): cnd.regexp(r"\b(no)\b", re.I),
            },
        },
        # Start of the cooking flow.

        "fact1_node": {
            RESPONSE: Message(text="Caesar salad isn't from anywhere near Italy."
                                   "The Caesar salad was actually invented by a hotel owner Caesar Cardini"
                                   " in Tijuana, Mexico back in 1927. To be fair, "
                                   "Cardini himself was actually born in Italy"),
        },
        "fact2_node": {
            RESPONSE: Message(text="Coriander may taste like soap to you because of your genes."),
        },
        "fact3_node": {
            RESPONSE: Message(text="Lemons float — but limes sink. It all comes down to density:"
                                   " limes are slightly denser than lemons."),
            TRANSITIONS: {
                ("greeting_flow", "no_requests_node"): cnd.regexp(r"\b(next)\b", re.I),
            },
        },
    },
}
