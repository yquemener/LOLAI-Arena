<!--[if IE]><script language="javascript" type="text/javascript" src="static/lib/excanvas.js"></script><![endif]-->
<script language="javascript" type="text/javascript" src="static/lib/prototype.js"></script>
<script language="javascript" type="text/javascript" src="static/flotr2.js"></script>

<head> 
<title>LoL Arena</title>
</head>

<body>
<h1> LoL Arena : {{game_name}}</h1>

<h2> {{" vs ".join([b.name for b in bots])}} </h2>
%for attr in attributes:
	<h3> attr </h3>
	<p>
	%if attr in bots[1].__dict__:
		%for b in bots:
			{{b.name}} : {{getattr(b,attr)}}
			<\br>
		%end
	%else:
		{{attr}} id not an attribute of bots.
	%end
	</p>
<center> And the winner is {{winner}} </center>
</p>

<div id="graphics">
%for plot in plots:
	<div id="container_{{plot["name"]}}" style="width:600px;height:300px;"></div>
%end
</div>

<p> <a href="/"> Retour à l'arène </a> </p>
</body>

<script>
// Execute this when the page's finished loading
%for plot in plots:
		var f = Flotr.draw(
				$('container_{{plot["name"]}}'), [
				%if "from_bots" in plot.keys():
						%for b in bots:
						{   data: {{[[i,data] for (i,data) in enumerate(getattr(b,"hist_"+plot["from_bots"]))]}},
								label: "{{b.name}}'s {{plot["from_bots"]}}",
								lines: {show: true, fill: true},
								points: {show: true}
						},
						%end
				%else:
						%for data in plots['datas']:
						{   data: {{[[i,d] for (i,d) in enumerate(data["data"])]}},
								label: "{{data["name"]}}",
								lines: {show: true, fill: true},
								points: {show: true}
						%end
				%end	
				]
		);

%end
</script>
