/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./apps/**/templates/**/*.html"],
  theme: {
    extend: {
      screens: {
        'xl2': '1100px',
      }
    },
  },
  plugins: [],
};