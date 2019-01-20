import random

bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"],
    
  "question": ["I don't know :(", 'you tell me!'],
    
 "statement": ['tell me more!',
      'why do you think that?',
      'how long have you felt this way?',
      'I find that extremely interesting',
      'can you back that up?',
      'oh wow!',
      ':)'
    ]
}

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = random.choice(responses[message])
    elif message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    else:
        # Return the "default" message
        bot_message = random.choice(responses["statement"]) #["default"]
    return bot_message

def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))
    
#send_message("what's today's weather?")
send_message("what's your name?")
#send_message("what's your favorite color?")
