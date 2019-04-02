

odoo.define('website_product_configure.javascript', function (require) {
 "use strict";
$(document).ready(function() {
    $('#hidden_box_btn').click(function (){
        var x = document.getElementById("hidden_box");
            if (x.style.display === "none") {
                x.style.display = "block";
                    } else {
                        x.style.display = "none";
                    }

                   });
                });
            });


