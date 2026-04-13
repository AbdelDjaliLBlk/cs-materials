<?php
session_start();
if (!isset($_SESSION["connecte"])) {
    header("Location: formulaire.php");
    exit();
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Résultat Candidature</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 50px; background-color: #f2f2f2; }
        h2 { color: #333; }
        table { border-collapse: collapse; width: 60%; background-color: white; box-shadow: 0px 0px 10px rgba(0,0,0,0.1); }
        th { background-color: #db0f0f; color: white; padding: 12px; text-align: left; width: 30%; }
        td { padding: 12px; border-bottom: 1px solid #ddd; }
        tr:hover { background-color: #f5f5f5; }
        .password { letter-spacing: 3px; color: #999; }
        a {
            display: inline;              /* no block/button behavior */
            margin-top: 0;
            padding: 0;
            background: none;
            color: #0e6111;               /* keep your green */
            text-decoration: none;        /* no underline by default */
            border-radius: 0;
            font-weight: 500;
        }

        a:hover {
            color: #45a049;
            text-decoration: underline;   /* underline on hover */
        }
    </style>
</head>
<body>

<h2>Informations du candidat</h2>

<table>
    <tr>
        <th>Nom du Champ Saisie</th>
        <th>Valeur de la saisie</th>
    </tr>
    <tr>
        <td><strong>Nom</strong></td>
        <td><?= htmlspecialchars($_SESSION["nom"]) ?></td>
    </tr>
    <tr>
        <td><strong>Prénom</strong></td>
        <td><?= htmlspecialchars($_SESSION["prenom"]) ?></td>
    </tr>
    <tr>
        <td><strong>Login</strong></td>
        <td><?= htmlspecialchars($_SESSION["login"]) ?></td>
    </tr>
    <tr>
        <td><strong>Mot de passe</strong></td>
        <td><span class="password">••••••••</span></td>
    </tr>
    <tr>
        <td><strong>Lettre de Motivation</strong></td>
        <td><?= htmlspecialchars($_SESSION["LDM"]) ?></td>
    </tr>
    <?php if (!empty($_SESSION["cv"])): ?>
    <tr>
        <td><strong>CV</strong></td>
        <td>
    <a href="<?= htmlspecialchars($_SESSION["cv"]) ?>" download>
        Télécharger le CV
    </a>
</td>
    </tr>
    <?php endif; ?>
</table>

<a href="formulaire.php" style="text-align: center;">↩ Retour</a>

<?php session_destroy(); ?>

</body>
</html>