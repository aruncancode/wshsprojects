var i = 0;
addValue(){
    add_value = document.form1.textinput.value;
    AddOpt = new Option(add_Value, add_value);
    document.getElementById("options")[i++] = AddOpt;
}