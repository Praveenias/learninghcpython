# app.py

from flask import Flask, render_template,flash,send_file,redirect, request,url_for
import connexion
from flask_bootstrap import Bootstrap5
from flask_wtf import CSRFProtect
from form import *
import secrets
from request_api import api_request
import os
from config import *




app = connexion.App(__name__, specification_dir="./")
#
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =db_config()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['AUTH_TOKEN'] = ''


db.init_app(app)
ma.init_app(app)

#app.add_api("swagger.yml")


api_req = api_request()


app.secret_key = secrets.token_urlsafe(16)
authorized = False
bootstrap = Bootstrap5(app)
csrf = CSRFProtect(app)

basedir = os.path.abspath(os.path.dirname(__file__))
@app.route("/")
def home():
    return render_template("base.html")



@app.route("/api")
def api_info():
    return render_template("api.html")


@app.route("/auth_info",methods=['GET', 'POST'])
def auth_info():
  form = TokenForm()
  if form.validate_on_submit():
    api_key =  {'apiKey':form.api_key.data}
    res = api_req.get_token(api_key)
    print(res)
    if res['status_code'] == 200:
      api_token = res["data"]['token']
      print(api_token)
      app.config.update({'AUTH_TOKEN' : api_token})
      print(app.config['AUTH_TOKEN'])
      flash("successfully authenticated")
    else:
      flash('Invalid Token')
  return render_template("api/auth.html",form=form)

@app.route("/licenses")
def licenses():
    res = api_req.get_licenses()
    if res['status_code'] == 200:
        data = res["data"]
        return render_template("api/license.html",data=data,columns = license_column_name)
    else:
        print(res)
        flash(res['message']) 
        return redirect('/auth_info')
    

@app.route("/products",methods=['GET', 'POST'])
def products():
    global sub_comp_map
    if request.method == 'POST':
        q_params = {}
        if len(request.form['productName']) > 0:
          q_params['productName'] = request.form['productName']
        # if len(request.form['companyName']) > 0:
        #     q_params['subscriberId'] = sub_comp_map[request.form['companyName']]

        res = api_req.get_products(q_params)
    else:
        res = api_req.get_products()
    if res['status_code'] == 200:
        data = res["data"]
        #print(data[:5])
        sub_comp_map ={i['companyName'] : i['subscriberId'] for i in data}
        query_info = {
            "u_company_name":list(sub_comp_map.keys()),
            "u_product_name" :list(set([d['productName'] for d in data ] )),
        }
        return render_template("api/products.html",data=data,columns = product_column_name,query_info=query_info)
    else:
        flash(res['message']) 
        return redirect('/auth_info')
    

@app.route("/subscribers",methods=['GET', 'POST'])
def subscribers():

    if request.method == 'POST':
        query_parameters = ['companyName','siteName','divisionName']
        q_params = {}
        for data in query_parameters:
          if len(request.form[data]) > 0:
            q_params[data] = request.form[data]
        res = api_req.get_subscribers(q_params)
    else:
        res = api_req.get_subscribers()
    if res['status_code'] == 200:
        data = res["data"]
        query_info = {
            "u_company_name":list(set([d['companyName'] for d in data ] )),
            "u_site_name" :list(set([d['siteName'] for d in data ] )),
            "u_division_name":list(set([d['divisionName'] for d in data ] )),
        }
        return render_template("api/subscribers.html",data=data,columns = subscriber_column_names,query_info=query_info)
    else:

        flash(res['message']) 
        return redirect('/auth_info')
    
    

@app.route("/boms",methods=['GET', 'POST'])
def boms():
    #res = requests.get(api_url+'boms',headers=headers)
    
    if request.method == 'POST':
        query_parameters = ['bomName']
        q_params = {}
        for data in query_parameters:
          if len(request.form[data]) > 0:
            q_params[data] = request.form[data]
        res = api_req.get_boms(q_params)
    else:
        res = api_req.get_boms()
    
    if res['status_code'] == 200:
        data = res["data"]
        query_info = {
            "u_bom_name":list(set([d['bomName'] for d in data ] )),
        }
        return render_template("api/boms.html",data=data,columns = boms_column_name,query_info=query_info)
    else:
        flash(res['message'])
        return redirect('/auth_info')
    
@app.route("/bom-status/<bom_id>?/<rev>?",methods=['GET', 'POST'])
@app.route("/bom-status/<bom_id>?",methods=['GET', 'POST'])
@app.route("/bom-status/",methods=['POST'],defaults={'bom_id': None,'rev':None})
def bom_status(bom_id='',rev=''):
  query_info = {
        'bomId':'',
        'revision':'',
        'requestType':["part_lifecycle_status","compliance_status"],
        'regulationType':["EU-RoHS","EU-REACH (SVHC List)","EU-REACH (Restricted List)","EU-REACH (Authorization List)","California Prop 65","TSCA"],
        "returnType":["list","summary"]
  }
  if request.method == 'GET':  
    query_info.update({
        'bomId':bom_id,
        'revision':rev,
   })
    return render_template("api/bom_status.html",query_info=query_info)
  if request.method == 'POST':
    IS_BOM= False
    if 'isbom' in request.form:
      IS_BOM=True
    bom_id = request.form['bom_id']
    rev = request.form['revision']
    if IS_BOM:
        q_params = {
            'bomId':request.form['bom_id'],
            'revision':request.form['revision'],
            'requestType':request.form['requestType'].replace(" ","_"),
            'regulationType':request.form['regulationType'],
            'returnType':request.form['returnType'],
            'searchBy':'bom'
        }
    else:
       q_params = {
            'subscriberId':request.form['bom_id'],
            'revision':request.form['revision'],
            'requestType':request.form['requestType'].replace(" ","_"),
            'regulationType':request.form['regulationType'],
            'returnType':request.form['returnType'],
            'searchBy':'subscriber'
        }
    query_info.update({
        'bomId':request.form['bom_id'],
        'revision':request.form['revision'],
    })
    res = api_req.get_bom_status(q_params)

    if res['status_code'] == 200:
        data = res["data"]
        summary_data = {}
        list_data = {}
        if q_params['returnType'] == 'summary':
          summary_data = res['data']
        if q_params['returnType'] == 'list':
          for key, val in data.items():
            list_data[key]=[]
            if len(val) > 0:
              {list_data[key].append(val1) for val1 in val.values()}
    
        return render_template("api/bom_status.html",query_info=query_info,summary_data=summary_data,list_data=list_data)
    else:
        flash(res['message'])
        return redirect('/auth_info')

@app.route("/regulation",methods=['GET', 'POST'])
def regulation():
    #res = requests.get(api_url+'boms',headers=headers)
    
    if request.method == 'POST':
        query_parameters = ['regulationType','regulationName','directiveName']
        q_params = {}
        for data in query_parameters:
          if len(request.form[data]) > 0:
            q_params[data] = request.form[data]
        res = api_req.get_regulations(q_params)
    else:
        res = api_req.get_regulations()
    
    if res['status_code'] == 200:
        data = res["data"]
        query_info = {
            "u_reg_type":list(set([d['regulationType'] for d in data ] )),
            "u_reg_name":list(set([d['regulationName'] for d in data ] )),
            "u_dir_name":list(set([d['directiveName'] for d in data ] )),
        }
        return render_template("api/regulation.html",data=data,columns = regulation_column_name,query_info=query_info)
    else:
        flash(res['message'])
        return redirect('/auth_info')
    
@app.route("/subtances",methods=['GET', 'POST'])
def subtances():
    #res = requests.get(api_url+'boms',headers=headers)
    
    if request.method == 'POST':
        query_parameters = ['casNumber','substanceName']
        q_params = {}
        for data in query_parameters:
          if len(request.form[data]) > 0:
            q_params[data] = request.form[data]
        res = api_req.get_substances(q_params)
    else:
        res = api_req.get_substances()
    
    if res['status_code'] == 200:
        data = res["data"]
        query_info = {
            "u_cas_num":list(set([d['casNumber'] for d in data ] )),
            "u_sub_name":list(set([d['substanceName'] for d in data ] )),
        }
        return render_template("api/subtances.html",data=data,columns = subtances_column_name,query_info=query_info)
    else:
        flash(res['message'])
        return redirect('/auth_info')  
    

@app.route("/manufacturer",methods=['GET', 'POST'])
def manufacturer():
    #res = requests.get(api_url+'boms',headers=headers)
    
    if request.method == 'POST':
        query_parameters = ['manufacturerName','returnType']
        q_params = {}
        for data in query_parameters:
          if len(request.form[data]) > 0:
            q_params[data] = request.form[data]
        res = api_req.get_manufacturer(q_params)
    else:
        q_params = {'returnType':'all','returnData':'csv'}
        res = api_req.get_manufacturer(q_params)
    
    if res['status_code'] == 200:
        data = []
        man_data = {
           'file_link':res["data"]["file"]
        }
        return render_template("api/manufacturer.html",data=data,man_data=man_data)
    else:
        flash(res['message'])
        return redirect('/auth_info')  
   

@app.route('/download_file/<path:filename>')
def download_file(file_path):
  path = "simple.docx"
  return send_file(path, as_attachment=True)

@app.route('/file_upload')
def file_upload():
    return render_template('file_upload.html')



if __name__ == "__main__":
    app.run(host="localhost", port=8001, debug=True)