function addValue() {
    var add_value = document.getElementById("addBox").value;
    if (add_value == "") {
        alert("please enter a value");
    }
    else {
        var opt = document.createElement("option");
        opt.innerHTML = add_value;
        opt.value = add_value;
        document.getElementById("options").add(opt);
        document.getElementById("addBox").value = "";
    }
}

function delValue() {
    var option_menu = document.getElementById("options");
    if (option_menu.selectedIndex == -1) {
        alert("please select an option to delete");
    }
    else {
        option_menu.remove(option_menu.selectedIndex);

    }
}