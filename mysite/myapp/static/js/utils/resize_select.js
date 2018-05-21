// Whenever a option is selected in a select element,
// This script will resize the width of to match
// the length of the option element's text
// requires the id attribute on select element for uniqueness
$(document).ready(function() {
  $(".resize-select").each(function() {
    var id = $(this).attr("id")
    if(id === undefined) { console.log("Id attribute was not found for select element") }

    // create temp elements
    var $tempSelect = $("<select></select>", { "id": id + "_tmp_select" })
    var $tempOption = $("<option></option>", { "id": id + "_tmp_option" })

    // add temp elements to page and hide
    $tempOption.appendTo($tempSelect)
    $tempSelect.appendTo($("body"))
    $tempSelect.hide()

    // dyanmically resize the select element on change
    $(this).change(function() {
      $tempOption.html($(this).find("option:selected").text())
      $(this).width(Math.round($tempSelect.width(), 1))
    }).change()
  })
})
