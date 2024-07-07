from model import *
import database as db
from validation import * 
import maskpass
print('\t*******Car Showroom Management System*******')

choice=0

while(choice!=4):
    print('\t\t\t 1.login')
    print('\t\t\t 2.Signup')
    print('\t\t\t 3.Show')
    print('\t\t\t 4.Exit') 
    print()
    choice=int(input('\t\t\t Enter your choice:'))
    print()

    if choice==1:
        print('\t\t\t *****Login*****')
        print()
        while True:
            print('\t\t\t 1.Admin login')
            print('\t\t\t 2.Customer Login')
            print('\t\t\t 3.Exit')
            print()
            choice=input('\t\t\t Enter your login choice:')

#--------------------- Admin login----------------------------------#
            if choice=='1':
                print('\t\t\t -----<Admin Login Section>----\n')
                print()
                #Email validation
                while True:

                    Email=input('\t\t\t Enter your Email:')
                    if EmailValidation(Email):
                        break
                 
                    else:
                        print('\n-----Invaild Email----\n')

                 #password validation
                while True:
                     Password=maskpass.askpass('\t\t\t Enter Your Password:',mask='*') 
                     if PasswordValidation(Password)==True:

                        break
                     else:
                         print('\n-----Invalid Password----\n')         
                
                data=db.Admin_Login(Email,Password)
                if data==True:
                    print('\t\t\t -----<Admin login successfully>----\n')
                    print()

#-----------------------Admin Choices----------------------------------------------#                    
                    while True:
                        print('\t\t\t --------<Admin Choice>-------------')
                        print()

                        print('\t\t\t 1.Add car details')
                        print('\t\t\t 2.Display car detail')
                        print('\t\t\t 3.Update car detail')
                        print('\t\t\t 4.customer list')
                        print('\t\t\t 5.booking list')
                        print('\t\t\t 6.Delete customer')
                        print('\t\t\t 7.Exit')
                        print()
                        choice=input('\t\t\t enter your Choice:')
                        if choice=='1':
                            print('\t\t\t ---------<Car Details>--------\n')

                            #model name
                            while True:
                                Model=input('\t\t\t Enter  model name:')
                                if AddressValidation(Model):
                                    break
                                else:
                                    print('\n-----------Invalid model-----------\n')

                            #car name 
                            while True:
                                Car=input('\t\t\t Enter  car name:')
                                if AddressValidation(Car):
                                    break
                                else:
                                    print('\n-----------Invalid car-----------\n')

                            #price        
                            while True:
                                Price=input('\t\t\t Enter price:')
                                if AddressValidation(Price):
                                    break
                                else:
                                    print('\n-----------Invalid price-----------\n')

                            #mileage
                            while True:
                                Mileage=input('\t\t\t Enter mileage:')
                                if AddressValidation(Mileage):
                                    break
                                else:
                                    print('\n-----------Invalid mileage-----------\n') 
                            
                            #car_ID
                            while True:
                                car_ID=input('\t\t\t Enter car_ID:')
                                if AddressValidation(car_ID):
                                    break
                                else:
                                    print('\n-----------Invalid mileage-----------\n') 

                            # y=(Model,Car,Price,Mileage,car_ID)
                            db.adds(Model,Car,Price,Mileage,car_ID)
                            print()
                            print('\t\t\t -----------<Details submitted Successfully>-------')
                            print() 
                        
                        elif choice=='2':
                            db.report_car_list()

                        elif choice=='3':
                            db.update_car() 
                        
                        elif choice=='4':
                            db.report_cust_list() 

                        elif choice=='5':
                            db.report_booking_list()   

                        elif choice=='6':
                            db.delete_customer() 

                        elif choice=='7':
                            break
                
                
                
                else:
                    print('-----Admin Email or Password wrong------')

            
#------------------Customer login-------------------------------#
            if choice=='2':
                print('\t\t\t -----<Customer Login Section>----\n')
                print()
                #Email validation
                while True:

                    Email=input('\t\t\t Enter your Email:')
                    if EmailValidation(Email):
                        break
                 
                    else:
                        print('\n-----Invaild Email----\n')

                 #password validation
                while True:
                     Password=maskpass.askpass('\t\t\t Enter Your Password:',mask='*') 
                     if PasswordValidation(Password)==True:

                        break
                     else:
                         print('\n-----Invalid Password----\n')         
                
                data=db.Customer_Login(Email,Password)
                if data==True:
                    print('\t\t\t -----<Customer login successfully>----\n')

#------------------------Customer Choices-----------------------------------#                    
                    while True:
                        print('\t\t\t 1.show car details')
                        print('\t\t\t 2.Book car')
                        print('\t\t\t 3.My booking list')
                        print('\t\t\t 4.Buy car')
                        print('\t\t\t 5.Cancel booking')
                        print('\t\t\t 6.Exit')
                        print()
                        choice=input("\t\t\t Enter your choice:")

                        if choice=='1':
                            db.report_car_list()

                        elif choice=='2':
                                                  
                            #booking date      
                            while True:
                                booking_date=input('\t\t\t Enter booking date:')
                                if AddressValidation( booking_date):
                                    break
                                else:
                                    print('\n-----------Invalid price-----------\n')

                            #customer name
                            while True:

                                customer_name=input('\t\t\t Enter customer name:')
                                
                                if AddressValidation(customer_name):
                                     
                                     break

                                    
                                else:
                                    print('\n-----------Invalid customer name-----------\n') 
                                

                            
                            while True:
                                car_ID=input('\t\t\t Enter car_ID:')                                
                                if AddressValidation(car_ID):

                                    break
                                else:
                                    print('\n-----------Invalid car ID-----------\n')
                               

                            # z=(booking_date,customer_name,car_ID)
                            db.add(booking_date,customer_name,car_ID)
                            print()
                            print('\t\t\t -----------<car booked Successfully>-------')
                            print() 

                        elif choice=='3':
                            db.My_booking_list()  


                        elif choice=='4':
                            while True:
                                booking_id=input('\t\t\t Enter booking id:')
                                if AddressValidation( booking_id):
                                    break
                                else:
                                    print('\n-----------Invalid booking id-----------\n') 

                            while True:
                                buying_date=input('\t\t\t Enter date:')
                                if AddressValidation( buying_date):
                                    break
                                else:
                                    print('\n-----------Invalid buying_date-----------\n')    

                            while True:
                                customer_name=input('\t\t\t Enter customer name:')
                                if AddressValidation(customer_name):
                                    break
                                else:
                                    print('\n-----------Invalid customer_name-----------\n')            

                             
                            while True:
                                car_ID=input('\t\t\t Enter car_ID:')
                                if AddressValidation(car_ID):
                                    break
                                else:
                                    print('\n-----------Invalid car_ID-----------\n') 


                            while True:
                                price=input('\t\t\t Enter price:')
                                if AddressValidation(price):
                                    break
                                else:
                                    print('\n-----------Invalid price-----------\n')   

                            while True:
                                downpayment=input('\t\t\t Enter downpayment:')
                                if AddressValidation(downpayment):
                                    break
                                else:
                                    print('\n-----------Invalid downpayment-----------\n') 

                            while True:
                                for_years=input('\t\t\t Enter years:')
                                if AddressValidation(for_years):
                                    break
                                else:
                                    print('\n-----------Invalid for_years-----------\n') 
                                                    
                            a=(booking_id,buying_date,customer_name,car_ID,price,downpayment,for_years)
                            db.details(a)
                            print()
                            print('\t\t\t -----------<car buy Successfully>-------')
                            print() 
                            print('\t\t\t----------<Your Buying details>--------')
                            db.My_Buying_list()

                        elif choice=='5':
                            db.cancel_booking()    

                        elif choice=='6':
                            break      



                else:
                    print('-----Customer Email or Password wrong------')

            if choice=='3':
                break
            

#------------------------signup for Customer-----------------------#
    elif choice==2:
        print('\t\t\t ********* signup ********')
        #Email validation
        while True:
            Email=input('\t\t\t Enter your Email:')
            if EmailValidation(Email):
                break
            else:
                print('\n-----Invaild Email----\n')

         #password validation
        while True:
            Password=maskpass.askpass('\t\t\t Enter Your Password:',mask='*') 
            if PasswordValidation(Password)==True:
                break
            else:
                print('\n-----Invalid Password----\n')     
        
        #Address validation
        while True:
            Address=input('\t\t\t Enter your address: ')  
            if AddressValidation(Address):
                break
            else:
                print('please enter valid address: ')  

        #Contact validation
        while True:
            Contact=input('\t\t\t Enter your contact: ')      
            if ContactValidation(Contact):
                break
            else:
                print('Enter valid contact: ')   

        #Name validation          
        while True:
            Name=input('\t\t\t Enter your name:')
            if NameValidation(Name):
                break
            else:
                print('Enter valid name:')
 

        x=(Email,Password,Address,Contact,Name)
        db.Register(x)
        print()
        print('\t\t\t -----Account Created Successfully----')
        print()






    elif choice==3:
        db.report_car_list()     
    else:
        break       