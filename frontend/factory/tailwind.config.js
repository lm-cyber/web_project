/** @type {import('tailwindcss').Config} */
const defaultTheme = require('tailwindcss/defaultTheme');

export default {
    content: ['./index.html', './src/**/*.{js,ts,jsx,tsx}'],
    theme: {
        container: {
            center: true,
        },
        colors: {
            white: '#FFF',
            darkBlue: '#000D53',
            black: '#000',
            lightGray: '#F0F0F0',
            gray: '#9F9F9F',
        },
        fontFamily: {
            sans: [['"Manrope Variable"', ...defaultTheme.fontFamily.sans]],
        },
        extend: {},
    },
    plugins: [],
};
