const http = require('http');  // Importer le module HTTP natif de Node.js
const server = http.createServer((req, res) => { // Créer un serveur HTTP
res.write('Bonjour tout le monde !');  // Envoyer une réponse au client
res.end();
});
server.listen(4000, () => { // Lancer le serveur sur le port 4000
  console.log('Server is running on port 4000');
});
