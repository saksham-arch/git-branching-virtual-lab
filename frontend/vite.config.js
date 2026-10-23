import {defineConfig} from 'vite';
export default defineConfig({base:'/static/react/', build:{manifest:true, rollupOptions:{output:{entryFileNames:'app.js',chunkFileNames:'chunks/[name]-[hash].js'}}}});
