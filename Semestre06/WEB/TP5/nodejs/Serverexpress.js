const express = require('express');  
const app = express();
app.use(express.static(__dirname));
app.get('/calcule', (req, res) => {
     const n = req.query.n;  
     const resultat = n * n; 
   setTimeout(() => {
        res.send(`Le serveur a reçu n=${n}. Voici votre résultat : ${resultat}.`);
    }, 3000);
});
// Démarrer le serveur sur le port 5000
const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Serveur démarré sur http://localhost:${PORT}`);
});
