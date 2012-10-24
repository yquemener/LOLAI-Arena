<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>

%for game in games:
    <h2> {{game}}  </h2>
    <form action="/vs" method="post">
    <input type='hidden' name='game' value='{{game}}'>
    <p> 
    <!--
    Les options devront être dans un future qu'on espère proche être donnée par le "game" avec une super @classmethod
    Comme ça on aura le nombre de joueurs, le nombre de manches....
    --!>
    Nombre de manches 
    <input type="text" name="manche" value='50'></br>
    Joueur 1:
    % for b in games[game]:
        <input type="radio" name="player1" value="{{b}}" id="{{b}}" required/> <label for="{{b}}">{{b}}</label>
    %end
    </br>
    Joueur 2:
    % for b in games[game]:
        <input type="radio" name="player2" value="{{b}}" id="{{b}}" required/> <label for="{{b}}">{{b}}</label>
    %end
    </br>
    <input type="submit" value="Jouer le match">
    </p>
%end
    
</body>
