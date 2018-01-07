"""
nvias - Program for creators - Talk to Alexa
Alexa skills - Funny Storry Maker
nvias.org
"""

from __future__ import print_function
import random

# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, content, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': output
        },
        'card': {
            'type': 'Standard',
            'title': "Funny Storry Maker - " + title,
            'content': content,
            'text': content,
            "image": {
                "smallImageUrl": "https://s3-eu-west-1.amazonaws.com/alexanvias/pic/Funny+story+maker+-+720x480.jpg",
                "largeImageUrl": "https://s3-eu-west-1.amazonaws.com/alexanvias/pic/Funny+story+maker+-+1200X800.jpg"
            }
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def set_magic_word():
    # random magic word
    # speechcon - dun dun dun, bada bing bada boom, voila, mamma mia, gotcha, abracadabra

    i = random.randint(1,10)
    if i == 1:
        speechcon = "<say-as interpret-as=\"interjection\">dun dun dun</say-as>"
    elif i == 2:
        speechcon = "<say-as interpret-as=\"interjection\">bada bing bada boom</say-as>"
    elif i == 4:
        speechcon = "<say-as interpret-as=\"interjection\">voila</say-as>"
    elif i == 5:
        speechcon = "<say-as interpret-as=\"interjection\">mamma mia</say-as>"
    elif i == 6:
        speechcon = "<say-as interpret-as=\"interjection\">abracadabra</say-as>"
    elif i == 7:
        speechcon = "<say-as interpret-as=\"interjection\">gotcha</say-as>"
    elif i == 8:
        speechcon = "<say-as interpret-as=\"interjection\">dum dum</say-as>,<say-as interpret-as=\"interjection\">dun dun</say-as>"
    elif i == 9:
        speechcon = "<say-as interpret-as=\"interjection\">dum dum</say-as>,<say-as interpret-as=\"interjection\">dun dun dun</say-as>"
    else:
        speechcon = "<say-as interpret-as=\"interjection\">ahem</say-as>. Surprise!"

    return speechcon

def set_color_animal(v_color, v_animal):
    # define new animal based on color    
    switcher = { 
        "pink": "pig",
        "green": "frog",
        "brown": "horse",
        "white": "polar bear",
        "yellow": "giraffe",
        "blue": "hipo",
        "orange": "tiger",
        "black": "penguin",
        "purple": "parrot",
        "gold": "jaguar",
        "gray": "koala",
        "silver": "fish",
        "red": "butterfly"
    }
    def_response = v_color + " " + v_animal
    
    return switcher.get(v_color, def_response)


def set_animal_voice(v_animal):
    # select the vioce effect for the animal
    switcher = {    
        'bird': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/bird.mp3\" />',
        'cat': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/cat.mp3\" />',
        'crocodile': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/crocodile.mp3\" />',
        'dog': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/dog.mp3\" />',
        'donkey': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/donkey.mp3\" />',
        'fish': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/fish.mp3\" />',
        'goat': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/goat.mp3\" />',
        'horse': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/horse.mp3\" />',
        'chicken': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/chicken.mp3\" />',
        'lion': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/lion.mp3\" />',
        'parrot': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/parrot.mp3\" />',
        'pig': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/pig.mp3\" />',
        'sheep': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/sheep.mp3\" />',
        'snake': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/snake.mp3\" />',
        'tiger': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/tiger.mp3\" />',
        'wolf': '<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/wolf.mp3\" />',
        'rooster': '<break/><say-as interpret-as=\"interjection\">cock a doodle doo</say-as><break/>',
        'cow': '<break/><say-as interpret-as=\"interjection\">moo</say-as><break/>'
    }
        
    i = random.randint(1,10)
    if i == 1:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/sheep.mp3\" />"
    elif i == 2:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/bird.mp3\" />"
    elif i == 3:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/lion.mp3\" />"
    elif i == 4:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/tiger.mp3\" />"
    elif i == 5:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/pig.mp3\" />"
    elif i == 6:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/parrot.mp3\" />"
    elif i == 7:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/chicken.mp3\" />"
    elif i == 8:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/goat.mp3\" />"
    elif i == 9:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/horse.mp3\" />"
    elif i == 10:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/donkey.mp3\" />"
    else:
        defaul_animal_voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/donkey.mp3\" />"

    def_response = defaul_animal_voice + " ouh, wait a moment <break/> was it realy a " + v_animal + "?" \
                   " <break time=\"1s\"/> <break/> Anyway, the " + v_animal
                   
    return switcher.get(v_animal, def_response)    

def get_welcome_voice(v_person):
    # defene a welcome message for a person

    i = random.randint(1,10)
    if i == 1:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/bonjorno.mp3\" />"
    elif i == 2:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/bonjour.mp3\" />"
    elif i == 3:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/gutten_tag.mp3\" />"
    elif i == 4:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/hello_a.mp3\" />"
    elif i == 5:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/hello_d.mp3\" />"
    elif i == 6:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/hello_k.mp3\" />"
    elif i == 7:
        voice = "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/hello_lr.mp3\" />"
    elif i == 8:
        voice = "<break/>Hi<break time=\"1s\"/>"
    else:
        voice = '<break/><say-as interpret-as=\"interjection\">aloha</say-as><break/>'

    return voice    

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = "Welcome"
    should_end_session = False
    
    # welcome_speechcon 
    i = random.randint(1,10)
    if i == 1:
        welcome_speechcon = "<say-as interpret-as=\"interjection\">hurray</say-as>"
    elif i == 2:
        welcome_speechcon = "<say-as interpret-as=\"interjection\">boing</say-as>"
    elif i == 4:
        welcome_speechcon = "<say-as interpret-as=\"interjection\">achoo</say-as>, <break time=\"700ms\" /> I'm sorry <break time=\"300ms\" />"
    elif i == 5:
        welcome_speechcon = "<say-as interpret-as=\"interjection\">cheerio</say-as>"
    else:
        welcome_speechcon = ""

    
    speech_output = "<speak>Welcome to Funny Story maker! <break/>" + welcome_speechcon + \
                    ". Just pick one Animal, one Color, one Person and one Room  " \
                    " and I will made-up a funny story for you!</speak>"
    content_output = "Welcome to Funny Story maker." \
                    "Just pick one Animal, one Color, one Person and one Room  " \
                    " and Alexa will made-up a funny story for you."
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "You can say I pick Dog as an Animal, Ping as a Color, " \
                    " Batman as a Person and Kitchen as a Room."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, content_output, reprompt_text, should_end_session))


def get_selection_session(intent, session):
    """ Sets the attributes of the story in the session and prepares the speech to reply to the user.
    """

    card_title = "Your story is being prepared ..."
    should_end_session = False
    reprompt_text = ""
    speech_output = ""
    content_output = "I'm preparing story about "
    session_attributes = {}
    v_animal = "no animal"
    v_color = "no color"
    v_person = "no person"
    v_room = "no room"

    if session.get('attributes', {}):
        if "Animal" in session.get('attributes', {}):
            v_animal = session['attributes']['Animal']
        if "Color" in session.get('attributes', {}):
            v_color = session['attributes']['Color']
        if "Person" in session.get('attributes', {}):
            v_person = session['attributes']['Person']
        if "Room" in session.get('attributes', {}):
            v_room = session['attributes']['Room']
    
    if 'slots' in intent:
        if 'Animal' in intent['slots'] and 'value' in intent['slots']['Animal']:
            v_animal = intent['slots']['Animal']['value']
        if 'Color' in intent['slots'] and 'value' in intent['slots']['Color']:
            v_color = intent['slots']['Color']['value']
        if 'Person' in intent['slots'] and 'value' in intent['slots']['Person']:
            v_person = intent['slots']['Person']['value']
        if 'Room' in intent['slots'] and 'value' in intent['slots']['Room']:
            v_room = intent['slots']['Room']['value']


    if v_animal == "no animal":
        speech_output = "<speak>What is your animal?</speak>"
        reprompt_text = "You can say, I pick Dog as a Animal."
        content_output = content_output + " ... the choice is up tu you. "
    else:
        content_output = content_output + " " + v_animal
        if v_color == "no color":
            speech_output = "<speak>Which color will you pick?</speak>"
            reprompt_text = "You can say, I like blue color."
        else:
            content_output = content_output + ", " + v_color + " color"
            if v_person == "no person":
                speech_output = "<speak>Please, pick some person for your story.</speak>"
                reprompt_text = "Just say, My favorite person is Superman!"
            else:
                content_output = content_output + " and " + v_person 
                if v_room == "no room":
                    speech_output = "<speak>And now we need a room.</speak>"
                    reprompt_text = "I select Living room as a room."
                        

    if v_animal != "no animal" and v_color != "no color" and v_person != "no person" and v_room != "no room":
        animal_voice = set_animal_voice(v_animal)
        color_animal = set_color_animal(v_color, v_animal)
        welcome_voice = get_welcome_voice(v_person)
        card_title =  "Now enjoy your story"
        magic_word = set_magic_word()
        content_output = "Enjoy your story about " + " " + v_animal + " and " + v_person + "."
        speech_output = "<speak><prosody rate=\"slow\"> One day a little " + v_animal + animal_voice + " went to his friend " \
                        + v_person + ". <say-as interpret-as=\"interjection\">ding dong</say-as><break time=\"1s\" />" + welcome_voice + \
                        " After the warm welcome, little " + v_animal + " told to " + v_person + ". I dont want to be " \
                        + v_animal + " anymore! So go to the " + v_room + \
                        ". Said " + v_person + ". When the " + v_animal +  " open the door, " \
                        "<audio src=\"https://s3-eu-west-1.amazonaws.com/alexanvias/sound_effects/Falling+color+can.mp3\" /> " \
                        "a can with " + v_color + " color " \
                        " pour out on him. " + magic_word + ". Said " + v_person + \
                        ". Now you are " + color_animal + "<audio src=\"https://s3.amazonaws.com/sounds226/boom.mp3\" /></prosody>" \
                        "<break time=\"2s\" /><say-as interpret-as=\"interjection\">well done</say-as>. Do you want to repeat " \
                        "the story, create new one or just change some characters? </speak>"
        reprompt_text = "Should I repeat the story, create new one or change some characters? " \
                        " You can finish the story maker by saying no, and return later. "
                        
    else:
        if v_animal == "no animal" and v_color == "no color" and v_person == "no person" and v_room == "no room":
           speech_output = "<speak>I'm not sure what is your selection. " \
                           " Say quickly one after another <break/> animal, color, " \
                           " person and room. <break/> Or say I select Cow as an animal, and so on .</speak>"
           content_output = "You can say I pick Dog as a Animal, Ping as a Color, " \
                           " Batman as a Person and Kitchen as a Room. "
           reprompt_text = "You can say I pick Dog as a Animal, Ping as a Color, " \
                           " Batman as a Person and Kitchen as a Room. "

    # write new sessions attributes
    session_attributes["Animal"] = v_animal
    session_attributes["Color"] = v_color
    session_attributes["Person"] =  v_person
    session_attributes["Room"] = v_room

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, content_output, reprompt_text, should_end_session))


def get_help_response():
    """ The help session - don't leave the kids without help :-)
    """
    session_attributes = {}
    should_end_session = False
    card_title = "Help"

    speech_output = "<speak><say-as interpret-as=\"interjection\">okey</say-as>, To build a funny story for you <break/>" \
                    "I need you to name one Animal, one Color, one Person and one Room.  " \
                    " If you are lost just wait few seconds and I'll give you a hint. " \
                    " You can even say quickly lot of nonsense and let's see what I can do!" \
                    " You can also change a characters by saying, change room to toilet, for example.</speak>"
    content_output = "To build a funny story for you " \
                    "I need you to name one Animal, one Color, one Person and one Room.  " \
                    " If you are lost just wait few seconds and I'll give you a hint. " \
                    " You can even say quickly lot of nonsense and let's see what I can do!" \
                    " You can also change a characters by saying change room to toilet, for example."
    reprompt_text = "You can say I pick Dog as an Animal, Ping as a Color, " \
                    " Batman as a Person and Kitchen as a Room."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, content_output, reprompt_text, should_end_session))


def dont_know_response(intent, session):
    """  
    If the user don't know the answer. Prepares the speech to reply to the user.
    """
    card_title = "You don't know"
    session_attributes = {}
    should_end_session = False

    speech_output = "<speak><say-as interpret-as=\"interjection\">oups</say-as>," \
                    " I think you don't know. Nevermind. You can say, " \
                    " I pick Dog as a Animal, Ping as a Color, " \
                    " Batman as a Person and Kitchen as a Room. </speak>"
    content_output = "Ohh, I think you don't know. Nevermind. You can say " \
                    " I pick Dog as a Animal, Ping as a Color, " \
                    " Batman as a Person and Kitchen as a Room."
    reprompt_text = "You can say I pick Dog as an Animal, Ping as a Color, " \
                    " Batman as a Person and Kitchen as a Room."
 
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, content_output, reprompt_text, should_end_session))
 
def new_response(intent, session):
    """  
    If the user don't know the answer. Prepares the speech to reply to the user.
    """
    card_title = "Create new funny story"
    session_attributes = {}
    should_end_session = False

    i = random.randint(1,3)
    if i == 1:
        speechcon = "<say-as interpret-as=\"interjection\">okey dokey</say-as>, the new story begin "
    elif i == 2:
        speechcon = "<say-as interpret-as=\"interjection\">encore</say-as>"
    else:
        speechcon = "Let's create brand new funny story! "

    speech_output = "<speak>" + speechcon + "," \
                    " Once again, " \
                    " Name one animal, color, person and room. </speak>"
    content_output = "Let's create brand new funny story. Once again, " \
                    " Name one animal, color, person and room."
    reprompt_text = "Let's create brand new funny story. Once again, " \
                    " Name one animal, color, person and room."

    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, content_output, reprompt_text, should_end_session))

        
def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "<speak>Thank you for your time with Funny Story. " \
                    " I hope you came back soon to make new Funny Story." \
                    " Have a nice day!</speak>"
    content_output = "Thank you for your time with Funny Story. " \
                    " I hope you came back soon to make new Funny Story." \
                    " Have a nice day!"
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, content_output, None, should_end_session))



# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "Selection":
        return get_selection_session(intent, session)
    elif intent_name == "IAnimal":
        return get_selection_session(intent, session)
    elif intent_name == "IColor":
        return get_selection_session(intent, session)
    elif intent_name == "IPerson":
        return get_selection_session(intent, session)
    elif intent_name == "IRoom":
        return get_selection_session(intent, session)
    elif intent_name == "RepeatStory":
        print("RepeatStory ", intent, session)
        return get_selection_session(intent, session)
    elif intent_name == "New":
        return new_response(intent, session)
    elif intent_name == "DontKnow":
        return dont_know_response(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_help_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.
    
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

