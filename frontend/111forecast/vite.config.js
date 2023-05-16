import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    build: {
        outDir: '../static',
    },
    proxy: {
    '/query': {
            target: 'https://ec2-34-230-20-67.compute-1.amazonaws.com/',
            changeOrigin: true,
            secure: false,
            ws: true
        }
    }
})
