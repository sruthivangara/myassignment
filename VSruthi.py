import csv #importing csv package
import json #importing json package

csv_file = open("SalesJan2009.csv") #openeing csv file as csv_file
for line in csv_file: 
    temp_line  = line.split(",")  #using split function to seperate with ,
   
    temp_line[0] = temp_line[0][1:-1] #using slice for index 0 to clear up extra quote characters
    temp_line[1] = temp_line[1][1:-1] #using slice for index 1 to clear up extra quote characters
    temp_line[2] = temp_line[2][1:-1] #using slice for index 2 to clear up extra quote characters
    temp_line[3] = temp_line[3][1:-1] #using slice for index 3 to clear up extra quote characters
    temp_line[4] = temp_line[4][1:-1] #using slice for index 4 to clear up extra quote characters
    temp_line[5] = temp_line[5][1:-1] #using slice for index 5 to clear up extra quote characters
    temp_line[6] = temp_line[6][1:-1] #using slice for index 7 to clear up extra quote characters
    temp_line[7] = temp_line[7][1:-1] #using slice for index 7 to clear up extra quote characters
   
    print(temp_line[0],temp_line[1],temp_line[2],temp_line[3],temp_line[4],temp_line[5],temp_line[6],temp_line[7]) #printing the data after removing double quotes

sales_data = []  #created an empty list called sales_data

#processing the data line by line and storing it in to each dictonary 

my_dict = {"Transcation_date":"1/2/2009 6:17","Product":"Product1","Price":"1200","Payment_Type":"Mastercard","Name":"carolina","City":"Basildon","State":"England","Country":"United Kingdom"}    #created a dictonary my_dict
my_dict1 = {"Transcation_date":"1/2/2009 4:53","Product":"Product1","Price":"1200","Payment_Type":"Visa","Name":"Betina","City":"Parkville","State":"MO","Country":"United States"}                #created a dictonary my_dict1
my_dict2 = {"Transcation_date":"1/2/2009 13:08","Product":"Product1","Price":"1200","Payment_Type":"Mastercard","Name":"Federica e Andrea","City":"Astoria","State":"OR","Country":"United States"} #created a dictonary my_dict2
my_dict3 = {"Transcation_date":"1/2/2009 14:44","Product":"Product1","Price":"1200","Payment_Type":"Visa","Name":"Gouya","City":"Echuca","State":"Victoria","Country":"Australia"}                  #created a dictonary my_dict3
my_dict4 = {"Transcation_date":"1/2/2009 12:56","Product":"Product2","Price":"3600","Payment_Type":"visa","Name":"Gerd W","City":"Cahaba Heights","State":"AL","Country":"United States"}           #created a dictonary my_dict4
my_dict5 = {"Transcation_date":"1/2/2009 13:19","Product":"Product1","Price":"1200","Payment_Type":"Visa","Name":"LAURENCE","City":"Mickleton","State":"NJ","Country":"United States"}              #created a dictonary my_dict5
my_dict6 = {"Transcation_date":"1/2/2009 20:11","Product":"Product1","Price":"1200","Payment_Type":"Mastercard","Name":"Fleur","City":"Peoria","State":"IL","Country":"United States"}              #created a dictonary my_dict6
my_dict7 = {"Transcation_date":"1/2/2009 20:09","Product":"Product1","Price":"1200","Payment_Type":"Mastercard","Name":"adam","City":"Martin","State":"TN","Country":"United States"}               #created a dictonary my_dict7
my_dict8 = {"Transcation_date":"1/2/2009 13:17","Product":"Product1","Price":"1200","Payment_Type":"Mastercard","Name":"Renee Elisabeth","City":"Tel Aviv","State":"Tel Aviv","Country":"Israel"}   #created a dictonary my_dict8
sales_data.append(my_dict)   #created an dictionary named my_data and appending it to sales_data
sales_data.append(my_dict1)  #created an dictionary named my_data1 and appending it to sales_data
sales_data.append(my_dict2)  #created an dictionary named my_data2 and appending it to sales_data
sales_data.append(my_dict3)  #created an dictionary named my_data3 and appending it to sales_data
sales_data.append(my_dict4)  #created an dictionary named my_data4 and appending it to sales_data
sales_data.append(my_dict5)  #created an dictionary named my_data5 and appending it to sales_data
sales_data.append(my_dict6)  #created an dictionary named my_data6 and appending it to sales_data
sales_data.append(my_dict7)  #created an dictionary named my_data7 and appending it to sales_data
sales_data.append(my_dict8)  #created an dictionary named my_data8 and appending it to sales_data

print(sales_data)  #printing the data that was appeneded into sales_data


#saving the sales_data list into file named transaction_data.json
with open('transaction_data.json', 'w') as f: 
    for item in sales_data:  #the items in sales_data
         f.write("%s\n" % item) 


# GitHub Link : https://github.com
#repository name : myassignment
         
