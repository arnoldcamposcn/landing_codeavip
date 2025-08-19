/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../templates/**/*.html',
    '../../templates/**/*.html',
    '../../**/templates/**/*.html',
    '../../main/templates/**/*.html',
    '../../packages/templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        'azul-vip': '#0068FF',
      },
    },
  },
  daisyui: {
    themes: ["light", "dark"],
  },
  plugins: [
    require('daisyui'),
  ],
}