<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>
%i=0
<h2> {{" vs ".join([b.name for b in bots])}} </h2>
<p> Résultat: </br>
%for b in bots:
    {{b.name}} : {{scores[i]}}
    %i=i+1
%end
<center> {{winner}} </center>
</p>
<p> <a href="arena"> Retour à l'arène </a> </p>

    

</body>
