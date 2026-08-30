// %% 
// LECTOR.JS - EL SERVIDOR WEB DE REGRESSIONDATA
// Python escribe y Node.js lee. Ese archivo .json es el puente de comunicación entre ambos.
// ¿Cómo abro el web?, necesitamos transformar ese script de Node (lector.js) en 
// un Servidor Web Real. Actualmente, el script corre una vez y se cierra; para la web, 
// necesitamos que se quede "escuchando" en un puerto (como el 3000).
// Abre el Web: Abre tu navegador favorito y escribe en la barra de direcciones: http://localhost:3000
// Ejecuta Python para crear los datos

const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    // RUTA 1: La página principal (HTML)
    if (req.url === '/') {
        fs.readFile('index.html', (err, content) => {
            res.writeHead(200, { 'Content-Type': 'text/html' });
            res.end(content);
        });
    } 
    // RUTA 2: Los datos (JSON) que pide el HTML con fetch
    else if (req.url === '/api/data') {
        fs.readFile('data_bridge.json', (err, data) => {
            res.writeHead(200, { 'Content-Type': 'application/json' });
            res.end(data);
        });
    }
});

server.listen(3000, () => {
    console.log("🚀 Frontend visual listo en http://localhost:3000");
});