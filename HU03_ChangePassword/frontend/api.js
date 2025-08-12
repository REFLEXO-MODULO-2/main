import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api/',  // Cambia si usas otro puerto
headers: {
    'Content-Type': 'application/json',
},
  withCredentials: false // Cambia a true si necesitas manejar sesiones o cookies
});

export default api;
