<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>
<h2> Jeu du prisonnier </h2>
<form action="/vs" method="post">
<p> Nombre de maches 
    <input type="text" name="manche" value='50'></br>
    Joueur 1:
    % for b in bots:
        <input type="radio" name="player1" value="{{b}}" id="{{b}}" required/> <label for="{{b}}">{{b}}</label>
    %end
    </br>
    Joueur 2:
    % for b in bots:
        <input type="radio" name="player2" value="{{b}}" id="{{b}}" required/> <label for="{{b}}">{{b}}</label>
    %end
    </br>
    <input type="submit" value="Jouer le match">
</form>
</p>
<form action="/vsall" method="post">
    <input type="submit" value="Jouer toutes les combinaisons">
</form>
</body>
