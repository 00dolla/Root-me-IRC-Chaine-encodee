<?php

$socket = fsockopen('server_name','port_server');
if(!$socket){
    // Connexion fails
   echo 'Erreur de connexion';
   exit;
}else {
    echo "Connexion Reussi \n";

    //Création USER
  fputs($socket,"USER loick loick loick loick\r\n");
  fputs($socket,"NICK loick\r\n");

  $continuer = 1; // On initialise une variable permettant de savoir si l'on doit continuer la boucle.
  while($continuer) // Boucle principale.
      {
          $donnees = fgets($socket, 1024); // Le 1024 permet de limiter la quantité de caractères à recevoir du serveur.
      $retour = explode(':',$donnees); // On sépare les différentes données.
      // On regarde si c'est un PING, et, le cas échéant, on envoie notre PONG.
      if(substr($retour[1],0,5) == "loick"){
          fputs($socket,"PRIVMSG bot_name : !ep2\r\n");
      }
      if(substr($retour[1],0,5) == "bot_name"){
          $string = base64_decode($retour[2]);
          fputs($socket,"PRIVMSG bot_name : !ep2 -rep ".$string."\r\n");
      }
      if(rtrim($retour[0]) == 'PING')
      {
          fputs($socket,'PONG :'.$retour[1]);
          $continuer = 0;
      }
       if($donnees) // Si le serveur a envoyé des données, on les affiche.
           echo $donnees;
      }
}
 ?>