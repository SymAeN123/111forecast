import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

function Home() {
    return (
        <div>Start Workin</div>
    )
}

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Home />
    </React.StrictMode>,
)
