<?php
print("OK\n");

# Ma première réponse
$ans = "C";

# Réponse suposé de l'autre
$other = "C";

# On attends le message de départ (qui doit être OK)
$master = fgets(STDIN);

# Tant qu'on ne nous a pas dit qu'on arretait
while($master != "Q"){
    # On copie la réponse de l'autre
    $ans = $other;
    # On envoie notre réponse
    print($ans . "\n");
    # On reçoit la réponse de l'autre
    $other = fgets(STDIN);
    # On attend un nouveau message du maitre (Continuer ou stop)
    $master = fgets(STDIN);
}
?>
