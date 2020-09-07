roll_name = document.getElementById("names");

face = {
	1: "https://upload.wikimedia.org/wikipedia/commons/2/2c/Alea_1.png",
	2: "https://upload.wikimedia.org/wikipedia/commons/b/b8/Alea_2.png",
	3: "https://upload.wikimedia.org/wikipedia/commons/2/2f/Alea_3.png",
	4: "https://upload.wikimedia.org/wikipedia/commons/8/8d/Alea_4.png",
	5: "https://upload.wikimedia.org/wikipedia/commons/5/55/Alea_5.png",
	6: "https://upload.wikimedia.org/wikipedia/commons/f/f4/Alea_6.png",
};

names = {
	11: "Snake Eyes",
	12: "Ace Deuce",
	13: "Easy Four",
	14: "Fever Five",
	15: "Easy Six",
	16: "Natural",
	22: "Hard Four",
	23: "Fever Five",
	24: "Easy Six",
	25: "Natural",
	26: "Easy Eight",
	33: "Hard Six",
	34: "Natural",
	35: "Easy Eight",
	36: "Nina",
	44: "Hard Eight",
	45: "Nina",
	46: "Easy Ten",
	55: "Hard Ten",
	56: "Yo",
	66: "Boxcars",
};

roll();

function roll() {
	num1 = Math.floor(Math.random() * 6) + 1;
	num2 = Math.floor(Math.random() * 6) + 1;

	$("#face1").attr("src", face[num1]);
	$("#face2").attr("src", face[num2]);

	if (names[num1.toString(10) + num2.toString(10)] == undefined) {
		roll_name.innerHTML = names[num2.toString(10) + num1.toString(10)];
	} else {
		roll_name.innerHTML = names[num1.toString(10) + num2.toString(10)];
	}
}

n = 1;
function something() {
	if (n) $("h2").fadeOut();
	else $("h2").fadeIn();
	n = !n;
}
