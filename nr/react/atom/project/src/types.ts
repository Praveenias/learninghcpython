export interface LoginCredentials {
  email: string;
  password: string;
}

export interface LoginError extends Error {
  message: string;
}

export interface User {
  id: string;
  email: string;
  name: string;
}