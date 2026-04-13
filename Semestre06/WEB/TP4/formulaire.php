<?php
session_start();

$erreur = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $login = $_POST["login"];
    $password = $_POST["password"];

    if ($login == "djalil" && $password == "00000") {
        $_SESSION["connecte"] = true;
        $_SESSION["nom"]    = $_POST["nom"];
        $_SESSION["prenom"] = $_POST["prenom"];
        $_SESSION["login"]  = $_POST["login"];
        $_SESSION["LDM"]    = $_POST["LDM"];

        if (!empty($_FILES["cv"]["name"])) {
            $destination = "telechar/" . $_FILES["cv"]["name"];
            if (move_uploaded_file($_FILES["cv"]["tmp_name"], $destination)) {
                $_SESSION["cv"] = $destination;
            } else {
                $_SESSION["cv"] = null;
            }
        }

        header("Location: affichage.php");
        exit();
    } else {
        $erreur = "Login ou mot de passe incorrect !";
    }
}
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <title>Candidature</title>

    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
        }

        form {
            width: 500px;
            margin: 60px auto;
            padding: 20px;
            background-color: white;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        h2 {
            text-align: center;
            color: #1a0f57;
        }

        label {
            display: block;
            margin-top: 10px;
            font-weight: bold;
            color: #050653
        }

        input, textarea {
            width: 100%;
            padding: 8px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="file"] {
            border: none;
        }

        button {
            display: block;
            margin: 20px auto;
            padding: 10px 20px;
            background-color: #333;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button:hover {
            background-color: #555;
        }

        .error {
            color: red;
            text-align: center;
        }
    </style>
</head>

<body>

    
    <?php if ($erreur): ?>
        <p class="error"><?= htmlspecialchars($erreur) ?></p>
        <?php endif; ?>
        
<form method="post" action="" enctype="multipart/form-data">
    <h2>Formulaire de Candidature</h2>

    <label>Entrez votre Nom: </label>
    <input type="text" name="nom" value="<?= htmlspecialchars($_POST['nom'] ?? '') ?>" required>

    <label>Entrez votre Prénom: </label>
    <input type="text" name="prenom" value="<?= htmlspecialchars($_POST['prenom'] ?? '') ?>" required>
    
    <label>Entrez votre Login: </label>
    <input type="text" name="login" value="<?= htmlspecialchars($_POST['login'] ?? '') ?>" required>

    <label>Entrez votre Mot de passe: </label>
    <input type="password" name="password" required>

    <label>Entrez votre Lettre de motivation: </label>
    <textarea name="LDM" rows="5"><?= htmlspecialchars($_POST['LDM'] ?? '') ?></textarea>

    <label>Telechargez votre CV (PDF): </label>
    <input type="file" name="cv" accept=".pdf">

    <button type="submit" style="width: 300px; background-color: blue;">Envoyer</button>

</form>

</body>
</html>