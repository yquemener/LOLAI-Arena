<!--[if IE]><script language="javascript" type="text/javascript" src="static/lib/excanvas.js"></script><![endif]-->
<script language="javascript" type="text/javascript" src="static/lib/prototype.js"></script>
<script language="javascript" type="text/javascript" src="static/flotr2.js"></script>

<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>

<div id="container" style="width:600px;height:300px;"></div>

<h2> {{" vs ".join([b.name for b in bots])}} </h2>
<p> Résultat final: <br/><br/>
%for b in bots:
    {{b.name}} : {{b.score}} <br/>
%end
<center> {{winner}} </center>
</p>
<p> <a href="/"> Retour à l'arène </a> </p>
</body>

<script>

// Execute this when the page's finished loading
var f = Flotr.draw(
	$('container'), [
	
%for b in players_charts.keys():
	{   data: [ 
	    %for i in range(len(players_charts[b])):
	        [{{i}}, {{players_charts[b][i]}}],
	    %end
	    ],
	    label: "{{b}}'s cash",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
%end	
]
);
</script>

