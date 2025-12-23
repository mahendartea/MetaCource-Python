import { defineConfig } from 'vitepress'

export default defineConfig({
    title: "Gua Ilmu Pemrograman",
    description: "Panduan Lengkap Belajar Python dari Dasar hingga Mahir",
    lang: 'id-ID',
    base: '/MetaCource-Python/', // Penting untuk GitHub Pages! Sesuaikan dengan nama repo.
    ignoreDeadLinks: true,



    themeConfig: {
        logo: '/logo.png', // Ganti ke logo baru yang akan kita buat
        siteTitle: 'Gua Ilmu Pemrograman',

        nav: [
            { text: 'Home', link: '/' },
            { text: 'Mulai Belajar', link: '/Pendahuluan' },
            { text: 'Tentang', link: 'https://github.com/mahendartea/MetaCource-BasicPython' }
        ],

        sidebar: [
            {
                text: 'Dasar Pemrograman',
                collapsed: false,
                items: [
                    { text: '0. Pendahuluan', link: '/Pendahuluan' },
                    { text: '1. Variable', link: '/Variable' },
                    { text: '2. Input & Output', link: '/InputOutput' },
                    { text: '3. Tipe Data', link: '/DataType' },
                    { text: '4. String Handling', link: '/StringHandling' },
                    { text: '5. Operasi', link: '/Operation' },
                    { text: '6. Percabangan', link: '/Conditional' },
                    { text: '7. Perulangan', link: '/Looping' },
                    { text: '8. Fungsi', link: '/Function' },
                ]
            },
            {
                text: 'Menengah (Advance)',
                collapsed: false,
                items: [
                    { text: '9. Module', link: '/Module' },
                    { text: '10. Datetime', link: '/PythonDatetime' },
                    { text: '11. Regex', link: '/PythonRegex' },
                    { text: '12. PIP', link: '/PythonPIP' },
                    { text: '13. JSON', link: '/PythonJson' },
                    { text: '14. CSV', link: '/PythonCSV' },
                    { text: '15. Try & Except', link: '/PythonTryExcept' },
                ]
            },
            {
                text: 'Database Engineering',
                collapsed: false,
                items: [
                    { text: '16. Database SQLite', link: '/Database' },
                    { text: '17. Database MySQL', link: '/DatabaseMySQL' },
                    { text: '18. Module Numpy', link: '/ModuleNumpy' },
                ]
            }
        ],



        socialLinks: [
            { icon: 'github', link: 'https://github.com/mahendartea' }
        ],

        footer: {
            message: 'Ditulis dan dikembangkan oleh Mahendar Dwi Payana.',
            copyright: 'Copyright © 2025 Gua Ilmu Pemrograman'
        },


        search: {
            provider: 'local'
        }
    }
})
