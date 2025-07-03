from selenium import webdriver
from array import array
from selenium.webdriver.common.keys import Keys
import xlsxwriter
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
#driver.get("https://merchant.stag.asyadexpress.com/order/domestic-order")
workbook = xlsxwriter.Workbook('Bulk Domestic Creation.xlsx') 
worksheet = workbook.add_worksheet() 

driver.get("https://merchant.stag.asyadexpress.com")
login_button = driver.find_element(By.XPATH, "//*[@id='validateLogin']")
assert login_button.is_displayed()
user_name = driver.find_element(By.XPATH, "//*[@id='username']")
password = driver.find_element(By.XPATH, "//*[@id='password']")
# input user name and password
user_name.send_keys("####")
password.send_keys("####")
# click on login button
login_button.click()
driver.get("https://merchant.stag.asyadexpress.com/order/domestic-order")
bulk_title=driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div[1]/h4")

# here is the Array Creation 
error_list = []
title_text = driver.find_element(By.XPATH,"/html/body/div[5]/div/div[2]/div/div/div[1]/h4").text
if title_text =="Bulk Domestic Creation":
    print(title_text)
else :
    error_list.append(title_text)

# Order Reference check
order_ref_text =driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[2]/div/span").text
if order_ref_text =="Order Reference *":
    print(order_ref_text)
else :
    error_list.append(order_ref_text)

# Sender Name check
sender_name_text = driver.find_element(By.XPATH , "//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[3]/div/span").text
if  sender_name_text =="Sender Name *":
    print(sender_name_text)
else :
    error_list.append(sender_name_text)
    
#sender company name check
sender_company_name=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[4]/div/span").text
if  sender_company_name=="Sender Company Name": 
    print(sender_company_name)
else :
    error_list.append(sender_company_name)
   
#Sender Address 1 check
Sender_Add1=driver.find_element(By.XPATH,"*//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[5]/div").text
if Sender_Add1 =="Sender Address 1 *": 
    print(Sender_Add1)
else :
    error_list.append(Sender_Add1)
   
#Sender Address 2 check
Sender_Add2=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[6]/div/span").text
if Sender_Add2 =="Sender Address 2": 
    print(Sender_Add2)
else :
    error_list.append(Sender_Add2)
   
#Sender Governate chec
sender_Governate=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[7]/div/span").text
if  sender_Governate=="Sender Governate *":
    print(sender_Governate)
else :
    error_list.append(sender_Governate)
  

#Sender Wilayat  check
Sender_Wilayat=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[8]/div/span").text
if Sender_Wilayat =="Sender Wilayat *":
    print(Sender_Wilayat)
else :
    error_list.append(Sender_Wilayat)

#Sender City check
Sender_City=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[9]/div").text
if  Sender_City=="Sender City *":
    print(Sender_City)
else :
    error_list.append(Sender_City)
   
#Sender Area  check
Sender_Area=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[10]/div/span").text
if  Sender_Area=="Sender Area *":
    print(Sender_Area)
else :
    error_list.append(Sender_Area)
    
#Sender Phone check
Sender_Phone=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[11]/div/span").text
if  Sender_Phone=="Sender Phone *":
    print(Sender_Phone)
else :
    error_list.append(Sender_Phone)
   
#Sender Email check
Sender_Email=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[12]/div/span").text
if  Sender_Email=="Sender Email":
    print(Sender_Email)
else :
    error_list.append(Sender_Email)

#Receiver Name check
Receiver_Name=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[13]/div/span").text
if  Receiver_Name=="Receiver Name *":
    print(Receiver_Name)
else :
    error_list.append(Receiver_Name)

#Receiver Company Name check
Receiver_Company_Name=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[14]/div/span").text
if  Receiver_Company_Name=="Receiver Company Name":
    print(Receiver_Company_Name)
else :
    error_list.append(Receiver_Company_Name)

#Receiver Address 1 *check
Receiver_Add1 =driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[15]/div/span").text
if  Receiver_Add1=="Receiver Address 1 *":
    print(Receiver_Add1)
else :
    error_list.append(Receiver_Add1)

#Receiver Address 2 check
Receiver_Add2=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[16]/div").text
if  Receiver_Add2=="Receiver Address 2":
    print(Receiver_Add2)
else :
    error_list.append(Receiver_Add2)
   
#Receiver Governate *check
Receiver_Governate=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[17]/div/span").text
if  Receiver_Governate=="Receiver Governate *":
    print(Receiver_Governate)
else :
    error_list.append(Receiver_Governate)
 
#Receiver Wilayat *check
Receiver_Wilayat=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[18]/div/span").text
if Receiver_Wilayat =="Receiver Wilayat *":
    print(Receiver_Wilayat)
else :
    error_list.append(Receiver_Wilayat)

#Receiver City *check
Receiver_City=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[19]/div/span").text
if  Receiver_City=="Receiver City *":
    print(Receiver_City)
else :
    error_list.append(Receiver_City)

#Receiver Area *check
Receiver_Area=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[20]/div/span").text
if  Receiver_Area=="Receiver Area *":
    print(Receiver_Area)
else :
    error_list.append(Receiver_Area)
 
#Receiver Phone *check
Receiver_Phone=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[21]/div/span").text
if  Receiver_Phone=="Receiver Phone *":
    print(Receiver_Phone)
else :
    error_list.append(Receiver_Phone)

#Receiver Email *check
Receiver_Email=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[22]/div/span").text
if  Receiver_Email=="Receiver Email *":
    print(Receiver_Email)
else :
    error_list.append(Receiver_Email)

#Payment *check
Payment=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[23]/div/span").text
if  Payment=="Payment *":
    print(Payment)
else :
    error_list.append(Payment)
  
#Amount *check
Amount=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[24]/div/span").text
if  Amount=="Amount *":
    print(Amount)
else :
    error_list.append(Amount)

#Total Weight (KG) *check
Total_Weight=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[25]/div/span").text
if  Total_Weight=="Total Weight (KG) *":
    print(Total_Weight)
else :
    error_list.append(Total_Weight)

#Pickup Type check
Pickup_Type=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[26]/div/span").text
if  Pickup_Type=="Pickup Type *":
    print(Pickup_Type)
else :
    error_list.append(Pickup_Type)
  
#Description *check
Description=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[27]/div/span").text
if  Description=="Description *":
    print(Description)
else :
    error_list.append(Description)
  
#Number of Packages check
Number_of_Packages=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[28]/div/span").text
if  Number_of_Packages=="Number of Packages":
    print(Number_of_Packages)
else :
    error_list.append(Number_of_Packages)
  
#Pickup at Delivery check
Pickup_at_Delivery=driver.find_element(By.XPATH,"//*[@id='example1']/div[2]/div/div/div/table/thead/tr/th[29]/div/span").text
if  Pickup_at_Delivery=="Pickup at Delivery":
    print(Pickup_at_Delivery)
else :
    error_list.append(Pickup_at_Delivery)
    

print("Errors: ",error_list)


#newwwwwww
row = 0
column = 0

for error in error_list:
    worksheet.write(row, column, error)
    column +=1




#
# 
# input()
