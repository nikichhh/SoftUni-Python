function promotions(type_day, age){
    if (0 <= age && age <= 18) {
        if (type_day == "Weekday") {
            console.log("12$");
        } else if (type_day == "Weekend") {
            console.log("15$");
        } else if (type_day == "Holiday") {
            console.log("5$");
        } else {
            console.log("Error!");
        }
    } else if (age > 18 && age <= 64) {
        if (type_day == "Weekday") {
            console.log("18$");
        } else if (type_day == "Weekend") {
            console.log("20$");
        } else if (type_day == "Holiday") {
            console.log("12$");
        } else {
            console.log("Error!");
        }
    } else if (age > 64 && age <= 122) {
        if (type_day == "Weekday") {
            console.log("12$");
        } else if (type_day == "Weekend") {
            console.log("15$");
        } else if (type_day == "Holiday") {
            console.log("10$");
        } else {
            console.log("Error!");
        }
    } else {
        console.log("Error!");
    }
}
