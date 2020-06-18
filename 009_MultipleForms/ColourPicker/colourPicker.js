function changeColour() {
	let red = make_rgb(Number(document.getElementById("red").value).toString(16));
	let green = make_rgb(
		Number(document.getElementById("green").value).toString(16)
	);
	let blue = make_rgb(
		Number(document.getElementById("blue").value).toString(16)
	);
	let colour = "#" + red + green + blue;
	document.getElementById("colour_mix").innerHTML = colour;
	document.getElementById("display").style.background = colour;
	document.getElementById("colour_mix").style.color = colour;
}

function make_rgb(x) {
	if (x.length < 2) {
		return "0" + x;
	} else {
		return x;
	}
}
