<?php
$conn = new mysqli("localhost", "root", "", "badr", 3306); // Connexion à la base de données
if ($conn->connect_error) {     
    die("Connexion échouée : " . $conn->connect_error);
}

$nom = $_POST['nom']; // Récupérer les données du formulaire
$passwd = $_POST['passwd'];

// VULNÉRABLE : Requête SQL construite directement avec les entrées utilisateur
$query = "SELECT nom, solde FROM banquebis WHERE nom = '$nom' AND passwd = '$passwd'";

$result = $conn->query($query);

if ($result->num_rows > 0) {    // Vérifier si un utilisateur correspond
    $row = $result->fetch_assoc(); // Récupérer les données du client
    echo "<h1>Bienvenue, " . htmlspecialchars($row['nom']) . "</h1>";
    echo "<h1>Votre solde est de : " . htmlspecialchars($row['solde']). "</h1>";
} else {
    echo "<h1>&Eacute;chec de l'authentification</h1>";
    echo "<h1>Nom ou mot de passe incorrect.</h1>";
}

// Fermer la connexion
$conn->close();



// Pourquoi l’authentification est cassée ?
// L’authentification est cassée parce que la requête SQL est construite directement
// avec les entrées de l’utilisateur sans aucune validation.
// L’utilisateur peut injecter du code SQL (ex: ' OR 1=1 #) qui rend la condition toujours vraie.


// Comment appelle-t-on cette attaque ?
// Cette attaque s’appelle : SQL Injection.


// Que peut faire un attaquant avec cette faille ?
// Un attaquant peut :
// - Se connecter sans mot de passe
// - Accéder aux données sensibles (ex: soldes)
// - Modifier ou supprimer des données
// - Endommager la base de données


// Pourquoi seul le premier utilisateur est affiché ?
// Parce que le code utilise fetch_assoc() une seule fois,
// donc il récupère فقط la première ligne du résultat,
// même si plusieurs lignes correspondent à la requête.


// Les requêtes préparées empêchent-elles l’attaque ? Pourquoi ?
// Oui, les requêtes préparées empêchent cette attaque.
// Parce qu’elles séparent la requête SQL (code) des données utilisateur.
// Les entrées sont traitées comme des valeurs simples (pas du code SQL),
// donc même si l’utilisateur écrit (' OR 1=1 #), ça sera considéré comme texte
// et non exécuté comme une commande SQL.

?>

