<?php

abstract class Voiture {
    protected $marque;
    protected $modele;
    protected $annee;

    public function __construct($marque, $modele, $annee) {
        $this->marque = $marque;
        $this->modele = $modele;
        $this->annee  = $annee;
    }

    public function getDescription() {
        return "{$this->marque} {$this->modele} ({$this->annee})";
    }

    abstract public function rouler();
}

interface Rechargeable {
    public function recharger();
}

class Essence extends Voiture {
    public function rouler() {
        return "{$this->getDescription()} roule avec un moteur à essence.";
    }
}

class Electrique extends Voiture implements Rechargeable {
    public function rouler() {
        return "{$this->getDescription()} roule silencieusement avec un moteur électrique.";
    }

    public function recharger() {
        return "{$this->getDescription()} est en train de se recharger.";
    }
}

class Hybride extends Voiture implements Rechargeable {
    public function rouler() {
        return "{$this->getDescription()} alterne entre essence et électricité.";
    }

    public function recharger() {
        return "{$this->getDescription()} recharge sa batterie.";
    }
}

class Garage {
    private $voitures = [];

    public function ajouterVoiture($voiture) {
        if (!($voiture instanceof Voiture)) {
            throw new Exception("Seules les voitures peuvent être ajoutées au garage !");
        }
        $this->voitures[] = $voiture;
    }

    public function afficherVoitures() {
        foreach ($this->voitures as $voiture) {
            echo $voiture->rouler() . "<br>";
        }
    }
}

$garage = new Garage();

echo "<h2>---Exercice 03---</h2>" . "<br>";
try {
    $garage->ajouterVoiture(new Essence("Renault", "Clio", 2020));
    $garage->ajouterVoiture(new Electrique("Tesla", "Model 3", 2022));
    $garage->ajouterVoiture(new Hybride("Toyota", "Prius", 2021));
} catch (Exception $e) {
    echo "Erreur : " . $e->getMessage() . "<br>";
}
$garage->afficherVoitures();

try {
    $garage->ajouterVoiture("Je ne suis une voiture");
}
catch(Exception $e) {
    echo "Erreur : " . $e->getMessage() . "<br>";
}
?>