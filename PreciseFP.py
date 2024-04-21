import requests

infile = open("Bearer.txt", "r")
Bearer = infile.read()
infile.close()

# test_url = 'https://app.precisefp.com/api/v3/form-engagements?sort=-created_at&limit=200&offset=0&account_id=33291'

data = {}
headers = {
    'Accept': 'application/json',
    'Authorization': Bearer
}
# active = True
def get_client():
    """
    Get the client's account ID by searching for their email address
    """
    trying = True
    while trying:
        try:
            input_client = input('Enter client email: ')
            list_client = list(input_client)
            for char in list_client:
                if char == '@':
                    char = '%40'
            str_client = ''.join(list_client)
            url = 'https://app.precisefp.com/api/v3/accounts?sort=-id&limit=50&offset=0&query='+str_client
            get_accounts = requests.get(url, data=data, headers=headers).json()
            return(get_accounts['items'][0]['id'])
            trying = False
        except:
            print('Email address not found')
            again = input('Try again? Y/N: ')
            if again == 'Y':
                trying = True
            else:
                trying = False

def get_engagements():
    """
    Using the account ID find available engagements
    """
    account_id = str(get_client())
    url = 'https://app.precisefp.com/api/v3/form-engagements?sort=-created_at&limit=200&offset=0&account_id='+account_id
    get_engage = requests.get(url, data=data, headers=headers).json()
    print('We found the following engagements:')
    count = 1
    items = get_engage['items']
    for engagement in items:
        if type(engagement['completed_at']) == str:
            print(str(count)+'. "'+engagement['title']+'" which was completed on '+engagement['completed_at'])
        else:
            print(str(count) + '. "' + engagement['title'])
        count += 1
    return items

def choose_engagement():
    """
    Offer the option of engagements to the user
    """
    items = get_engagements()
    chosen = False
    while chosen == False:
        try:
            choice = int(input('Enter the number you would like: '))
            if choice >0 and choice <= len(items):
                return(items[choice-1]['id'])
                chosen = True
            else:
                print('Please choose a valid number')
        except:
            print('Please enter one number only')

def get_engagement_data():
    """
    Once selected, load the engagement data
    """
    engage_id = choose_engagement()
    close = 'https://app.precisefp.com/api/v3/form-engagements/'+engage_id+'/close'
    requests.post(close, data=data, headers=headers).json() #Ensures the engagement is closed, which is a requirement to get the data
    url = 'https://app.precisefp.com/api/v3/form-engagements/'+engage_id+'/data'
    get_data = requests.get(url, data=data, headers=headers).json() #Gets the engagement data
    return(get_data)
    # cont = input('Do you want to find another client? Y/N: ')
    # return(cont)

# get_engagement_data()

# while active:
#     cont = get_engagement_data()
#     def re_run(cont):
#         if cont == 'Y':
#             get_engagement_data()
#         elif cont == 'N':
#             active = False
#             return(active)
#         else:
#             print('Please enter Y or N')
#             cont = input('Do you want to find another client? Y/N: ')
#             re_run(cont)
#
#     re_run(cont)
# get_test = requests.get(test_url, data=data, headers=headers).json()
#
# print(get_test)