/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html"],
  theme: {
    extend: {
      colors: {
        primary: '#635642',
        secondary: '#e3e1de',
        'on-primary': '#ffffff',
        'on-secondary': '#635642',
        'newsletter-background': '#2f2e41',
        'on-newsletter': '#ffffff',
        dark: '#2f2e41',
        'buybook-primary': '#6c63ff',
        'on-buybook': '#ffffff',
        'white-background': '#f7f5fb',
      },
    },
  },
  plugins: [],
};