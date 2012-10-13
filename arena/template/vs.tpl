<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>

<h2> {{" vs ".join(bots)}} </h2>
<p> Résultat: </br>
%for (i,b) in enumerate(bots):
    {{b}} : {{scores[i]}}
%end
<center> {{winner}} </center>
</p>
<p> <a href="arena"> Retour à l'arène </a> </p>

    

</body>
