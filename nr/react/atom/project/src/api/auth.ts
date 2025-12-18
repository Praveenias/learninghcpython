import { LoginCredentials } from '../types';
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api/v1';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
  },
  withCredentials: false, // Enable credentials for session management
});

// Axios interceptor to handle response errors
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response) {
      // Server responded with error status
      throw new Error(error.response.data.message || 'An error occurred during the request');
    } else if (error.request) {
      // Request made but no response received
      throw new Error('No response received from server');
    } else {
      // Error in request setup
      throw new Error('Error setting up the request');
    }
  }
);

export const setAuthToken = (token: string | null) => {
  if (token) {
    api.defaults.headers.common['Authorization'] = `Bearer ${token}`;
    // Optionally store token in localStorage
    localStorage.setItem('authToken', token);
  } else {
    delete api.defaults.headers.common['Authorization'];
    localStorage.removeItem('authToken');
  }
};

// Initialize token from localStorage if exists
const storedToken = localStorage.getItem('authToken');
if (storedToken) {
  setAuthToken(storedToken);
}

export async function loginUser({ email, password }: LoginCredentials) {
  try {
    const response = await api.post('/login', {
      email,
      password,
    });

    // Axios automatically throws for non-2xx responses
    // and transforms the response to JSON
    const { token, user } = response.data.data;
    
    // Set the auth token for subsequent requests
    setAuthToken(token);

    return {
      token,
      user,
    };
  } catch (error) {
    if (error instanceof Error) {
      throw error;
    }
    throw new Error('An unexpected error occurred during login');
  }
}

export async function logoutUser() {
  try {
    await api.post('/logout');
    setAuthToken(null);
  } catch (error) {
    console.error('Logout failed:', error);
    // Still remove token even if logout request fails
    setAuthToken(null);
  }
}

//customer releated api

export async function getCustomernameFromLevel(level:string) {
  try {
    let res;
    res = await api.get('/getCustomerFromLevel', {
      params: {
        level: level,
      }
    });
    return res.data
  } catch (error) {

  }
}

export async function getProductNameFromCustomer(customerId:string) {
  try {
    let res;
    res = await api.get('/getProductFromCustomer', {
      params: {
        customerId: customerId,
      }
    });
    return res.data
  } catch (error) {

  }
}

export async function getChartData(ProductIds:string) {
  try {
    let res;
    res = await api.get('/obsconsildatedreport', {
      params: {
        product_ids: ProductIds,
        responseType:'count'
      }
    });
    // console.log(res);
    
    return res.data
  } catch (error) {
    console.log(error);
    return null;
    

  }
}
// Export the api instance for use in other parts of the application
export default api;