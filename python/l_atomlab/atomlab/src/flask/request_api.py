
import requests as req

class api_request:
  def __init__(self) -> None:
    self.base_url = 'http://127.0.0.1:8000/api/v1/'
    # self.authToken:str = '29|o5KSvdDSYkzqwevUU20gGU5fG6irLGiaDEmQV1pd',
    # self.headers:dict = {
    #     'Authorization': 'Bearer ' + self.authToken,
    #     'Content-Type': 'application/json'
    # }

  def get_request(self,routename:str,params:dict={})->dict:
    #auth_token = '29|o5KSvdDSYkzqwevUU20gGU5fG6irLGiaDEmQV1pd'
    auth_token = ''
    headers:dict = {
        'Authorization': 'Bearer ' + '',
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }
    out = {
      'status_code':'',
      'status':'',
      'data':[],
      'message':''
    }
    try:
      res = req.get(self.base_url+routename,headers=headers,params=params)
      if res.status_code == 200:
        out = {
            'status_code':res.status_code,
            'status':'success',
            'data':res.json()['data'],
            'message':res.json()['message']
        }   
      if res.status_code == 401:
        out = {
            'status_code':401,
            'status':'failure',
            'message':'UNauthorized access'
        }    
      if res.status_code == 500:
        out = {
            'status_code':500,
            'status':'failure',
            'message':'Internal server error'
        }
      if res.status_code == 404:
        out = {
            'status_code':404,
            'status':'failure',
            'message':'Page Not found'
        }
      if res.status_code == 422:
        out = {
            'status_code':422,
            'status':'failure',
            'message':res.json()['message']
        }
    except req.exceptions.ConnectionError:
      out = {
            'status_code':400,
            'status':'failure',
            'message':'Failed to establish a connection'
        }
      
    except Exception as e:
      #print(res)
      out = {
            'status_code':500,
            'status':'failure',
            'message':e
        }

    return out
  
  def get_token(self,q_params:dict = {})->dict:
    return self.get_request('access-token',q_params)

  def get_boms(self,q_params:dict = {})->dict:
    return self.get_request('boms',q_params)
  
  def get_licenses(self,q_params:dict = {})->dict:
    return self.get_request('licenses',q_params)
  
  def get_subscribers(self,q_params:dict = {})->dict:
    return self.get_request('subscribers',q_params)
  
  def get_products(self,q_params:dict = {})->dict:
    return self.get_request('products',q_params)
  
  def get_substances(self,q_params:dict = {})->dict:
    return self.get_request('substances',q_params)
  
  def get_regulations(self,q_params:dict = {})->dict:
    return self.get_request('regulations',q_params)
  
  def get_manufacturer(self,q_params:dict = {})->dict:
    return self.get_request('manufacturers',q_params)
  
  def get_bom_status(self,q_params:dict = {})->dict:
    return self.get_request('boms/compliance-status',q_params)
  


if __name__ == '__main__':
  api = api_request()
  a = api.get_boms()
  #print(a)