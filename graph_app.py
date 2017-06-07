#importing required modules
import os
import pickle
import csv
import json
import pygal
import pandas as pd
from flask import Flask,redirect, url_for,request,render_template
app = Flask(__name__)
input_file = 'data.csv'

#Routing to index.html page 
@app.route('/')
def hello_world():
	
  	return render_template("index.html")

#Route to graph_query.html page
@app.route('/graph_query')
def graph_query():
	dec = '1'
	global input_file
	#getting the browsed input file to a variable
	input_file = request.args.get('input_file')
	#passing input_file and dec to graph1.py as command line arguments
	command = "spark-submit graph1.py "+input_file+" "+dec                   
    	os.system(command)
	#Reading all the schema attributes from temp_schema.txt
	with open("static/temp_files/temp_schema.txt","rb") as fp:
		schema1 = pickle.load(fp)
	len1 = len(schema1) 
  	return render_template("index2.html",schema1=schema1,len1=len1)


#Routing to display1.html page
@app.route('/graph_analysis1')	
def graph_analysis1():
	
	#Getting schema attribute and user input selected in graph_query.html from the browser 
	schema_attr1 = request.args.get('schema_attr1')
	user_attr1 = request.args.get('user_attr1')
		
		
	#If Attribute is not specified with any value,i.e.,user_attr1 is empty
	if user_attr1=='':
		dec = '2'
		#intializing arrays to store the result 
		display1 = []
		display_count = []
		
		#Writing schema_attr1 and user_attr1 to val_temp.txt file
		target = open('static/temp_files/val_temp.txt', 'w')
		target.write(schema_attr1)
		target.write(',')
		target.write(user_attr1)
		target.write(',')
		target.close()
		
		#Sending input_file,dec & schema_attr1 to graph1.py using command line arguments 
		command = "spark-submit graph1.py "+input_file+" "+dec+" "+schema_attr1
		os.system(command)
		
		#Getting the unique of attribute result of the given query to display1 array from temp_data2.csv file		
		with open('static/temp_files/temp_data1.csv','rb') as csvfile:
			reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
			for row in reader:
				display1.append(row[1])
				display_count.append(row[2])
		
		#Unpickling the Schema attribute list to the schema1 list
		with open("static/temp_files/temp_schema.txt","rb") as fp:
			schema1 = pickle.load(fp)
		
		#rendering graph section
		line_chart = pygal.Bar()
		line_chart.title = 'Graph analysis for '+schema1[int(schema_attr1[1:])-1]
		for i in range(1,len(display1)):		
			line_chart.add(display1[i], int(display_count[i]))
		

		graph_data = line_chart.render_data_uri()
		
		#Rendering the display1.html file and sending the arrays and graph dat to the browser , i.e..,display1.html page
		return render_template("index3.html",display1 = display1 , schema1 = schema1 , display_count = display_count , graph_data=graph_data)
	
	#If user_attr1 isn't empty
	else:
		dec='3'
		#Writing the schema_attr1 and user_attr1 values to val_temp.txt file
		target = open('static/temp_files/val_temp.txt', 'w')
		target.write(schema_attr1)
		target.write(',')
		target.write(user_attr1)
		target.write(',')
		target.close()
		#Sending the input file name and dec to graph1.py using commandline arguments
		command = "spark-submit graph1.py "+input_file+" "+dec
		os.system(command)
		
		#Initializing arrays display1 display_count arrays 
		display_count = []
		display1 = []
		
		#Inserting the count result of the query to display_count array	
		with open('static/temp_files/temp_data1.csv','rb') as csvfile:
			reader = csv.reader( csvfile , delimiter = "," , quotechar = "|")
			
			for row in reader:
				display1.append(row[1])
				display_count.append(row[2])
					
		#Unpickling the schema attribute values stored(pickled) in temp_schema.txt		
		with open("static/temp_files/temp_schema.txt","rb") as fp:
			schema1 = pickle.load(fp)
			
		print "++++++++++++++++++++++++++++++++++++++++++++++++",display_count
		len2 = len(display1) 
		len3 = len(display_count)
		
		#rendering graph section
		line_chart = pygal.Bar()
		line_chart.title = 'Graph analysis for '+schema1[int(schema_attr1[1:])-1]
		for i in range(1,len(display1)):		
			line_chart.add(display1[i], int(display_count[i]))
		

		graph_data = line_chart.render_data_uri()
		
		
		return render_template("index3.html",display1 = display1 , schema1 = schema1 , display_count = display_count,graph_data = graph_data)


#Route to display2.html page where we get extended query attribute
@app.route('/graph_analysis2')	
def graph_analysis2():
	#Getting schema_attr2 and user_attr2 from display1.html page ,i.e.,extended query attributes
	schema_attr2 = request.args.get('schema_attr2')
	user_attr2 = request.args.get('user_attr2')
	print schema_attr2,user_attr2
	#Appending the schema_attr2 and user_attr2 to val_temp.txt file
	target = open('static/temp_files/val_temp.txt', 'a')
	target.write(schema_attr2)
	target.write(',')
	target.write(user_attr2)
	target.write(',')
	target.close()
	dec='4'
	#Sending data to graph1.py file using command line arguments
	command = "spark-submit graph1.py "+input_file+" "+dec
	os.system(command)
	#Initializing arrrays to store extended query result to display1 and display_count arrays
	display_count = []
	display1 = []
	ldisplay = []
	lengths = []
	target = open("static/temp_files/len_temp.txt","r+")
	repeat = target.read()
	lengths = repeat.split(',')
	target.close()
	if lengths[2] == '4':
		empty_array_display = []
		empty_array_display1 = []
		empty_array = pd.read_csv("static/temp_files/temp_data1.csv",delimiter = ",")
		empty_array_display = empty_array.as_matrix(columns = None)
		
		row_len = len(empty_array.index)
		col_len = len(empty_array.columns)
		print "\n------------",empty_array
		print "\n-------------",empty_array_display
		print "this is within if loop"
		len1 = len(empty_array)
		line_chart = pygal.Bar()

		
		for i in range(row_len):	
			print empty_array_display[i][1]
			print empty_array_display[i][2]

		for i in range(row_len):	
			line_chart.add(empty_array_display[i][1], int(empty_array_display[i][2]))
		

		graph_data = line_chart.render_data_uri()
		
		

		return render_template("index4.html" ,row_len = row_len,col_len=col_len, empty_array_display = empty_array_display , empty_array = empty_array,graph_data=graph_data )

		
	
if __name__ == '__main__':
   app.run(debug=True)

