/* set the active tab navigation based on url path */
$(function() {
  $('#tab-navigation .nav-item a').each(function() {
    var href = $(this).attr('href')
    var path = location.pathname
    var match = href === path || href.substring(1) === path.substring(1)
    if (match) {
      $(this).addClass('active text-success');
    } else {
      $(this).addClass('text-dark')
    }
  });
})
