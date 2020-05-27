var x = {};

function addValue() {
    var add_value = document.getElementById("addBox").value;
    if (add_value == "") {
        alert("please enter a value");
    }
    else {
        var opt = document.createElement("option");
        opt.innerHTML = add_value;
        opt.value = add_value;
        opt.onclick = function () { showValue(); };
        x[add_value] = [];
        document.getElementById("options").add(opt);
        document.getElementById("addBox").value = "";

    }
}

function addValue2() {
    var add_value = document.getElementById("addBox").value;
    var selectTrue = document.getElementById("options").selectedIndex;
    if (add_value == "") {
        alert("please enter a value");
    }
    else {

        if (selectTrue == -1) {
            alert("please select a value from box1");
        }

        else {

            var selectValue = document.getElementById("options").value;
            var opt = document.createElement("option");
            opt.innerHTML = add_value;
            opt.value = selectValue;
            document.getElementById("options2").add(opt);
            x[selectValue].push(add_value);
            document.getElementById("addBox").value = "";

        }
    }
}

function delValue() {
    var option_menu = document.getElementById("options");
    if (option_menu.selectedIndex == -1) {
        alert("please select an option to delete");
    }
    else {
        delete x[option_menu.value];
        option_menu.remove(option_menu.selectedIndex);
    }
}

function delValue2() {
    var option_menu = document.getElementById("options2");
    if (option_menu.selectedIndex == -1) {
        alert("please select an option to delete");
    }
    else {
        x[option_menu.value].splice(option_menu.selectedIndex, 1);
        option_menu.remove(option_menu.selectedIndex);
    }
}


function showValue() {
    document.getElementById("options2").options.length = 0;
    var selected_value = document.getElementById("options").value;

    for (var i in x[selected_value]) {
        var new_opt = document.createElement("option");
        new_opt.innerHTML = x[selected_value][i];
        new_opt.value = selected_value;
        document.getElementById("options2").add(new_opt);
    }
}