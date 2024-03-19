import { createRoot } from 'react-dom/client'

import Router from './router'

import 'react-complex-tree/lib/style-modern.css'
import './style.css'

// Clear out session storage.
sessionStorage.removeItem('user')

const proxyUrl = process.env.APPLICATION_URL

const root = createRoot(document.getElementById("root"))
root.render(<Router proxy={proxyUrl} />)
