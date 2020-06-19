function calc() {
	show = document.getElementById("showVal");
	hor = document.getElementById("horizRange").value;
	ver = document.getElementById("vertRange").value;

	horShow = document.getElementById("horizValue");
	verShow = document.getElementById("vertValue");

	horShow.innerHTML = hor;
	verShow.innerHTML = ver;

	show.innerHTML = hor * ver;
}
