<!DOCTYPE html>
<html>
	<head>
		<title>Mitarbeiter_form</title>
		<meta charset="UTF-8" />

		<style>

		</style>
		<script type="text/javascript" src="/sit.js"></script><!--<script type="text/javascript" src="sorttable.js"></script>-->

	</head>
	<body>

		<form id="idWTForm" action="/saveMitarbeiter" method="POST">	
			<input type="hidden" value="${key_s}" id="id_s" name="id_s" />
			<div>
				<label for="name">Name</label></div>
				<input type="text" value="${data_o['name']}" id="name" name="name" required />
			</div>
			<div>
				<label for="branche">Vorname</label>
				<input type="text" value="${data_o['vorname']}" id="vorname" name="vorname" required />
			</div>
			<div>
				<label for="schwerpunkt">Funktion</label>
				<input type="text" value="${data_o['funktion']}" id="funktion" name="funktion" required />
			</div>
			<div>
				<input type="submit" id="saveButton"  value="Speichern" />
				<a href="/"><input type="submit" value="Abbrechen"  /></a>
			</div>
		</form>
	</body>
</html>
