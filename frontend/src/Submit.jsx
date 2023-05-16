import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'

function Submit() {
    return (
        <div>Can this Work?</div>
    )
}

ReactDOM.createRoot(document.getElementById('root')).render(
    <React.StrictMode>
        <Submit />
    </React.StrictMode>,
)
