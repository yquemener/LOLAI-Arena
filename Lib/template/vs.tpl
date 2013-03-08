<!--[if IE]><script language="javascript" type="text/javascript" src="static/lib/excanvas.js"></script><![endif]-->
<script language="javascript" type="text/javascript" src="static/lib/prototype.js"></script>
<script language="javascript" type="text/javascript" src="static/flotr2.js"></script>

<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>

<h2> {{" vs ".join([b.name for b in bots])}} </h2>
<p> Résultat: </br>
%if "score" in bots[1].__dict__:
		%for b in bots:
				{{b.name}} : {{b.score}}
		%end
%end
<center> And the winner is {{winner}} </center>
</p>

<div id="container_account" style="width:600px;height:300px;float: left;"></div>

<p> <a href="/"> Retour à l'arène </a> </p>

    
</body>

<script>
// Execute this when the page's finished loading
var f = Flotr.draw(
	$('container_account'), [
%for b in bots:
	{   data: {{[[i,data] for (i,data) in enumerate(b.hist_account) if i%2]}},
	    label: "{{b.name}}'s cash",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
%end	
]
);
</script>
