/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/*.jinja2"],
  daisyui: {
      themes: [
        {
          main: {
            "primary": '#761D3A',
            "secondary": "#D926A9",
            "accent": "#1FB2A6",
            "neutral": "#191D24",
            "base-100": "#2A303C",
            "info": "#3ABFF8",
            "success": "#36D399",
            "warning": "#FBBD23",
            "error": "#f43f5e",
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
