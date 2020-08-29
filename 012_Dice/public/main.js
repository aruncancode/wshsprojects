face1 = document.getElementById("face1");
face2 = document.getElementById("face2");

function roll() {
	num1 = Math.floor(Math.random() * 6) + 1;
	num2 = Math.floor(Math.random() * 6) + 1;

	face1.src = "./Dice Images/" + num1 + ".jpg";
	face2.src = "./Dice Images/" + num2 + ".jpg";
}
