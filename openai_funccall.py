import openai
import json
import print_test
from IPython.display import JSON

def get_sales_campaign_running(city_name:str,bank_name:str,detailed_reason:str):
    """returns the sales campaign which are currently happening in city"""
    campaigns = {
        "Mumbai" : 
        [
            {    
            "from_date" : "01-nov-2023",
            "to_date"   : "03-nov-2023",
            "description" : "cross border payments cheaper and faster",
            "sales_team_status" : "busy"
            } ,
            {
            "from_date" : "22-nov-2023",
            "to_date"   : "23-nov-2023",
            "description" : "blockchain payments at fingertips",
            "sales_team_status" : "busy"
            }
        ],
        "Bangalore" :  
        [
            {    
            "from_date" : "05-nov-2023",
            "to_date"   : "08-nov-2023",
            "description" : "syndicated loans and blockchain",
            "sales_team_status" : "busy"
            } ,
            {
            "from_date" : "25-nov-2023",
            "to_date"   : "27-nov-2023",
            "description" : "corporate liquidity management ",
             "sales_team_status" : "busy"
            }
        ]
    }
    campaign = campaigns[city_name]
    campaign_withinfo = {}
    campaign_withinfo ["bank_name"] = bank_name
    campaign_withinfo ["detailed_reason"] = detailed_reason
    campaign_withinfo ["campaign"] = campaign
    JSON(campaign, expanded=True)  
    return json.dumps(campaign_withinfo)


def get_sales_intelligence(bank_name1 : str,bank_name2 : str):
    """returns the customers sales intelligence from CRM db"""
    bank_array = []
    bank_array.append(bank_name1)
    bank_array.append(bank_name2)    
    info = {
        "SBI" : {
            "name" : "State Bank of India",
            "is_our_customer" : "No",
            "sales_volume" : ""
        },
        "HDFC" : {
            "name" : "HDFC Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "5 million"
        },
        "PNB" : {
            "name" :  "Punjab National Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "50 million"
        },
        "ICICI" : {
            "name" : "ICICI Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "10 million"
        },
        "AXIS" : {
            "name" : "Axis Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "20 million"  
        }
    }
    crm_info = []
    for bank in bank_array:
        obj = info[bank]
        crm_info.append(obj)
        
    
    JSON(crm_info, expanded=True)  
    return json.dumps(crm_info)


def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    messages = [ {"role" : "system", "content" : "Follow the instruction strictly"},
        {"role": "user", "content": "what are top 2 indian banks . Please do not worry that you do not have access to real time information.Format your answer using abbreviation only  "}]
    print_test.print_messages(messages)
    functions = [
        {
            "name": "get_sales_intelligence",
            "description": "Get the customer specific sales intelligence data from internal system",
            "parameters": {
                "type": "object",
                "properties": {
                    "bank_name1": {
                        "type": "string",
                        "description": "the names of the bank , example ICICI",
                    },
                    
                    "bank_name2": {
                        "type": "string",
                        "description": "the name of the second bank , example SBI",
                    }
                    
                },
                "required" : ["bank_name1","bank_name2"]

            },
        },
        {
            "name": "get_sales_campaign_running",
            "description": "Get the current sales campaign running will allow you to schedule future",
            "parameters": {
                "type": "object",
                "properties": {
                    "city_name": {
                        "type": "string",
                        "description": "the names of the city e.g Pune",
                    },
                       "bank_name": {
                        "type": "string",
                        "description": "the bank which is chosen",
                    },
                       "detailed_reason": {
                        "type": "string",
                        "description": "detailed reason for choosing bank over others",
                    },
                },
                "required" : ["city_name"]

            },
        }
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=messages,
        functions = functions,
        function_call = { "name": "get_sales_intelligence"}
    )
    print(response)
    response_message = response["choices"][0]["message"]
  

    # Step 2: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_sales_intelligence": get_sales_intelligence,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        JSON(function_args,expanded=True)
        function_response = function_to_call(
            bank_name1=function_args.get("bank_name1"),
            bank_name2=function_args.get("bank_name2")
        )
        print (f"final formatted response from sales intelligence{function_response}")
        # Step 4: send the info on the function call and function response to GPT
        messages.append(response_message)  # extend conversation with assistant's reply
        messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
        messages.append(
            {
                "role": "user",
                "content": "based on the all response , which bank out of these 2 banks should be target of our marketing campaign and why . Suggest a city where we can hold marketing campaign ",
            }
        )   
        print_test.print_messages(messages)
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
            functions = functions,
            function_call = { "name": "get_sales_campaign_running"}
        )  # get a new response from GPT where it can see the function response
        
        response_message = second_response["choices"][0]["message"]
  

    # Step 4: check if GPT wanted to call a function
    if response_message.get("function_call"):
        # Step 5: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_sales_campaign_running": get_sales_campaign_running,
        }  # only one function in this example, but you can have multiple
        function_name = response_message["function_call"]["name"]
        function_to_call = available_functions[function_name]
        function_args = json.loads(response_message["function_call"]["arguments"])
        JSON(function_args,expanded=True)
        function_response = function_to_call(
           city_name=function_args.get("city_name") ,
           bank_name=function_args.get("bank_name"),
           detailed_reason=function_args.get("detailed_reason")
           )
        print (f"final formatted response from sales campaign")
        json_object = json.loads(function_response)
        json_formatted_str = json.dumps(json_object, indent=2)
        event = "sales campaign"
        color_prefix =  '\033[31m' #RED
        print(f"{color_prefix}\n[{event}]\n{json_formatted_str}")
        
    messages.append(response_message)  # extend conversation with assistant's reply
    messages.append(
            {
                "role": "function",
                "name": function_name,
                "content": function_response,
            }
        )  # extend conversation with function response
    messages.append(
           {
            "role": "user",
             "content": "Display best suitable schedule for 2 days excluding current campaigns where sales team is not available , please exclude diwali holidays and weekend ",
           }
        )
  
    third_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages
        )
   
        
    return third_response

