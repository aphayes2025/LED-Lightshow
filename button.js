/*
The javascript file for our LED project. It creates all the buttons for the different effects and connects them from the html to python file
*/
var button = $("#red_led_button");
button.click(function() {
    console.log(button.text());
    if (button.text() === "Red LED On") {
        $.ajax({
            url: "/red_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button.text("Red LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button.text("Red LED On");
            }
        })
    }
});

var button2 = $("#blue_led_button");
button2.click(function() {
    console.log(button2.text());
    if (button2.text() === "Blue LED On") {
        $.ajax({
            url: "/blue_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button2.text("Blue LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button2.text("Blue LED On");
            }
        })
    }
});

var button3 = $("#green_led_button");
button3.click(function() {
    console.log(button3.text());
    if (button3.text() === "Green LED On") {
        $.ajax({
            url: "/green_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button3.text("Green LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button3.text("Green LED On");
            }
        })
    }
});

var button4 = $("#orange_led_button");
button4.click(function() {
    console.log(button4.text());
    if (button4.text() === "Orange LED On") {
        $.ajax({
            url: "/orange_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button4.text("Orange LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button4.text("Orange LED On");
            }
        })
    }
});

var button5 = $("#yellow_led_button");
button5.click(function() {
    console.log(button5.text());
    if (button5.text() === "Yellow LED On") {
        $.ajax({
            url: "/yellow_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button5.text("Yellow LED Off");
            }
    });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button5.text("Yellow LED On");
            }
        })
    }
});

var button6 = $("#pink_led_button");
button6.click(function() {
    console.log(button6.text());
    if (button6.text() === "Pink LED On") {
        $.ajax({
            url: "/pink_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button6.text("Pink LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button6.text("Pink LED On");
            }
        })
    }
});

var button7= $("#purple_led_button");
button7.click(function() {
    console.log(button7.text());
    if (button7.text() === "Purple LED On") {
        $.ajax({
            url: "/purple_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
                button7.text("Purple LED Off");
            }
        });
    } else {
        $.ajax({
            url: "/led_off",
            type: "post",
            success: function() {
                button7.text("Purple LED On");
            }
        })
    }
});

var button8 = $("#rainbow_led_button");
button8.click(function() {
    console.log(button8.text());
    if (button8.text() === "Rainbow LED On") {
        button8.text("Rainbow LED Off");
        $.ajax({
            url: "/rainbow_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
    button8.text("Rainbow LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});
var button9 = $("#strobe_led_button");
button9.click(function() {
    console.log(button9.text());
    if (button9.text() === "Strobe LED On") {
        button9.text("Strobe LED Off");
        $.ajax({
            url: "/strobe_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button9.text("Strobe LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button10 = $("#christmas_chase_led_button");
button10.click(function() {
    console.log(button10.text());
    if (button10.text() === "Christmas Chase LED On") {
        button10.text("Christmas Chase LED Off");
        $.ajax({
            url: "/christmas_chase_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button10.text("Christmas Chase LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button11 = $("#scroll_led_button");
button11.click(function() {
    console.log(button11.text());
    if (button11.text() === "Scroll LED On") {
        button11.text("Scroll LED Off");
        $.ajax({
            url: "/scroll_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button11.text("Scroll LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button12 = $("#bar_scroll_led_button");
button12.click(function() {
    console.log(button12.text());
    if (button12.text() === "Bar Scroll LED On") {
        button12.text("Bar Scroll LED Off");
        $.ajax({
            url: "/bar_scroll_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button12.text("Bar Scroll LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button13 = $("#wave_led_button");
button13.click(function() {
    console.log(button13.text());
    if (button13.text() === "Wave LED On") {
        button13.text("Wave LED Off");
        $.ajax({
            url: "/wave_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button13.text("Wave LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button14 = $("#constant_random_led_button");
button14.click(function() {
    console.log(button14.text());
    if (button14.text() === "Constant Random LED On") {
        button14.text("Constant Random LED Off");
        $.ajax({
            url: "/constant_random_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button14.text("Constant Random LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button15 = $("#rainbow_pattern_led_button");
button15.click(function() {
    console.log(button15.text());
    if (button15.text() === "Rainbow Pattern LED On") {
        button15.text("Rainbow Pattern LED Off");
        $.ajax({
            url: "/rainbow_pattern_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button15.text("Rainbow Pattern LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button16 = $("#random_led_button");
button16.click(function() {
    console.log(button16.text());
    if (button16.text() === "Random LED On") {
        button16.text("Random LED Off");
        $.ajax({
            url: "/random_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button16.text("Random LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button17 = $("#sparkle_led_button");
button17.click(function() {
    console.log(button17.text());
    if (button17.text() === "Sparkle LED On") {
        button17.text("Sparkle LED Off");
        $.ajax({
            url: "/sparkle_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button17.text("Sparkle LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button18 = $("#wave2_led_button");
button18.click(function() {
    console.log(button18.text());
    if (button18.text() === "Wave2 LED On") {
        button18.text("Wave2 LED Off");
        $.ajax({
            url: "/wave2_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button18.text("Wave2 LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button19 = $("#fill_three_led_button");
button19.click(function() {
    console.log(button19.text());
    if (button19.text() === "Fill Three LED On") {
        button19.text("Fill Three LED Off");
        $.ajax({
            url: "/fill_three_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button19.text("Fill Three LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button20 = $("#chase_three_led_button");
button20.click(function() {
    console.log(button20.text());
    if (button20.text() === "Chase Three LED On") {
        button20.text("Chase Three LED Off");
        $.ajax({
            url: "/chase_three_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button20.text("Chase Three LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});

var button21 = $("#gradient_led_button");
button21.click(function() {
    console.log(button21.text());
    if (button21.text() === "Gradient LED On") {
        button21.text("Gradient LED Off");
        $.ajax({
            url: "/gradient_led_on",
            type: "post",
            success: function(response) {
                console.log(response);
            }
        });
    } else {
        button21.text("Gradient LED On");
        $.ajax({
            url: "/effects_led_off",
            type: "post",
        })
    }
});
