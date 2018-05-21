$(document).ready(function() {
  // Updates the text of dropdown toggle button
  // when user clicks on dropdown item
  $(".dropdown-menu .dropdown-item").click(function() {
    // update the 'selected' class attribute
    $(this).parent().find(".selected").removeClass("selected")
    $(this).addClass("selected")

    // update the toggle display text
    var $toggleButton = $(this).parent().siblings(".dropdown-toggle")
    var selectedText = $(this).text() + " "
    $toggleButton.html(selectedText)
  })
})
