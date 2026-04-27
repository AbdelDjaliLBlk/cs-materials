<?php
$conn = new mysqli("localhost", "root", "", "badr", 3306); 

// Préparer la requête SQL
$stmt = $conn->prepare("INSERT INTO banque (nom, solde, passwd) VALUES (?, ?, ?)");

// Liste des utilisateurs
$users = [
    ['Ali', 1500.75, password_hash('123', PASSWORD_DEFAULT)],
    ['Sara', 2500.00, password_hash('456', PASSWORD_DEFAULT)],
    ['Omar', 320.50, password_hash('2023', PASSWORD_DEFAULT)],
    ['Nadia', 870.25, password_hash('348', PASSWORD_DEFAULT)]
];

foreach ($users as $user) {
    $stmt->execute([$user[0], $user[1], $user[2]]);
}

echo "Utilisateurs insérés avec succès !";


// password_hash('123', PASSWORD_DEFAULT)
// Cette fonction permet de hacher (chiffrer de manière sécurisée) le mot de passe '123' 
// avant de le stocker dans la base de données.

// Rôle des paramètres :
// '123' : le mot de passe en clair saisi par l'utilisateur
// PASSWORD_DEFAULT : indique à PHP d'utiliser le meilleur algorithme disponible pour le hachage

// Algorithme utilisé :
// Actuellement, PHP utilise l'algorithme BCRYPT pour le hachage (peut changer dans le futur)
?>

