var n = 0;

cost = 0;
var chosen = [];

choices = {
	MAG: [0, 5],
	VEG: [0, 4],
	HAW: [0, 6],
	NEW: [0, 5],
	SML: [0, 2],
	MED: [0, 3],
	LAG: [0, 4],
	BAC: [0, 3],
	CHE: [0, 2],
	PEP: [0, 3],
	COKE: [0, 2],
	FAN: [0, 2],
	H20: [0, 2],
	SLURPE: [0, 100],
};

function limit_size(id, n) {
	size_ids = ["SML", "MED", "LAG"];
	if (n) {
		var filteredAry = size_ids.filter(function (e) {
			return e !== id;
		});

		for (e of filteredAry) {
			document.getElementById(e).disabled = true;
		}
	} else {
		for (e of size_ids) {
			document.getElementById(e).disabled = false;
		}
	}
}

function get(id, clicked) {
	choices[id][0] = clicked;
	if (["SML", "MED", "LAG"].includes(id)) {
		n = !n;
		limit_size(id, n);
	}
	process();
}

function process() {
	chosen = [];
	cost = 0;
	for (i = 0; i < Object.keys(choices).length; i++) {
		if (choices[Object.keys(choices)[i]][0]) {
			cost += choices[Object.keys(choices)[i]][1];
			chosen.push(Object.keys(choices)[i]);
		}
	}
	document.getElementById("cost").innerHTML = "$" + cost;
}

function redirect() {
	window.location.href = "checkout.html";
	window.localStorage.setItem("chosen", chosen);
}
