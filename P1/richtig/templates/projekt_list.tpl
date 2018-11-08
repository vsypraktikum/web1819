<!DOCTYPE html>
<html>
	<head>
		<title>Projekt_liste</title>
		<meta charset="UTF-8" />
		<link rel="stylesheet" type="text/css" href="/style.css">
		<style>
			@import "/style.css";

		</style>
		<script type="text/javascript" src="/ppm.js"></script>
	</head>
	<body onload="StandardListe_INIT()">
	<div class="kopf"></div>
		<div><a href="/">Zurück</a></div>
		<div><a href="/addProjekt">Neu</a></div>
		<table>
			<tr>
				<th>Nummer</th><th>Bezeichnung</th><th>Beschreibung</th><th>Zeitraum</th><th>Budget</th><th>Kunden_ID</th><th>Mitarbeiter_ID</th><th>Zeitaufwand</th>
			</tr>
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td >${data_o[key_s]['nummer']}</td>
					<td>${data_o[key_s]['bezeichnung']}</td>
					<td>${data_o[key_s]['beschreibung']}</td>
					<td>${data_o[key_s]['zeitraum']}</td>
					<td>${data_o[key_s]['budget']}</td>
					<td>${data_o[key_s]['kunden-id']}</td>
					<td>${data_o[key_s]['mitarbeiter-id']}</td>
					<td>${data_o[key_s]['stunden']}</td>
				</tr>
			% endfor
		</table>
		<div id="/deleteProjekt/" class="likeabutton">Löschen</div>
		<div id="/editProjekt/" class="likeabutton">Bearbeiten</div>
	</body>
</html>
