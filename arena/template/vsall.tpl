<head> 
<title>LoL Arena</title>
</head>

<body>
<style type="text/css">
    .header {background-color:#dddddd;border-style:dotted;border-width:1px;}
    .score {border-style:dotted;border-width:1px;}
    .sum {border-style:solid;border-width:1px;}    
</style>
<h1> LoL Arena </h1>

<h2> All vs. all results </h2>
<table>
    <tr>
        <td><div class="header">\</div></td>
        %for b in bots:
        <td><div class="header">{{b}}</div></td>
        %end
        <td><div class="header">Total score</div></td>
    </tr>
    %for c1 in bots:
    <tr>
        <td><div class="header">{{c1}}</div></td>
        %for c2 in bots:
        <td><div class="score">{{scores[(c1,c2)]}}</div></td>
        %end
        <td><div class="sum">{{scores[c1]}}</div></td>
    </tr>
    %end
</table>
</p>
<p> <a href="arena"> Retour à l'arène </a> </p>

    

</body>
