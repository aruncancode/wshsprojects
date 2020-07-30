redirect();

function redirect() {
	chosen = window.localStorage.getItem("chosen");
	console.log(chosen);

	if (chosen.length > 0)
		for (e of chosen.split(",")) {
			var s = document.createElement("h3");
			s.innerHTML = "1 X " + e;
			document.getElementById("receiptItems").appendChild(s);
		}
}
