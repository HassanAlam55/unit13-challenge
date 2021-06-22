# debug intent with variables changed to strings in line debu
intent1 = {
  "currentIntent": {
    "name": "RecommendPortfolio",
    "nluIntentConfidenceScore": 'score',  #debug 
    "slots": {
      "firstName": "Name",
      "age": 55,
       "investmentAmount": 10000,
        "riskLevel": 'low'
    },
    "slotDetails": {
      "slot1": {
        "resolutions" : [
          { "value": "resolved value" },
          { "value": "resolved value" }
        ],
        "originalValue": "original text"
      },
      "slot2": {
        "resolutions" : [
          { "value": "resolved value" },
          { "value": "resolved value" }
        ],
        "originalValue": "original text"
      }
    },
    "confirmationStatus": "None, Confirmed, or Denied (intent confirmation, if configured)"
  },
  "alternativeIntents": [
    {
      "name": "intent-name",
      "nluIntentConfidenceScore": 'score', #taken out for debug
      "slots": {
        "slot name": "value",
        "slot name": "value"
      },
      "slotDetails": {
        "slot name": {
          "resolutions" : [
            { "value": "resolved value" },
            { "value": "resolved value" }
          ],
          "originalValue": "original text"
        },
        "slot name": {
          "resolutions" : [
            { "value": "resolved value" },
            { "value": "resolved value" }
          ],
          "originalValue": "original text"
        }
      },
      "confirmationStatus": "None, Confirmed, or Denied (intent confirmation, if configured)"
    }
  ],
  "bot": {
    "name": "bot name",
    "alias": "bot alias",
    "version": "bot version"
  },
  "userId": "User ID specified in the POST request to Amazon Lex.",
  "inputTranscript": "Text used to process the request",
  "invocationSource": "DialogCodeHook",
  "outputDialogMode": "Text or Voice, based on ContentType request header in runtime API request",
  "messageVersion": "1.0",
  "sessionAttributes": { 
     "key1": "value1",
     "key2": "value2"
  },
  "requestAttributes": { 
     "key": "value",
     "key": "value"
  },
  "recentIntentSummaryView": [
    {
        "intentName": "Name",
        "checkpointLabel": 'Label', # debug
        "slots": {
          "slot name": "value",
          "slot name": "value"
        },
        "confirmationStatus": "None, Confirmed, or Denied (intent confirmation, if configured)",
        "dialogActionType": "ElicitIntent, ElicitSlot, ConfirmIntent, Delegate, or Close",
        "fulfillmentState": "Fulfilled or Failed",
        "slotToElicit": "Next slot to elicit"
    }
  ],
   "sentimentResponse": { 
      "sentimentLabel": "sentiment",
      "sentimentScore": "score"
   },
   "kendraResponse": {
       'Complete query response from Amazon Kendra' #taken out for debugging
   },
   "activeContexts": [
        {
            "timeToLive": {
                "timeToLiveInSeconds": 'seconds', #debug
                "turnsToLive": 'turns' # debug
            },
            "name": "name",
            "parameters": {
                "key name": "value"
            }
        }
    ]
}