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
    var table = document.getElementById("fake-table");
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
        text: "Value Over Time"              
      },
      data: [//array of dataSeries              
        { //dataSeries object

         /*** Change type "column" to "bar", "area", "line" or "pie"***/
         type: "column",
         dataPoints: tempData
        } 
            ]
     });
 
    chart.render();
  }
});
