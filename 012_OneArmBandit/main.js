ad = "imgs/";
face = {
	1: ad + "1.jpg",
	2: ad + "2.jpg",
	3: ad + "3.jpg",
	4: ad + "4.jpg",
	5: ad + "5.jpg",
	6: ad + "6.jpg",
	7: ad + "7.jpg",
};

while (!roll()) {
	roll();
} // the game loads into jackpot

function roll() {
	num1 = Math.floor(Math.random() * 6) + 1;
	num2 = Math.floor(Math.random() * 6) + 1;
	num3 = Math.floor(Math.random() * 6) + 1;

	$("#face1").attr("src", face[num1]);
	$("#face2").attr("src", face[num2]);
	$("#face3").attr("src", face[num3]);

	if (num1 == num2 && num1 == num3 && num2 == num3) {
		document.getElementById("heading").innerHTML = "Jackpot!";
		confetti.start();
		return true;
	} else {
		confetti.stop();
		document.getElementById("heading").innerHTML = "One arm bandit!";
	}
}
