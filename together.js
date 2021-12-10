/**
 * @description      : 
 * @author           : student
 * @group            : 
 * @created          : 11/06/2021 - 08:44:27
 * 
 * MODIFICATION LOG
 * - Version         : 1.0.0
 * - Date            : 11/06/2021
 * - Author          : student
 * - Modification    : 
 **/
function leapYear(year) {
    if (year % 4 == 0)
        console.log(`${year} is a leap year`)

    else {
        console.log(`${year} is not a leap year`)
    }
}
leapYear(2020);
leapYear(1991)

//function to times any 2 numbers
function number() {
    var num1 = 22
    var num2 = 10
    var x = num1 * num2

    console.log(x)
}
number();

function naming(){
    var frist_name="Aisha"
    var last_name="Fadallala"
    var full_name=frist_name + last_name

    console.log(full_name)
}
naming()