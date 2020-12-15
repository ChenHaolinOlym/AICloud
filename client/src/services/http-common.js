import axios from "axios";

export default axios.create({
  // baseURL: "http://localhost:5000",
  baseURL: "http://10.30.6.52:5000",
  headers: {
    "Content-type": "application/json"
  }
});
