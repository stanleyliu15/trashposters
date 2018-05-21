// Change the color of the status toggle button
// When user clicks on dropdown-item
$(document).ready(function() {
  $(".dropdown-menu .dropdown-item").click(function() {
    var $toggleBtn = $(this).parent().siblings(".dropdown-toggle")
    var statusType = $(this).attr("data-status-type")

    var cls = $toggleBtn.attr("class").match(/btn-[\w]*/)
    if(cls !== null) {
      $toggleBtn.removeClass(cls[0])
    }

    switch(statusType) {
      case "WAIT":
        $toggleBtn.addClass("btn-dark")
        break
      case "PROGRESS":
        $toggleBtn.addClass("btn-secondary")
        break
      case "DONE":
        $toggleBtn.addClass("btn-success")
    }

  })
})
