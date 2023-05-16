import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [react()],
    build: {
        outDir: '../backend/public_backend/public/',
        rollupOptions: {
            output: {
                entryFileNames: `assets/[name].js`,
                chunkFileNames: `assets/[name].js`,
                assetFileNames: `assets/[name].[ext]`
            },
            input: {
                main: resolve(__dirname, 'index.html'),
                submit: resolve(__dirname, 'submit/index.html')
            }
        }
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
