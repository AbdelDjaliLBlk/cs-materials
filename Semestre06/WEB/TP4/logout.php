<?php
session_start();
session_unset();
session_destroy();
setcookie("informatique", "", time() - 3600);
setcookie("PHPSESSID", "", time() - 3600);
header("Location: session.php");
exit();
?>