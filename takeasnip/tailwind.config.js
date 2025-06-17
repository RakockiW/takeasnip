/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './templates/*.html',
      './**/templates/**/*.html'
  ],
  theme: {
    extend: {
        fontFamily: {
            mono: ['"JetBrains Mono"', 'monospace']
        }
    },
  },
  plugins: [],
}

