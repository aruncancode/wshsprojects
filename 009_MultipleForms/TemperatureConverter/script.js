celOb = document.getElementById("celciusInput");
farOb = document.getElementById("fahrenheitInput");

function toFar() {
	far = (celOb.value * 9) / 5 + 32;
	farOb.value = far;
	if (far == 32) {
		celOb.value = 0;
	}
}

function toCel() {
	cel = ((farOb.value - 32) * 5) / 9;
	celOb.value = cel;
}
