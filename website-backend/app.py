# importing packages
from flask import Flask ,render_template, redirect, url_for, session, request, logging
import requests
import json
import dbquery
import numpy
app = Flask(__name__) #app initialisation

@app.route('/', methods=['GET','POST']) #landing page intent
def home():
    sql = "SELECT TIME_STAMP FROM DATA WHERE USERID =1 AND DATA_DATE = CURDATE();"
    data = dbquery.fetchall(sql)
    List = list()
    #converting from tuple to string
    for t in data:
        List.append(int(t[0]))
    List.sort()
    data = {x:List.count(x) for x in List}
    print(data)
    
    return render_template("index.html",data=data) #display the html template



#method to insert data to db
@app.route('/insert_to_db', methods=['POST']) #landing page intent
def data_from_model():
    if request.method == 'POST':
        x= request.get_json()
        time = x['time']
        userid =x['userid']
        sql="INSERT INTO DATA VALUES (%s ,NOW(),%s);"%(userid,time)
        dbquery.inserttodb(sql)
        return "200"
    return "Error"






if __name__=='__main__':
	app.run(debug=True,host="0.0.0.0",port=8000) 
    #use threaded=True instead of debug=True for production
    # use port =80 for using the http port



#sample code for form data recieve
# request.form['name']
# Sample Code for JSON send data to api

#url = 'URL_FOR_API'
#data = {'TimeIndex':time1 ,'Name':name,'PhoneNumber':phone}
#headers = {'content-type': 'application/json'}
#r=requests.post(url, data=json.dumps(data), headers=headers)
#data = r.json()
#print(data)


#Sample code for JSON recieve data from API

#url = 'URL_FOR_API'
#headers = {'content-type': 'application/json'}
#r=requests.get(url, headers=headers)
#data = r.json()
#count = data['Count']