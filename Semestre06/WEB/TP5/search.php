<?php
$users = ['Ali', 'Badr', 'Chahinaze', 'Doua', 'Ines', 'Yanis', 'Mohammed', 'Youcef', 'Fethallah', 'Amine'];

if (isset($_GET['query'])) {
    $query = strtolower(trim($_GET['query']));
    $results = [];

    foreach ($users as $user) {
        if (strpos(strtolower($user), $query) !== false) {
            $results[] = $user;
        }
    }

    if (!empty($results)) {
        foreach ($results as $result) {
            echo '<div>' . htmlspecialchars($result) . '</div>';
        }
    } else {
        echo '<div>Aucun résultat trouvé.</div>';
    }
}
?>
