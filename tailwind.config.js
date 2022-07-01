/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.jinja2"],
  theme: {},
  plugins: [require('daisyui')],
  theme: {
    colors: {
      'midnight': {
        100: '#1e1928',
        200: '#231e2d',
      },
      'baelz': {
        100: '#dd2a62',
        200: '#aa204b',
        300: '#5d1129',
      },
    },
  },
}
