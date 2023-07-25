/**
 * plugins/index.js
 *
 * Automatically included in `./src/main.js`
 */

// Plugins
import { loadFonts } from './webfontloader'
import vuetify from './vuetify'
import axios from './axios'
import pinia from '../store'
import router from '../router'

export function registerPlugins (app) {
  loadFonts()
  app
    .use(axios)
    .use(vuetify)
    .use(router)
    .use(pinia)
}
