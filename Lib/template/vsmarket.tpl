<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>

<h2> {{" vs ".join([b.name for b in bots])}} </h2>
<p> Résultat: </br>
%for b in bots:
    {{b.name}} : {{b.score}}
%end
<center> {{winner}} </center>
</p>
<p> <a href="/"> Retour à l'arène </a> </p>

    
</body>
