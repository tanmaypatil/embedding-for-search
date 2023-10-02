
import json
def get_old_sales_intelligence(bank_name):
    """returns the customers sales intelligence from CRM db"""
    info = {
        "ICICI" : {
            "is_customer" : "Yes",
            "sales_volume" : "10 million"
        },
        "SBI" : {
            "is_customer" : "Yes",
            "sales_volume" : "20 million"
            
        }
    }
    return info[bank_name]

def get_sales_intelligence(bank_array):
    """returns the customers sales intelligence from CRM db"""
    info = {
        "State Bank of India" : {
            "name" : "State Bank of India",
            "is_our_customer" : "No",
            "sales_volume" : ""
        },
        "HDFC Bank" : {
            "name" : "HDFC Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "5 million"
        },
        "Punjab National Bank" : {
            "name" :  "Punjab National Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "50 million"
        },
        "ICICI Bank" : {
            "name" : "ICICI Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "10 million"
        },
        "Axis Bank" : {
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

def get_sales_intelligence(bank_string : str):
    """returns the customers sales intelligence from CRM db"""
    bank_array = bank_string.split(',')
    info = {
        "State Bank of India" : {
            "name" : "State Bank of India",
            "is_our_customer" : "No",
            "sales_volume" : ""
        },
        "HDFC Bank" : {
            "name" : "HDFC Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "5 million"
        },
        "Punjab National Bank" : {
            "name" :  "Punjab National Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "50 million"
        },
        "ICICI Bank" : {
            "name" : "ICICI Bank",
            "is_our_customer" : "Yes",
            "sales_volume" : "10 million"
        },
        "Axis Bank" : {
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



x = get_sales_intelligence('Punjab National Bank,Axis Bank')

print(json.dumps(x))