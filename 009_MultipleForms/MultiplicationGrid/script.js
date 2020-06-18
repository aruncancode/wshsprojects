function calc() {
	show = document.getElementById("showVal");
	hor = document.getElementById("horizRange").value;
	ver = document.getElementById("vertRange").value;

	show.innerHTML = hor * ver;
}
