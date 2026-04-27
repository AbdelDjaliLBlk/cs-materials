<?php
$conn = new mysqli("localhost", "root", "", "badr", 3306);

if ($conn->connect_error) {
    die("Connexion échouée : " . $conn->connect_error);
}

$nom    = $_POST['nom'];
$passwd = $_POST['passwd'];

$stmt = $conn->prepare("SELECT nom, solde, passwd FROM banque WHERE nom = ?");
$stmt->bind_param("s", $nom);
$stmt->execute();
$result = $stmt->get_result();

if ($result->num_rows === 1) {
    $row = $result->fetch_assoc();

    // نقارن كلمة المرور مع الـ hash باستخدام password_verify
    if (password_verify($passwd, $row['passwd'])) {
        echo "<h1>Bienvenue, " . htmlspecialchars($row['nom']) . " !</h1>";
        echo "<h1>Votre solde est de : " . htmlspecialchars($row['solde']) . " DA</h1>";
    } else {
        echo "<h1>Échec de l'authentification</h1>";
        echo "<p>Mot de passe incorrect.</p>";
    }
} else {
    echo "<h1>Échec de l'authentification</h1>";
    echo "<p>Nom introuvable.</p>";
}

$stmt->close();
$conn->close();
?>