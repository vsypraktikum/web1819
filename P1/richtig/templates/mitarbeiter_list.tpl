<!DOCTYPE html>
<html>
	<head>
		<title>Mitarbeiter_liste</title>
		<meta charset="UTF-8" />
		<link rel="stylesheet" href="/style.css">
		<style>
			@import "/style.css";
		</style>
		<script type="text/javascript" src="/ppm.js"></script>
	</head>
	<body onload="StandardListe_INIT()">
		<div class="kopf"></div>
		<div><a href="/">Zurück</a></div>
		<div><a href="/addMitarbeiter">Neu</a></div>
		<table> 
		
			<tr>
				<th>Name</th><th>Vorname</th><th>Funktion</th>
			</tr>
			
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td>${data_o[key_s]['name']}</td>
					<td>${data_o[key_s]['vorname']}</td>
					<td>${data_o[key_s]['funktion']}</td>
				</tr>
			% endfor
		</table>
		
		<div id="/deleteMitarbeiter/" class="likeabutton">Löschen</div>
		<div id="/editMitarbeiter/" class="likeabutton">Bearbeiten</div>
	</body>
</html>
