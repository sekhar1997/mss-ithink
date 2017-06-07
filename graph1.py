#importing all the required modules
import numpy as np
from pyspark.sql import *
from pyspark import SparkContext,SparkConf
from pyspark.sql.types import *
import pickle
import pandas as pd
import sys
import json
from pprint import pprint
import csv

#Incoming system arguments from graph_app.py file
#Filename and the decision variable

input_file = sys.argv[1]
dec = sys.argv[2]

#Creating a SparkContext and SqlContext
sc = SparkContext(conf=SparkConf())
sqlContext = SQLContext(sc)

#Reading the InputFile data using SparkContext sc and converting it into list formatt
rddFile = sc.textFile(input_file)
header = rddFile.first()

data = rddFile.map(lambda x:x.split(','))
arr1 = []
arr1 = data.first()
print "===============",arr1

#Sending the Schema(first row of file) into a Temporary textfile using pickle
with open("static/temp_files/temp_schema.txt","wb") as fp:
	pickle.dump(arr1,fp)


datas = rddFile.filter(lambda line:line != header)

data = datas.map(lambda x:x.split(','))

#Creating a DataFrame and a temporary Table view to perform Sql queries
df = sqlContext.createDataFrame(data)
df.createOrReplaceTempView("table1")

if dec=='2':
	#this loop runs if filed name is not specified for selected attribute
	print "\n field name is not specified"
	query_res = []
	display = []
	display_count = []
	schema_attr1 = sys.argv[3]
	
	query1 = "select DISTINCT "+schema_attr1+" from table1 "
	query_res1 = sqlContext.sql(query1)
#converting the dataframe to json data and writing data to csv file
	query_res1.toPandas().to_csv("static/temp_files/temp_data1.csv")
#Reading the data from json file to perform sql queries


	with open('static/temp_files/temp_data1.csv','rb') as csvfile:
		reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
		for row in reader:
			display.append(row[1])
		display.pop(0)	
	#assigning distinct values of attribute to dataframe from dispaly array
	dataframe1 = pd.DataFrame(display)
	print display
	arr2 = []
	len2 = len(display)
	
	display_count=[]
	list1 = []
	for i in range(len2):
		query2 = "select * from table1 where "+schema_attr1+" = '"+display[i]+"' "
		query_res2 = sqlContext.sql(query2)
		list1.append(query_res2.count())
		if i == 0:
			query_res2.toPandas().to_csv('static/temp_files/raw_data1.csv')
		else:
			with open('static/temp_files/raw_data1.csv','a') as f:
				query_res2.toPandas().to_csv(f,header = False)


	print "\n Count array appending to list1 \n",list1
	
	dataframe1[1]=pd.DataFrame(list1)
	dataframe1.to_csv('static/temp_files/temp_data1.csv')

elif dec=='3':
	#this loop runs if filed name is specified for selected attribute
	print "\n filed name is specified for selected attribute"
	attrs = []
	target = open("static/temp_files/val_temp.txt","r+")
	repeat = target.read()
	attrs = repeat.split(',')
	target.close()
	print "printing the query variables ------------",attrs
	schema_attr1 = attrs[0]
	user_attr1 = attrs[1]
	query_res = []
	display = []
	display_count = []
	
	

	display_count=[]
	list1 = []
	user_query = []
	query2 = "select * from table1 where "+schema_attr1+" = '"+user_attr1+"'"
	query_res2 = sqlContext.sql(query2)
	list1.append(query_res2.count())
	query_res2.toPandas().to_csv("static/temp_files/raw_data1.csv")
	
	
	user_query.append(user_attr1)
	dataframe1 = pd.DataFrame(user_query)
	dataframe1[1] = pd.DataFrame(list1)
	dataframe1.to_csv("static/temp_files/temp_data1.csv")
	#out = open('static/temp_files/temp_data1.csv', 'w')
	#out.write(user_query)
	
	
	print "\n Count array appending to list1 \n",list1

elif dec=='4':
	attrs = []
	target = open("static/temp_files/val_temp.txt","r+")
	repeat = target.read()
	attrs = repeat.split(',')
	target.close()
	print "printing the query variables ------------",attrs
	schema_attr1 = attrs[0]
	user_attr1 = attrs[1]
	schema_attr2 = attrs[2]
	user_attr2 = attrs[3]

	if user_attr2!='' and user_attr1!='':
		#this loop runs if both the user attribute values are given
		listx = []
		listy = []
		raw_data = []
		query2 = "select * from table1 where "+schema_attr1+" = '"+user_attr1+"' and "+schema_attr2+"= '"+user_attr2+"'"
		query_res2 = sqlContext.sql(query2)
		listy.append(query_res2.count())
		#raw_data.append(query_res2.collect())

		user_query = "count for the combination of '"+user_attr1+"' and '"+user_attr2+"'"
		listx.append(user_query)
		dataframe2 = pd.DataFrame(listx)

		
		print "\n Count array appending to list1 \n",listy
		dataframe2[1] = pd.DataFrame(listy)
		dataframe2.to_csv('static/temp_files/temp_data1.csv')

		query_res2.toPandas().to_csv("static/temp_files/raw_data1.csv")

	elif user_attr1=='' and user_attr2!='':

		print "\n #first attribute not given and second attribute given"
		ext_query_attr = []
		listy = []
		with open('static/temp_files/temp_data1.csv','rb') as csvfile:
			reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
			for row in reader:
				ext_query_attr.append(row[1])
		
		ext_query_attr.pop(0)
		dataframe2 = pd.DataFrame(ext_query_attr)
		
		print ext_query_attr
		len4 = len(ext_query_attr)
		for i in range(len4):
			query2 = "select * from table1 where "+schema_attr1+" = '"+ext_query_attr[i]+"' and "+schema_attr2+"= '"+user_attr2+"'"
			print "\n",query2
			query_res2 = sqlContext.sql(query2)
			listy.append(query_res2.count())
			if i == 0:
				query_res2.toPandas().to_csv('static/temp_files/raw_data1.csv')
			else:
				with open('static/temp_files/raw_data1.csv','a') as f:
					query_res2.toPandas().to_csv(f,header = False)

		print "\n Count array appending to list1 \n",listy
		dataframe2[1] = pd.DataFrame(listy)
		dataframe2.to_csv('static/temp_files/temp_data1.csv')
		
	elif user_attr1!='' and user_attr2=='':
		empty_list = []
		empty_query_res = []
		ext_query_attr = []
		display3 = []
		
	
		
		both_query = "select DISTINCT "+schema_attr2+" from table1 "
		both_query_res1 = sqlContext.sql(both_query)

		both_query_res1.toPandas().to_csv("static/temp_files/temp_data2.csv")
	
		
		with open('static/temp_files/temp_data2.csv','rb') as csvfile:
			reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
			for row in reader:
				display3.append(row[1])
			display3.pop(0)
		dataframe3 = pd.DataFrame(display3)

	
		for i in range(len(display3)):
			empty_query = "select * from table1 where "+schema_attr1+" = '"+user_attr1+"' and "+schema_attr2+" = '"+display3[i]+"'"
			print empty_query
			
			raw_query_res = sqlContext.sql(empty_query)
			empty_query_res = raw_query_res.count()
			empty_list.append(empty_query_res)
			if i == 0:
				raw_query_res.toPandas().to_csv('static/temp_files/raw_data1.csv')
			else:
				with open('static/temp_files/raw_data1.csv','a') as f:
					raw_query_res.toPandas().to_csv(f,header = False)


		print empty_list

		dataframe3[user_attr1] = pd.DataFrame(empty_list)

		dataframe3.to_csv('static/temp_files/temp_data1.csv')


	elif user_attr1=='' and user_attr2=='':
		empty_list = []
		empty_query_res = []
		ext_query_attr = []
		display3 = []
		display4 = []
		listy = []
		
		both_query = "select DISTINCT "+schema_attr2+" from table1 "
		both_query_res1 = sqlContext.sql(both_query)

		both_query_res1.toPandas().to_csv("static/temp_files/temp_data2.csv")
	
		
		with open('static/temp_files/temp_data2.csv','rb') as csvfile:
			reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
			for row in reader:
				display3.append(row[1])
			display3.pop(0)
		dataframe3 = pd.DataFrame(display3)

		with open('static/temp_files/temp_data1.csv','rb') as csvfile:
			reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
			for row in reader:
				display4.append(row[1])
			display4.pop(0)
		dataframe4 = pd.DataFrame(display4)


		print dataframe3
		print dataframe4
		print "@@@@",display3
		print "!!!!",display4

		for i in range(len(display3)):
			for j in range(len(display4)):
				query = "select * from table1 where "+schema_attr1+" = '"+display4[j]+"' and "+schema_attr2+" = '"+display3[i]+"'"
				print query
				raw_query_res = sqlContext.sql(query)
				query_res = raw_query_res.count()
				listy.append(query_res)

				if i == 0:
					raw_query_res.toPandas().to_csv('static/temp_files/raw_data1.csv')
				else:
					with open('static/temp_files/raw_data1.csv','a') as f:
						raw_query_res.toPandas().to_csv(f,header = False)

		
		for i in range(len(display3)+1):
			for j in range(len(display4)):	
				if(i == 0):
					dfs_empty = pd.DataFrame(display4)
			if i == len(display3):
				break
			else:
				dfs_empty[display3[i]] = pd.DataFrame(listy[(i*(j+1)):(i+1)*(j+1)])
		dfs_empty.to_csv('static/temp_files/temp_data1.csv')

	'''

			

			if(i == 1):
				dfs_empty = pd.DataFrame(empty_list[:j])
			else:
				print display4[i]
				dfs_empty[display3[j]] = pd.DataFrame(listy[(i-1)*j:(i)*j])
		print listy
		dfs_empty.to_csv('static/temp_files/temp_data1.csv')
	'''


