import axios from 'axios'

export default {
  install: (app, options) => {
    const http = axios.create({
      baseURL: "http://localhost:8000"
    })
    app.provide('http', http)
    // store.
  }
}