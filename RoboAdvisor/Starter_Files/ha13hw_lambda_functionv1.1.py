### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta

### Functionality Helper Functions ###
def parse_int(n):
    """
    Securely converts a non-integer value to integer.
    """
    try:
        return int(n)
    except ValueError:
        return float("nan")

def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except ValueError:
        return float("nan")

""" ha functions"""
def validate_data(age, investment_amount, intent_request):
    """
    Validates the data provided by the user.
    """

    # Validate that the user is over 21 years old
    if age is not None:
        """ ha change this"""
        ### ha tod do change this to age to integer
        # delete birth_date = datetime.strptime(birthday, "%Y-%m-%d")
        # delete age = relativedelta(datetime.now(), birth_date).years
        int_age = parse_int(age) 
        if int_age < 0 or int_age > 65 :
            return build_validation_result(
                False,
                "age",
                "Your age should be > 0 and < 66"
                "please give an age in an age in this range",
            )

    # Validate the investment amount, it should be > 0
    if investment_amount is not None:
        investment_amount = parse_float(
            investment_amount
        )  # Since parameters are strings it's important to cast values
        if investment_amount <= 5000:
            return build_validation_result(
                False,
                "usdAmount",
                "You need to have atleast 5000 for invesntment"
                "please proivde a number > 5000",
            )

    # A True results is returned if age or amount are valid
    return build_validation_result(True, None, None)

def create_recommendation(in_risk_level):
    
    switch (in_risk_level){
        case 'none': return  "100% bonds (AGG), 0% equities (SPY);
        case 'low': return  "60% bonds (AGG), 40% equities (SPY)";
        case 'medium': return "40% bonds (AGG), 60% equities (SPY)";
        case 'high': return "20% bonds (AGG), 80% equities (SPY)";
        default: return 'no recommendation';
    }
    
    return init_recommendation

""" hassans routines end here"""



"""pre proivided functions here """
def build_validation_result(is_valid, violated_slot, message_content):
    """
    Define a result message structured as Lex response.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def recommend_portfolio(intent_request):
    """
    Performs dialog management and fulfillment for recommending a portfolio.
    """

    first_name = get_slots(intent_request)["firstName"]
    age = get_slots(intent_request)["age"]
    investment_amount = get_slots(intent_request)["investmentAmount"]
    risk_level = get_slots(intent_request)["riskLevel"]
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # Perform basic validation on the supplied input slots.
        # Use the elicitSlot dialog action to re-prompt
        # for the first violation detected.
        #ha code get all the slots
        #ha - is this necessary since everything is laready returned
        slots = get_slots(intent_request)

        ### YOUR DATA VALIDATION CODE STARTS HERE ###
        # ha code
        # vakudatem if not valid clear slot and ask for info
        validation_result = validate_data(age, investment_amount, intent_request)
        
        
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None 
            
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )
        
        ### YOUR DATA VALIDATION CODE ENDS HERE ###

        # Fetch current session attibutes
        output_session_attributes = intent_request["sessionAttributes"]

        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the initial investment recommendation

    ### YOUR FINAL INVESTMENT RECOMMENDATION CODE STARTS HERE ###
    initial_recommendation = create_recommendation(risk_level)
    ### YOUR FINAL INVESTMENT RECOMMENDATION CODE ENDS HERE ###

    # Return a message with the initial recommendation based on the risk level.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """{} thank you for your information;
            based on the risk level you defined, my recommendation is to choose an investment portfolio with {}
            """.format(
                first_name, initial_recommendation
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "RecommendPortfolio":
        return recommend_portfolio(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
