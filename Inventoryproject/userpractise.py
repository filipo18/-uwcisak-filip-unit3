# Create bank info

customer1 = {'FirstName': 'Filip', 'LastName': 'Keitaro', 'AccNumber': '00001', 'PinNumber': '1119', 'Balance': 5, 'Age': 18, 'Contact': 'filip@keitaro.jp'}


def depoist(customerdict, amount):
    # This function deposits amount in the customer dict
    customerdict['Balance'] += amount
    print(f'New balance is {customerdict["Balance"]}')


def checkbalance(customerdict):
    print(f'Balance is {customerdict["Balance"]}')

def withdraw(customerdict, amount):
    customerdict['Balance'] -= amount
    print(f'New balance is {customerdict["Balance"]}')
