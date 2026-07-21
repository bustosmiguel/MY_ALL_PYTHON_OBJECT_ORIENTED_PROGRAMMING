// %% APP.JS - EL PUENTE DE REGRESSIONDATA
const os = require('os'); // Importamos el módulo de Sistema Operativo

console.log("--- BIENVENIDO AL NODO DE CONTROL ---");
console.log(`Cliente: Miguel Bustos`);
console.log(`Sistema Operativo: ${os.type()} ${os.release()}`);
console.log(`Memoria Libre: ${(os.freemem() / 1024 / 1024).toFixed(2)} MB`);

// Simulación de una tarea de servidor
setTimeout(() => {
    console.log("🚀 Node.js está listo para recibir datos de Python...");
}, 2000);