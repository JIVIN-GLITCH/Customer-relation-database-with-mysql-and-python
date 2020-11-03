from tkinter import *
import mysql.connector
from csv import writer
from tkinter import ttk

root = Tk()
root.title("Customer Relationship Management")
root.geometry("400x600")

# Connect to mysql
mydb = mysql.connector.connect(
		host = "localhost",
		user = "root",
		passwd = "your mysql password",
		#auth_plugin='mysql_native_password', 
		database = 'database name',
	)

#print(mydb)

# Create cursor and initialise it
my_cursor = mydb.cursor()

# Create database
#my_cursor.execute("CREATE DATABASE codemy")


# Test to see if database was created
#my_cursor.execute("SHOW DATABASES") 
#for db in my_cursor:
	#print(db)


# VARCHAR IS TEXT
# Create table

my_cursor.execute("""CREATE TABLE IF NOT EXISTS customers (
		first_name VARCHAR(255),
		last_name VARCHAR(255),
		zipcode int(10),
		price_paid DECIMAL(10,2),
		user_id INT AUTO_INCREMENT PRIMARY KEY)
		""")


# Alter table
'''
my_cursor.execute("""ALTER TABLE customers ADD (
	email VARCHAR(255),
	address_1 VARCHAR(255),
	address_2 VARCHAR(255),
	city VARCHAR(50),
	state VARCHAR(50),
	country VARCHAR(255),
	phone VARCHAR(255),
	payment_method VARCHAR(50),
	discount_code VARCHAR(255))
	""")
'''

# Show table

#my_cursor.execute("SELECT * FROM customers")

'''
for thing in my_cursor.description:
	print(thing)

'''

# Clear value fields in app
def clear_fields():
	first_name_box.delete(0,END)
	last_name_box.delete(0,END)
	address1_box.delete(0,END)
	address2_box.delete(0,END)
	city_box.delete(0,END)
	state_box.delete(0,END)
	zipcode_box.delete(0,END)
	country_box.delete(0,END)
	phone_box.delete(0,END)
	email_box.delete(0,END)
	username_box.delete(0,END)
	payment_method_box.delete(0,END)
	discount_code_box.delete(0,END)
	price_paid_box.delete(0,END)

# Submit customer to databse
def add_customer():
	sql_command = "INSERT INTO customers (first_name,last_name,zipcode,price_paid,email,address_1,address_2,city,state,country,phone,payment_method,discount_code) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	values = (first_name_box.get(),last_name_box.get(),zipcode_box.get(),price_paid_box.get(),email_box.get(),address1_box.get(),address2_box.get(),city_box.get(),state_box.get(),country_box.get(),phone_box.get(),payment_method_box.get(),discount_code_box.get())

	# Query databse
	my_cursor.execute(sql_command,values)

	mydb.commit()

	#Clear fields
	clear_fields()

# List out the names of all customers
def list_customers():
	branch = Tk()
	branch.title("List of all customers")
	branch.geometry("800x600")

	my_cursor.execute("SELECT * FROM customers")
	res = my_cursor.fetchall()
	num = 0
	for i,x in enumerate(res):
		for y in x:
			cust_labl = Label(branch,text = y).grid(row = i,column = num)
			num += 1

	csv_button = Button(branch,text = "Save to Excel",command = lambda:write_to_csv(res))
	csv_button.grid(row = i + 1,column = 0)

	mydb.commit()
		
	branch.mainloop()

def write_to_csv(res):
	with open('customers.csv','a') as f:
		w = writer(f,dialect = 'excel')
		for record in res:
			w.writerow(record) 

def search_customers():
	branch2 = Tk()
	branch2.title("Search/Edit for customers")
	branch2.geometry("900x600")


	def update():
		sql_command = """UPDATE customers SET first_name = %s,last_name = %s,zipcode = %s,price_paid = %s,email = %s,address_1 = %s,address_2 = %s,city = %s,state = %s,country = %s,phone = %s,payment_method = %s,discount_code = %s WHERE user_id = %s"""

		first_name = first_name_box2.get()
		last_name =last_name_box2.get()
		address_1 = address1_box2.get()
		address_2 = address2_box2.get()
		city = city_box2.get()
		state = state_box2.get()
		zipcode = zipcode_box2.get()
		country = country_box2.get()
		phone = phone_box2.get()
		email = email_box2.get()
		payment_method = payment_method_box2.get()
		discount_code = discount_code_box2.get()
		price_paid = price_paid_box2.get()
		id_value = id_box2.get

		inputs = (first_name, last_name, zipcode, price_paid, email, address_1, address_2, city, state, country, phone, payment_method, discount_code, id_value)
		my_cursor.execute(sql_command, inputs)
		mydb.commit()

		branch2.destroy()


	def edit_now(id,index):
		first_name_label = Label(branch2,text = "First Name").grid(row = index + 1,column = 0,sticky = W,padx = 10)
		last_name_label = Label(branch2,text = "Last Name").grid(row = index + 2,column = 0,sticky = W,padx = 10)
		address1_label = Label(branch2,text = "Address 1").grid(row = index + 3,column = 0,sticky = W,padx = 10)
		address2_label = Label(branch2,text = "Address 2").grid(row = index + 4,column = 0,sticky = W,padx = 10)
		city_label = Label(branch2,text = "City").grid(row = index + 5,column = 0,sticky = W,padx = 10)
		state_label = Label(branch2,text = "State").grid(row = index + 6,column = 0,sticky = W,padx = 10)
		zipcode_label = Label(branch2,text = "Zipcode").grid(row = index + 7,column = 0,sticky = W,padx = 10)
		country_label = Label(branch2,text = "Country").grid(row = index + 8,column = 0,sticky = W,padx = 10)
		phone_label = Label(branch2,text = "Phone").grid(row = index + 9,column = 0,sticky = W,padx = 10)
		email_label = Label(branch2,text = "Email").grid(row = index + 10,column = 0,sticky = W,padx = 10)
		username_label = Label(branch2,text = "Username").grid(row = index + 11,column = 0,sticky = W,padx = 10)
		payment_method_label = Label(branch2,text = "Payment Method").grid(row = index +  12,column = 0,sticky = W,padx = 10)
		discount_code_label = Label(branch2,text = "Discount code").grid(row = index + 13,column = 0,sticky = W,padx = 10)
		price_paid_label = Label(branch2,text = "Price Paid").grid(row = index + 14,column = 0,sticky = W,padx = 10)
		id_label = Label(branch2,text = "User id").grid(row = index + 15,column = 0,sticky = W,padx = 10)
		# Entry boxes

		sql2 = "SELECT * FROM customers WHERE user_id = %s"
		name2 = (id,)

		global result2

		result2 = my_cursor.execute(sql2,name2)
		result2 = my_cursor.fetchall()

		global first_name_box2
		first_name_box2 = Entry(branch2)
		first_name_box2.grid(row = index + 1,column = 1,pady = 5)
		first_name_box2.insert(0,result2[0][0])

		global last_name_box2
		last_name_box2 = Entry(branch2)
		last_name_box2.grid(row = index + 2,column = 1,pady = 5)
		last_name_box2.insert(0,result2[0][1])

		global address1_box2
		address1_box2 = Entry(branch2)
		address1_box2.grid(row = index + 3,column = 1,pady = 5)
		address1_box2.insert(0,result2[0][6])

		global address2_box2
		address2_box2 = Entry(branch2)
		address2_box2.grid(row = index + 4,column = 1,pady = 5)
		address2_box2.insert(0,result2[0][7])
		
		global city_box2
		city_box2 = Entry(branch2)
		city_box2.grid(row = index + 5,column = 1,pady = 5)
		city_box2.insert(0,result2[0][8])

		global state_box2
		state_box2 = Entry(branch2)
		state_box2.grid(row = index + 6,column = 1,pady = 5)
		state_box2.insert(0,result2[0][9])

		global zipcode_box2
		zipcode_box2 = Entry(branch2)
		zipcode_box2.grid(row =index +  7,column = 1,pady = 5)
		zipcode_box2.insert(0,result2[0][2])

		global country_box2
		country_box2 = Entry(branch2)
		country_box2.grid(row = index + 8,column = 1,pady = 5)
		country_box2.insert(0,result2[0][10])

		global phone_box2
		phone_box2 = Entry(branch2)
		phone_box2.grid(row = index + 9,column = 1,pady = 5)
		phone_box2.insert(0,result2[0][11])

		global email_box2
		email_box2 = Entry(branch2)
		email_box2.grid(row = index + 10,column = 1,pady = 5)
		email_box2.insert(0,result2[0][5])
		

		global username_box2
		username_box2 = Entry(branch2)
		username_box2.grid(row = index + 11,column = 1,pady = 5)
		username_box2.insert(0,result2[0][0])

		global payment_method_box2
		payment_method_box2 = Entry(branch2)
		payment_method_box2.grid(row = index + 12,column = 1,pady = 5)
		payment_method_box2.insert(0,result2[0][12])

		global discount_code_box2
		discount_code_box2 = Entry(branch2)
		discount_code_box2.grid(row = index + 13,column = 1,pady = 5)
		discount_code_box2.insert(0,result2[0][13])

		global price_paid_box2 
		price_paid_box2 = Entry(branch2)
		price_paid_box2.grid(row = index + 14,column = 1,pady = 5)
		price_paid_box2.insert(0,result2[0][3])

		global id_box2
		id_box2 = Entry(branch2)
		id_box2.grid(row = index + 15,column = 1,pady = 5)
		id_box2.insert(0,result2[0][4])

		save_btn = Button(branch2,text = "Save Record",command = update).grid(row = index + 16,column = 1)


	# Search customer
	def search():
		selected = drop.get()

		if selected == "Search by...":
			test = Label(branch2,text = "Looks like you forgot to pick a dropdown selection..",width = 30)
			test.grid(row =3,column = 0)

		if selected == 'Last Name':

			Sql = "SELECT * FROM customers WHERE last_name = %s"
		if selected == 'Email':

			Sql = "SELECT * FROM customers WHERE email = %s"
		if selected == 'First Name':

			Sql = "SELECT * FROM customers WHERE first_name = %s"

		
		name = search_box.get()

		my_cursor.execute(Sql,(name,))
		global result
		result = my_cursor.fetchall()

		if not result:
			result = "Record not found...."


		for i,x in enumerate(result):
			num = 0
			i += 2
			id_reference = x[4]
			edit_btn = Button(branch2,text = "Edit " + str(id_reference),command = lambda:edit_now(id_reference,i)).grid(row = i,column = num)
			for y in x:
				cust_labl = Label(branch2,text = y).grid(row = i,column = num + 1)
				num += 1

		print(result)
		#searched_label = Label(branch2,text = result).grid(row = 2,column = 0,columnspan = 2)

		mydb.commit()

	# Entry box for customer search
	search_box = Entry(branch2)
	search_box.grid(row = 0,column = 1,pady = 10)
	# Label to search for customer
	search_label = Label(branch2,text = "Search").grid(row = 0,column = 0,pady = 10)

	search_button = Button(branch2,text = "Search",command = search).grid(row = 1,column = 1,pady = 10)

	# Dropdown
	drop = ttk.Combobox(branch2,values= ["Search by...",'Last Name','Email','First Name'])
	drop.current(0)
	drop.grid(row = 0,column = 2)

# Create label
title_label = Label(root,text = "Codemy database",font = ("Helvetica",16))
title_label.grid(row = 0,column = 0,pady = 10,columnspan = 2)

# Create main form to enter customer data
first_name_label = Label(root,text = "First Name").grid(row = 1,column = 0,sticky = W,padx = 10)
last_name_label = Label(root,text = "Last Name").grid(row = 2,column = 0,sticky = W,padx = 10)
address1_label = Label(root,text = "Address 1").grid(row = 3,column = 0,sticky = W,padx = 10)
address2_label = Label(root,text = "Address 2").grid(row = 4,column = 0,sticky = W,padx = 10)
city_label = Label(root,text = "City").grid(row = 5,column = 0,sticky = W,padx = 10)
state_label = Label(root,text = "State").grid(row = 6,column = 0,sticky = W,padx = 10)
zipcode_label = Label(root,text = "Zipcode").grid(row = 7,column = 0,sticky = W,padx = 10)
country_label = Label(root,text = "Country").grid(row = 8,column = 0,sticky = W,padx = 10)
phone_label = Label(root,text = "Phone").grid(row = 9,column = 0,sticky = W,padx = 10)
email_label = Label(root,text = "Email").grid(row = 10,column = 0,sticky = W,padx = 10)
username_label = Label(root,text = "Username").grid(row = 11,column = 0,sticky = W,padx = 10)
payment_method_label = Label(root,text = "Payment Method").grid(row = 12,column = 0,sticky = W,padx = 10)
discount_code_label = Label(root,text = "Discount code").grid(row = 13,column = 0,sticky = W,padx = 10)
price_paid_label = Label(root,text = "Price Paid").grid(row = 14,column = 0,sticky = W,padx = 10)

# Entry boxes
first_name_box = Entry(root)
first_name_box.grid(row = 1,column = 1,pady = 5)

last_name_box = Entry(root)
last_name_box.grid(row = 2,column = 1,pady = 5)

address1_box = Entry(root)
address1_box.grid(row = 3,column = 1,pady = 5)

address2_box = Entry(root)
address2_box.grid(row = 4,column = 1,pady = 5)

city_box = Entry(root)
city_box.grid(row = 5,column = 1,pady = 5)

state_box = Entry(root)
state_box.grid(row = 6,column = 1,pady = 5)

zipcode_box = Entry(root)
zipcode_box.grid(row = 7,column = 1,pady = 5)

country_box = Entry(root)
country_box.grid(row = 8,column = 1,pady = 5)

phone_box = Entry(root)
phone_box.grid(row = 9,column = 1,pady = 5)

email_box = Entry(root)
email_box.grid(row = 10,column = 1,pady = 5)

username_box = Entry(root)
username_box.grid(row = 11,column = 1,pady = 5)

payment_method_box = Entry(root)
payment_method_box.grid(row = 12,column = 1,pady = 5)

discount_code_box = Entry(root)
discount_code_box.grid(row = 13,column = 1,pady = 5)


price_paid_box = Entry(root)
price_paid_box.grid(row = 14,column = 1,pady = 5)


# Create Buttons

add_customer_button = Button(root,text = "Add Customer to Database",command = add_customer)
add_customer_button.grid(row = 15,column = 0,pady = 10)

clear_fields_button = Button(root,text = "Clear Fields",command = clear_fields).grid(row = 15,column = 1,pady  =10)

list_customer_btn = Button(root,text = "List Customers",command = list_customers).grid(row = 16,column = 0,sticky = W,padx = 10)

search_btn = Button(root,text = "Search/Edit Customers",command = search_customers).grid(row = 16,column = 1,padx = 20)

root.mainloop()
