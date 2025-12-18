
import pyodide_http
pyodide_http.patch_requests()
import requests as req


class api_request:
  def __init__(self) -> None:
    self.base_url = 'http://127.0.0.1:8000/api/v1/'
    self.authToken = '1|akFo3mhPxK3uP6M6cMkKIx0tryIFbm3cAbC1z0U8'
    self.headers = {
        'Authorization': 'Bearer ' + self.authToken,
        'Content-Type': 'application/json'
    }

  def get_request(self,routename:str)->dict:
    out = {
      'status_code':'',
      'status':'',
      'data':[],
      'message':''
    }
    #res = req.get(self.base_url+routename,headers=self.headers)
    #print(res)
    try:
      res = req.get(self.base_url+routename,headers=self.headers)
      if res.status_code == 200:
        out = {
            'status_code':res.status_code,
            'status':res.json()['success'],
            'data':res.json()['data'],
            'message':res.json()['message']
        }       
      if res.status_code == 500:
        out = {
            'status_code':500,
            'status':'failure',
            'message':'Internal server error'
        }
      return out
    except req.exceptions.ConnectionError:
      out = {
            'status_code':400,
            'status':'failure',
            'message':'Failed to establish a connection'
        }
    return out

  def get_boms(self)->dict:
    return self.get_request('boms')
  
  def get_licenses(self)->dict:
    return self.get_request('licenses')
  
  def get_subscribers(self)->dict:
    return self.get_request('subscribers')
  
  def get_products(self)->dict:
    return self.get_request('products')
  
  def get_substances(self)->dict:
    return self.get_request('substances')
  

if __name__ == '__main__':
  api = api_request()
  print(api.get_boms())