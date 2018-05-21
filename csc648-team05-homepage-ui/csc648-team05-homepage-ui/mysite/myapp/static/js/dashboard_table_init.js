$(document).ready(function () {

  var STATUS_COL_INDEX = 5
  var DELETE_COL_INDEX = 6

  $("#dashboard-table-posts").DataTable({
    "columnDefs": [{ orderable: false, targets: [STATUS_COL_INDEX, DELETE_COL_INDEX] }]
  });

  $("#dashboard-table-users").DataTable();

  /* Customize the look of the select menu */
  customizeSelectMenuLook();
})

/*
  DataTable generates a default select menu for show number of entries ,
  This function simply adds custom styles to that element
*/
function customizeSelectMenuLook() {
  var $users_length = $("#dashboard-table-users_length label select")
  var $posts_length = $("#dashboard-table-posts_length label select")

  $users_length.css("width", "auto")
  $posts_length.css("width", "auto")

  if (navigator.userAgent.indexOf("Firefox") != -1) {
    $users_length.addClass("py-0")
    $posts_length.addClass("py-0")
  }

  $users_length.addClass("custom-select h-100")
  $posts_length.addClass("custom-select h-100")
}