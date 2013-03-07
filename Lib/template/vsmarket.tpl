<!--[if IE]><script language="javascript" type="text/javascript" src="static/lib/excanvas.js"></script><![endif]-->
<script language="javascript" type="text/javascript" src="static/lib/prototype.js"></script>
<script language="javascript" type="text/javascript" src="static/flotr2.js"></script>

<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena </h1>
<h2> {{" vs ".join([b.name for b in bots])}} </h2>
<p> Résultat final: <br/><br/>
%for b in bots:
    {{b.name}} : {{b.score}} <br/>
%end
<center> {{winner}} </center>
</p>
<div id="container_cash" style="width:600px;height:300px;float: left;"></div>
<div id="container_flour" style="width:600px;height:300px;float: left;"></div>
<div id="container_wheat" style="width:600px;height:300px;float: left;"></div>
<div id="container_flour_price" style="width:600px;height:300px;float: left;"></div>

<p> <a href="/"> Retour à l'arène </a> </p>
</body>

<script>

// Execute this when the page's finished loading
var f = Flotr.draw(
	$('container_cash'), [
%for b in players_charts.keys():
	{   data: {{[[i,data] for (i,data) in enumerate(players_charts[b]["cash"]]}},
	    label: "{{b}}'s cash",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
%end	
]
);

// Ici ça serai plus simple de mettre tout l'historique de l'évolution de cette "richesse" directement dans le bot pour pouvoir importer les data avec 
// 		data: b.history[data_name]
// Par contre cela nécéssite de faire un systeme pour que les bots enregistrent eux même leurs historiques.
//
// Ensuite on pourrai faire une liste (donnée par arena.py) des données à tracer sur des graphiques et on aurait plus qu'à boucler dessus pour creer les graphiques.
//
// Et même que la création de graphique pourrai être faire dans une fonction js du genre
// plot_data(data_name) ...
// 		var f = Flotr.draw(
// 			$('container_data_name'), [
// 		%for b in players_charts.keys():
// 			{   data: {{b.data[data_name]}} // je vois un potentiel soucis ici!
// 			    label: "{{b.name}}'s cash",
// 			    lines: {show: true, fill: true},
// 			    points: {show: true}
// 			},
// 		%end	
// 		]
// 		);
//
// Mais avant de faire tout ça il faut faire une bon système d'historique dans les bots!

var f2 = Flotr.draw(
	$('container_wheat'), [
%for b in players_charts.keys():
	{   data: [ 
	    %for i in range(len(players_charts[b]["wheat"])):
	        [{{i}}, {{players_charts[b]["wheat"][i]}}],
	    %end
	    ],
	    label: "{{b}}'s wheat",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
%end	
]
);

var f3 = Flotr.draw(
	$('container_flour'), [
%for b in players_charts.keys():
	{   data: [ 
	    %for i in range(len(players_charts[b]["flour"])):
	        [{{i}}, {{players_charts[b]["flour"][i]}}],
	    %end
	    ],
	    label: "{{b}}'s flour",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
%end	
]
);

var f4 = Flotr.draw(
	$('container_flour_price'), [
	{   data: [ 
	    %for i in range(len(stats_charts["flour_price"])):
	        [{{i}}, {{stats_charts["flour_price"][i]}}],
	    %end
	    ],
	    label: "Flour price",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
]
);


var f5 = Flotr.draw(
	$('container_wheat_price'), [
	{   data: [ 
	    %for i in range(len(stats_charts["wheat_price"])):
	        [{{i}}, {{stats_charts["wheat_price"][i]}}],
	    %end
	    ],
	    label: "Wheat price",
	    lines: {show: true, fill: true},
	    points: {show: true}
	},
]
);
</script>

