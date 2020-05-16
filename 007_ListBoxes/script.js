function addValue() {
    var add_value = document.getElementById("addBox").value;
    if (add_value == "") {
        alert("please enter a value");
    }
    else {
        var opt = document.createElement("option");
        opt.text = add_value;
        opt.value = add_value;
        document.getElementById("options").options.add(opt);
        document.getElementById("addBox").value = "";
    }
}

function delValue() {
    var del_value = document.getElementById("options");
    del_value.remove(del_value.selectedIndex);
}