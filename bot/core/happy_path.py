from dff.script import Message

happy_path = (
    (Message(text="/start"), Message(text="Hello! How are you today?")),
    (Message(text="Hi"), Message(text="Hello! How are you today?")),
    (Message(text="Bye"), Message(text="Ok, goodbye.")),
    (Message(text="Hello"), Message(text="Hello! How are you today?")),
    (
        Message(text="Good, how are you?"),
        Message(text="I'm doing well. What do you want to talk about? "
                     "I know some sports trivia and I love food.")
    ),
    (
        Message(text="Let's talk about chess."),
        Message(text="Sorry, I don't know much about that topic."
                     " Is there any other topic you would talk about?")
    ),
    (
        Message(text="I love food too. Let's talk about that."),
        Message(text="Would you like to hear some facts about food?")
    ),
    (
        Message(text="no"),
        Message(text="Well then. Is there anything else you'd like?")
    ),
    (Message(text="no"), Message(text="Ok, goodbye.")),
    (
        Message(text="Wait, let's talk sports."),
        Message(text="Would you like to hear some facts about sports?")
    ),
    (
        Message(text="Yes."),
        Message(text="Olympic gold medals are 93% silver, six percent copper "
                     "and 1 percent gold for the finish.")
    ),
    (
        Message(text="next"),
        Message(text="Tennis pro Maria Sharapova's grunt "
                     "is louder than an aircraft.")
    ),
    (
        Message(text="Okay, that's enough facts for now."),
        Message(text="Well then. Is there anything else you'd like?")
    ),
    (
        Message(text="I don't know."),
        Message(text="Oops, sorry. Didn't understand what you were saying.")
    ),
    (
        Message(text="Go back."),
        Message(text="Well then. Is there anything else you'd like?")
    ),
    (Message(text="no"), Message(text="Ok, goodbye.")),
)
