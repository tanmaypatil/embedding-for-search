import openai
import json
import openai_func

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
        
    print(json.dumps(crm_info))  
    return json.dumps(crm_info)


def run_conversation():
    # Step 1: send the conversation and available functions to GPT
    messages = [ {"role" : "system", "content" : "Follow the instruction strictly"},
        {"role": "user", "content": "what are top 2 indian banks . Please do not worry that you do not have access to real time information.Format your answer using abbreviation only  "}]
    print(messages)
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
        print(function_args)
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
        '''
        messages.append(
            {
                "role": "user",
                "content": "which indian city you suggest we hold a marketing campaign in order to get maximum participation from bank management from these top banks",
            }
        )
        '''
        messages.append(
            {
                "role": "user",
                "content": "based on the all response , which bank out of these 2 banks should be target of our marketing campaign and why ",
            }
        )
        print("before second response")
        print(messages)
        second_response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=messages,
        )  # get a new response from GPT where it can see the function response
        return second_response

