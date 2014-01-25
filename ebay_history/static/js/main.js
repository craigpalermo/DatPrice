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
});
