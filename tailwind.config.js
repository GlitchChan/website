/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.jinja2"],
  daisyui: {
    themes: [
      {
        rosepine: {
          "primary": "#c4a7e7",
          "secondary": "#ea9a97",
          "accent": "#c4a7e7",
          "neutral": "#2a273f",
          "base-100": "#232136",
          "info": "#3e8fb0",
          "success": "#9ccfd8",
          "warning": "#f6c177",
          "error": "#eb6f92",
        },
      },
    ],
  },
  plugins: [require('daisyui')],
  theme: {
    colors: {
      'midnight': {
        100: '#1E1928',
        200: '#231E2d',
        300: '#1a1621',
      },
      'baelz': {
        100: '#dd2a62',
        200: '#aa204b',
        300: '#5d1129',
      },
    },
  },
}
