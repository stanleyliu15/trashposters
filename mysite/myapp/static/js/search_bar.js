$(document).ready(function() {




//submits search when enter is pressed
$('#query').keypress(function(e){
	if(e.which == 13)
		search();
});



  var BASE_PLACEHOLDER = "Search by "

  // Whenever a new option is selected in search bar select menu,
  // This script will update the placeholder to match the option's text
  // and add 'selected' attribute to the option
  $("#filter-post-select-menu").change(function() {
    var $searchBar = $("#query")
    var $selectedOption = $(".custom-select option:selected")
    var placeholder = BASE_PLACEHOLDER

    // remove old selected option's selected attribute
    $(this).find("option[selected=selected]").attr("selected", false)
    // add selected attribute to the current selected option
    //$("option:selected", this).attr("selected", true)

    // Special case when 'All' option is selected
    // loop over the option's in the select menu
    // placeholder will be the concatenation of the options value
    if($selectedOption.val() === "all" && $selectedOption.index() == 0) {
      var $select = $(this).children("option").not(":first")

      // create placeholder based on each of the option element's value
      $select.each(function(i) {
        if(i == $select.length - 1)
          placeholder += "or " + this.value
        else
          placeholder += this.value + ", "
      })
    }
    // Concatenate placeholder as normal
    else {
      placeholder += $selectedOption.val()
    }

    $searchBar.attr("placeholder", placeholder)
  }).change();
})



function search(){
	var selection = $('#filter-post-select-menu').find(':selected').text().toLowerCase();
	var query = $('#query').val();
	window.location.href = window.location.origin+"/search/"+selection+"="+query;

}


