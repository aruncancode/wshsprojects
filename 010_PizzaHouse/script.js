var n = 0;

var cost = 0;
var chosen = [];

choices = {
	Margherita: [0, 5],
	Vegetariana: [0, 4],
	Hawaiian: [0, 6],
	"New Yorker": [0, 5],
	Small: [0, 2],
	Medium: [0, 3],
	Large: [0, 4],
	Bacon: [0, 3],
	Cheese: [0, 2],
	Pepperoni: [0, 3],
	Coke: [0, 2],
	Fanta: [0, 2],
	Water: [0, 2],
	"Slurpe Juice": [0, 100],
};

function limit_size(id, n) {
	size_ids = ["Small", "Medium", "Large"];
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
	if (["Small", "Medium", "Large"].includes(id)) {
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
	document.getElementById("cost").innerHTML = "$" + cost + ".00";
}

function redirect() {
	window.location.href = "checkout.html";
	window.localStorage.setItem("chosen", chosen);
	window.localStorage.setItem("cost", cost);
}
