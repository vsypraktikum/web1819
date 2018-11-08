<!DOCTYPE html>
<html>
	<head>
		<title>Projekt_form</title>
		<meta charset="UTF-8" />

		<style>

		</style>
		<script type="text/javascript" src="/sit.js"></script><!--<script type="text/javascript" src="sorttable.js"></script>-->

	</head>
	<body>
	
		<form id="idWTForm" action="/saveProjekt" method="POST">
		
			<input type="hidden" value="${key_s}" id="id_s" name="id_s" />
			<div>
				<label for="nummer">Nummer</label></div>
				<input type="text" value="${data_o['nummer']}" id="nummer" name="nummer" required />
			</div>
			<div>
				<label for="bezeichnung">Bezeichnung</label>
				<input type="text" value="${data_o['bezeichnung']}" id="bezeichnung" name="bezeichnung" required />
			</div>
			<div>
				<label for="beschreibung">Beschreibung</label>
				<input type="text" value="${data_o['beschreibung']}" id="beschreibung" name="beschreibung" required />
			</div>
			<div>
				<label for="zeitraum">Bearbeitungszeitraum</label>
				<input type="text" value="${data_o['zeitraum']}" id="zeitraum" name="zeitraum" required />
			</div>
			<div>
				<label for="budget">Budget</label>
				<input type="text" value="${data_o['budget']}" id="budget" name="budget" required />
			</div>
			<div>
				<label for="kunden-id">Kunden_ID</label>
				<input type="text" value="${data_o['kunden-id']}" id="kunden-id" name="kunden-id" required />
			</div>
			<div>
				<label for="mitarbeiter-id">Mitarbeiter-ID</label>
				<input type="text" value="${data_o['mitarbeiter-id']}" id="mitarbeiter-id" name="mitarbeiter-id" required />
			</div>
			<div>
				<label for="stunden">Zeitaufwand</label>
				<input type="text" value="${data_o['stunden']}" id="stunden" name="stunden" required />
			</div>
			<div>
				<input type="submit" id="saveButton"  value="Speichern" />
				<a href="/"><input type="submit" value="Abbrechen"  /></a>
			</div>
		</form>

		<table>
			<tr>
				<th>Bezeichnung</th><th>Ansprechpartner</th><th>Nummer</th><th>Ort</th>
			</tr>
			% for key_s in data_o:
				<tr id="${key_s}" class="noMark" onClick="markRow(${key_s});">
					<td>${data_o[key_s]['bezeichnung']}</td>
					<td>${data_o[key_s]['ap']}</td>
					<td>${data_o[key_s]['nummer']}</td>
					<td>${data_o[key_s]['ort']}</td>
				</tr>
			% endfor
		</table>
	</body>
</html>
