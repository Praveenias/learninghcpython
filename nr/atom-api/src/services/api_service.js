import axios from "axios";

const headers = {
  "Content-Type": "application/json",
  "Accept": "application/json",
};

const BASE_URL = 'http://127.0.0.1:8000'; // Replace with your API base URL

const apiService = {
  async get(endpoint,params={}) {
   // console.log(params);
    try {
      const response = await axios.get(`${BASE_URL}/${endpoint}`,{params},headers);
      return response.data;
    } catch (error) {
      console.error('API GET request failed:', error);
      throw error;
    }
  },

  async post(endpoint, payload) {
    try {
      const response = await axios.post(`${BASE_URL}/${endpoint}`, payload,headers);
      return response.data;
    } catch (error) {
      console.error('API POST request failed:', error);
      throw error;
    }
  },

  // Add more API methods as needed
};

export default apiService;
