import mysql.connector as db
from model import *

import re
import pandas as pd
con=db.connect(host='localhost',user='root',passwd='Mangu@123',db='mangesh')
print('Connection Establish Successfully')

cursor=con.cursor()


try:
    Admin_Table='create table if not exists admin11(Email text,Password text)'
    cursor.execute(Admin_Table)
    con.commit()
except:
    print('Table already exists')    


try:
    Customer_Table='create table if not exists Customer(Email text,Password text,address text,contact varchar(20),name varchar(20) primary key);'
    cursor.execute(Customer_Table)
    con.commit()
except:
    print('Table already exists')    


try:
    Car_Table='create table if not exists car(Model varchar(20),Car varchar (20),Price int(20),Mileage varchar(30),car_ID int(20) primary key)'
    cursor.execute(Car_Table)
    con.commit()
except:
    print('Table already exists')

try:
    Booking_Table='create table if not exists Booking_list55(booking_id int(20) primary key auto_increment,booking_date date,customer_name varchar(30),foreign key(customer_name) references Customer(name),status varchar(20) default "Pending",car_ID int,foreign key(car_ID) references car(car_ID))'
    cursor.execute(Booking_Table)
    con.commit()
except:
    print('Table already exists')

try:
    Buy_Table='create table if not exists Buying_list(booking_id int(20),foreign key(booking_id) references booking_list55(booking_id),buying_date date,name varchar(30),foreign key(name) references Customer(name),status varchar(20) default "Done",car_ID int(20),foreign key(car_ID) references car(car_ID),price int(20),downpayment int(20),Loan int(20) GENERATED ALWAYS AS (price-downpayment) STORED,for_years int(10),rate float(10,2) default 2.5,EMI BIGINT UNSIGNED GENERATED ALWAYS AS ((((price - downpayment) * rate*for_years/100)+ (price - downpayment))/ (for_years*12)) STORED)'
    cursor.execute(Buy_Table)
    con.commit()
except:
    print('Table already exists')



def Register(x):
    register_query='insert into Customer(Email,Password,address,contact,name) values (%s,%s,%s,%s,%s)'
    cursor.execute(register_query,x)
    con.commit()

def adds(Model,Car,Price,Mileage,car_ID):
    details_query=f'insert into car(Model,Car,Price,Mileage,car_ID) values ("{Model}","{Car}","{Price}","{Mileage}","{car_ID}")'
    cursor.execute(details_query)
    con.commit()

def add(booking_date,customer_name,car_ID):
    details_query=f'insert into Booking_list55(booking_date,customer_name,car_ID) values ("{booking_date}","{customer_name}","{car_ID}")'
    cursor.execute(details_query)
    con.commit()



# def details(z):
#     details_query='insert into Booking_list55(booking_date,customer_name,car_ID) values (%s,%s,%s)'
#     cursor.execute(details_query,z)
#     con.commit()

def details(a):
    details_query='insert into Buying_list(booking_id,buying_date,name,car_ID,price,downpayment,for_years) values (%s,%s,%s,%s,%s,%s,%s)'
    cursor.execute(details_query,a)
    con.commit()


def Admin_Login(Email,Password):
    select_query='select * from admin11 where Email=%s and Password=%s'
    data=(Email,Password)
    cursor.execute(select_query,data)
    s=cursor.fetchone()

    try:
        if s[0]==Email:
            if s[1]==Password:
                return True
    except:
        print('-----Invalid Email or Password-----')            

def Customer_Login(Email,Password):
    select_query='select * from Customer where Email=%s and Password=%s'
    data=(Email,Password)
    cursor.execute(select_query,data)
    s=cursor.fetchone()

    try:
        if s[0]==Email:
            if s[1]==Password:
                return True
    except:
        print('-----Invalid Email or Password-----') 


# def Cust_val(customer_name):
#     select_query='select * from Customer where name=%s'
#     data=(customer_name)
#     cursor.execute(select_query,data)
#     s=cursor.fetchone()

#     try:
#         if s[0]==customer_name:
#             return True
            
#     except:
#         print('-----Invalid name-----')            

#----------------------------------------------------------------------#
#------------- Functions for Admin choices------------------------------------------        
def report_car_list():
    print('\n ***Welcome To Showroom*** ')    
    print('-'*120)    
    sql='select * from car'  
    cursor.execute(sql)  
    records=cursor.fetchall()  
    rec=pd.DataFrame(records,columns=['Model','Car','Price','Mileage','car_ID'])  
    pd.set_option('display.colheader_justify','center')  
    if rec.empty==True:
        print('\n no car found')
    else:
        print(rec)    
   
    wait=input('\n\n Press any key to continue....')

def update_car_info(field):
    print('Update car details') 
    print('-'*60)  
    car_ID=input('Enter car_ID:') 
    value=input('Enter new value:')
    if field=='Price' or field=='Mileage':
        sql=f'update car set {field}= "{value}" where car_ID= {car_ID}'
    else:
        sql=f'update car set {field}= "{value}" where car_ID= {car_ID}'
    cursor.execute(sql)
    con.commit()
    print()
    print('-------Car details updated successfully----')
    wait=input('\n\n\n press any key to continue......')
    

def update_car():
    while True:
        print('1. Model')
        print('2. Car')
        print('3. Price')
        print('4. Mileage')
        print('5. car_ID')
        print('6. Exit to main menu')
        print('\n')
        choice=input('Enter your choice:')
        field='value'
        if choice=='1':
            field='Model'
        if choice=='2':
            field='Car'
        if choice=='3':
            field='Price' 
        if choice=='4':
            field='Mileage' 
        if choice=='5':
            field='car_ID'      
        if choice=='6':
            break
        update_car_info(field)

def report_cust_list():
    print('\n Customer List ')    
    print('-'*120)    
    sql='select Email,address,contact,name from Customer'  
    cursor.execute(sql)  
    records=cursor.fetchall()  
    rec=pd.DataFrame(records,columns=['Email','address','contact','name'])  
    pd.set_option('display.colheader_justify','center')  
    if rec.empty==True:
        print('\n no customer found')
    else:
        print(rec)    
   
    wait=input('\n\n Press any key to continue....')    


def delete_customer():
    print('Delete Customer Screen')
    print('-'*100)
    ac=input('Enter customer name:')
    sql='delete from Customer where name =%s'
    data=(ac,)
    cursor.execute(sql,data)
    con.commit()
    print('\n Customer deleted successfully')
    wait=input('\n press any key to continue.....')

#------------------------Functions for customer choices-----------------#

def report_booking_list():
    print('\n  All Booking ')    
    print('-'*120)    
    sql='select booking_ID,booking_date,customer_name,status,car_ID from Booking_list55'  
    cursor.execute(sql)  
    records=cursor.fetchall()  
    rec=pd.DataFrame(records,columns=['booking_ID','booking_date','customer_name','status','car_ID'])  
    pd.set_option('display.colheader_justify','center')  
    if rec.empty==True:
        print('\n no booked car')
    else:
        print(rec)    
   
    wait=input('\n\n Press any key to continue....') 


def cancel_booking():
    print('Cancel booking Screen')
    print('-'*100)
    ac=input('Enter car_ID:')
    sql='delete from booking_list55 where car_ID=%s'
    data=(ac,)
    cursor.execute(sql,data)
    con.commit()
    print('\n Booking cancel successfully')
    wait=input('\n press any key to continue.....')


def My_booking_list():
    print('\n  My Booking List ')    
    print('-'*120)  
    ac=input('Enter Your name:')  
    sql='select * from booking_list55 WHERE customer_name=%s'  
    data=(ac,)
    cursor.execute(sql,data)  
    records=cursor.fetchall()  
    rec=pd.DataFrame(records,columns=['booking_ID','booking_date','customer_name','status','car_ID'])  
    pd.set_option('display.colheader_justify','center')  
    if rec.empty==True:
        print('\n no booked car')
    else:
        print(rec)    
   
    wait=input('\n\n Press any key to continue....') 
    

def My_Buying_list():
    print('\n   My buying list')    
    print('-'*120)  
    ac=input('\t\t\t Enter Your name:')  
    sql='select buying_date,name,status,car_ID,price,downpayment,EMI from buying_list WHERE name=%s'  
    data=(ac,)
    cursor.execute(sql,data)  
    records=cursor.fetchall()  
    rec=pd.DataFrame(records,columns=['buying_date','name','status','car_ID','price','downpayment','EMI'])  
    pd.set_option('display.colheader_justify','center')  
    if rec.empty==True:
        print('\n no buy car')
    else:
        print(rec)    
    print()
    print('\t\t\t Drive safely.....Live happily')
    print()
    wait=input('\n\n Press any key to continue....') 

    
    