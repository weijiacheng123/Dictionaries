import csv
customers = open('customers.csv','r')
customer_file = csv.reader(customers,delimiter=',')

next(customer_file)

for record in customer_file:
    print(record)
    print('first name:',record[1])
    print('last name:',record[2])
    print('city:',record[3])
    print('country:',record[4])
    print('phone:',record[5])

