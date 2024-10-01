/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './static/**/*.css',
    './static/**/*.js',
    "./node_modules/flowbite/**/*.js",
    // Altri percorsi se necessari
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

