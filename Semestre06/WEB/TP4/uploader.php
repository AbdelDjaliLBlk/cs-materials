<?php
// on vérifies que le champ est bien rempli:
if(!empty($_FILES["fichier_choisi"]["name"]))
{
	// nom du fichier choisi:
	$nomFichier    = $_FILES["fichier_choisi"]["name"] ;
	// nom temporaire sur le serveur:
	$nomTemporaire = $_FILES["fichier_choisi"]["tmp_name"] ;
	// type du fichier choisi:
	$typeFichier   = $_FILES["fichier_choisi"]["type"] ;
	// poids en octets du fichier choisit:
	$poidsFichier  = $_FILES["fichier_choisi"]["size"] ;
	// code de l'erreur si jamais il y en a une:
	$codeErreur    = $_FILES["fichier_choisi"]["error"] ;
	// chemin qui mène au dossier qui va contenir les fichiers uplaod:
	$chemin = "telechar/" ;
	if(move_uploaded_file ($nomTemporaire, $chemin.$nomFichier))
	{
		echo("L'upload a r&eacute;ussi<br>") ;
		echo("$nomFichier<br>") ;
		echo("$nomTemporaire<br>") ;
		echo("$typeFichier<br>") ;
		echo("$poidsFichier<br>") ;
		echo("$codeErreur<br>") ;
		}
	else
		echo("<br>L'upload a &eacute;chou&eacute;") ;
}//fin if
else
{
	echo("Vous n'avez pas choisit de fichier!!<br>") ;
	echo("<a href=\"source.php\">Retour</a>") ;
}//fin else
?>
