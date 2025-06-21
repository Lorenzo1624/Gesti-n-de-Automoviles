module.exports = {
    content: [
        "../../templates/**/*.html",
    ],
  safelist: [
    {
      pattern: /(bg|text|border)-(red|yellow|blue|green|indigo|purple|pink|gray)-(100|200|300|400|500|600|700|800|900)/, // Todos los colores y variantes
    },
  ],
    theme: {
        extend: {},
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}