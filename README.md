# tournois-Raphael-Hassine
Nous allons réaliser une application dont le but est de gérer les résultats d'un tournoi sportif avec des poules, une phase finale, les dates et lieux, les équipes, les résultats et classements. Les utilisateurs peuvent consulter toutes les données par un principe de navigation, ou effectuer une recherche sur une donnée en particulier (poule, date, lieu, équipe, match) et commenter les matchs. Les administrateurs peuvent modérer les commentaires a posteriori.

L'application est évolutive, et dans la phase individuelle du projet vous pouvez vous limiter aux éléments suivants :

Elle contiendra une liste de matchs disponibles, constitués des attributs suivants :

    la date et heure,
    le lieu,
    les deux équipes,
    le score,
    le numéro de la poule.

Dans un premier temps on limitera le projet individuel à la phase de poule; la phase à élimination directe ne sera ajoutée que durant la phase du projet collectif.

Une équipe est constituée des attributs suivants :

    nom de l'équipe,
    nom de l'entraîneur,
    la liste des joueurs.

L'appartenance des équipes aux poules est stockée dans une autre classe :

    le numéro de la poule,
    le tournoi,
    la liste des équipes.

Et pour pouvoir organiser plusieurs tournois il faut aussi prévoir une entité ad-hoc contituée des attributs suivants :

    nom du tournoi,
    nom du lieu (facultatif),
    dates (facultatif),
    liste des équipes engagées,
    nombre de poules et nombre d'équipe par poule.
