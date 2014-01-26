$(document).ready(function () {
    $("#first-choice").change(function() {
        var $dropdown = $(this);

        $.getJSON("/static/categories.json", function(data) {
            var key = $dropdown.val();
            var vals = data[key]['SubCategories'];

            console.log(data[key]['SubCategories']);
            var $secondChoice = $("#second-choice");
            $secondChoice.empty();

            var opt = document.createElement('option');
            $(opt).html("Select a Sub-Category");
            $secondChoice.append(opt);

            $.each(vals, function(index, value) {
                var opt = document.createElement('option');
                $(opt).val(value.id);
                $(opt).html(value.value);
                $secondChoice.append(opt);
            });
        });
    });

    window.onload = function () {
        var table = document.getElementById("average-table");
        var tempData = []
            for (var i = 0, row; row = table.rows[i]; i++){
                for (var j = 0, col; col = row.cells[j]; j++){
                    temp = {}
                    temp['label']=table.rows[i].cells[j++].innerHTML;
                    temp['y']=parseInt(table.rows[i].cells[j].innerHTML);
                    tempData.push(temp);
                    console.log(temp);
                }
            }        
        var chart = new CanvasJS.Chart("chartContainer", {

            title:{
                text: "Average Resale Value of \"" + $("#search_term").html() + "\"",
                fontWeight: "lighter",
            },
            axisX:{
                title: "Time of Day",
            },
            axisY:{
                title: "Price (Dollars)",
                gridColor: "#C0C0C0",
            },
            data: [//array of dataSeries              
                { //dataSeries object
                type: "column",
                color: "rgba(12,143,221,.5)",
                dataPoints: tempData
                } 
            ]
         });
     
        chart.render();
    }

    $("#keywords").focus()


    function checkSubmitReady(){
        var $keywords = $("#keywords");
        var $first = $("#first-choice");
        var $second = $("#second-choice");
        var ready = true;

        if (!$keywords.val()) {
            $keywords.attr("placeholder", "You must enter keywords!");
            $keywords.css("border", "2px dashed #d9534f");
            ready = false;
        } else {
            $keywords.css("border", "none");
        }
        if ($first.children("option").filter(":selected").text() === "Select a Category") { 
            $first.css("border", "2px dashed #d9534f");
            ready = false;
        } else {
            $first.css("border", "none");
        }
        if ($second.children("option").filter(":selected").text() === "Select a Sub-Category") { 
            $second.css("border", "2px dashed #d9534f");
            ready = false;
        } else {
            $second.css("border", "none");
        }
        
        return ready;
    }

    /* Submit buttons for search form */
    $("#similar-button").click(function() {
        if (checkSubmitReady()) {
            $("#search-form").attr('action', '/similar/');
            $("#search-form").submit();
        }
    });
    $("#appraise-button").click(function() {
        if (checkSubmitReady()) {
            $("#search-form").attr('action', '/');
            $("#search-form").submit();
        }
    });

    /* set label colors */
    $(".offset-label").each(function(){
        var id = $(this).attr('id');
        var num = $(this).html();
        if (parseInt($(this).html(), 10) > 100) {
            $(this).addClass("label label-danger");
            $(this).html("Overpriced by " + (num - 100) + "%");
        } else {
            $(this).addClass("label label-success");
            $(this).html("Underpriced by " + (100 - num) + "%");
        } 
        $(this).attr("title", num);
    });

    /* add custom sort by title attribute */
    jQuery.fn.dataTableExt.oSort['title-numeric-asc']  = function(a,b) {
        var x = a.match(/title="*(-?[0-9\.]+)/)[1];
        var y = b.match(/title="*(-?[0-9\.]+)/)[1];
        x = parseFloat( x );
        y = parseFloat( y );
        return ((x < y) ? -1 : ((x > y) ?  1 : 0));
    };
    jQuery.fn.dataTableExt.oSort['title-numeric-desc'] = function(a,b) {
            var x = a.match(/title="*(-?[0-9\.]+)/)[1];
                var y = b.match(/title="*(-?[0-9\.]+)/)[1];
                    x = parseFloat( x );
                        y = parseFloat( y );
                            return ((x < y) ?  1 : ((x > y) ? -1 : 0));
    };

    /* datatables */
    $("#similar_table").dataTable({
        "aaSorting": [[ 3, "asc" ]],
        "aoColumns": [
                        null,
                        null,
                        null,
                        { "sType": "title-numeric" },
                    ]
    });

});
