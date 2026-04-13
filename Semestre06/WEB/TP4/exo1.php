<?php
$chaine = "PHP est un langage de script";
echo strrev($chaine) . "<br>";  // Afficher la chaine à l'envers
echo ucfirst("php est un langage de script") . "<br>"; // Mettre la première lettre en majuscule
echo str_pad("PHP", 8, "*") . "<br>"; // Ajouter des caractères pour atteindre une longueur de 8
echo str_repeat("PHP ", 3) . "<br>"; // Répéter la chaîne "PHP " 3 fois
$mots = explode(" ", $chaine); // Diviser la chaîne en mots
print_r($mots); // Afficher les mots sous forme de tableau
echo "<br>"; // Revient à la ligne
$numbers = [1, 2, 2, 3, 4, 4, 5];
print_r(array_unique($numbers)); // Afficher les nombres uniques
echo "<br>";
print_r(array_filter($numbers, fn($n) => $n > 2));
echo "<br>";
print_r(array_map(fn($n) => $n * 2, $numbers));
echo "<br>";
$data = ["nom" => "Ali", "age" => 25];
$json = json_encode($data);
echo $json . "<br>";
$array = json_decode($json, true);
print_r($array);

?>