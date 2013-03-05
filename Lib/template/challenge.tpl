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

<h2> Challenge </h2>
<table>
<tr>
<td><div class="header">\</div></td>
%for b in bots:
    <td><div class="header">{{b}}</div></td>
%end
<td><div class="header">Total score</div></td>
</tr>
%for (i,bi) in enumerate(bots):
    <tr>
    <td><div class="header">{{bi}}</div></td>
    %for (j,bj) in enumerate(bots):
        <td><div class="score">{{" / ".join([str(s) for s in scores[i][j]])}}</div></td>
    %end
    <td><div class="sum">{{sum([s[0] for s in scores[i]])}}</div></td>
    </tr>
%end
</table>
</p>
<p> <a href="arena"> Retour à l'arène </a> </p>


</body>
