// src/api.js
import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // Your Django backend URL
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  },
});



export default api;