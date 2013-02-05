<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>

%for game in games:
    <h2> {{game}}  </h2>
    <form action="/vs" method="post">
    <input type='hidden' name='game_name' value='{{game}}'>
    <p> 

    %for elem in [e for e in games[game] if (e!="players") and (e!="bots")]:
    {{games[game][elem][1]}}
    <input type="text" name="{{elem}}" value='{{games[game][elem][0]}}
'></br>
    %end

    %for i in range(games[game]["players"]):
    Joueur {{i+1}}:
    % for b in games[game]["bots"]:
        <input type="radio" name="bot{{i+1}}" value="{{b}}" id="{{b}}" required/> <label for="{{b}}">{{b}}</label>
    %end
    </br>
    %end

    <input type="submit" value="Jouer le match">
    </form>
    </p>
    <p> 
    <form action="/challenge" method="post">
    <input type='hidden' name='game_name' value='{{game}}'>
    <input type='hidden' name='chall_type' value='championship'>
    <input type='submit' value="Que tout le monde s'affronte!">
    </form>
    </p>
    
%end

    
</body>
