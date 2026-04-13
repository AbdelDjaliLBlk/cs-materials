<?php
session_start(); 
if ($_SERVER["REQUEST_METHOD"] == "POST" && !empty($_POST["nom"])) {
    $nom = htmlspecialchars($_POST["nom"]);
    $_SESSION["user"] = $nom;
    setcookie("informatique", $nom, time() + 60);
   header("Location: session.php");
   exit();
}
$nomSession = isset($_SESSION["user"]) ? $_SESSION["user"] : null;
$nomCookie = isset($_COOKIE["informatique"]) ? $_COOKIE["informatique"] : null;
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestion des Sessions et Cookies</title>
</head>
<body>
<h2>Connexion</h2>
<?php if (!$nomSession) { ?>
    <form method="POST">
        <label>Nom :</label>
        <input type="text" name="nom" required>
        <button type="submit">Se connecter</button>
    </form>
<?php } else { ?> 
    <p>Bienvenue, <strong><?php echo $nomSession; ?></strong></p>
    <p>Stocké dans le cookie : <?php echo $_COOKIE["informatique"] ?? 'Non défini'; ?></p>
    <p>ID de session (PHPSESSID) : <strong><?php echo session_id(); ?></strong></p>
    <a href="logout.php">Se déconnecter</a>
<?php } ?> 
</body>
</html>