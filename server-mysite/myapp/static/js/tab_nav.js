/* set the active tab navigation based on url */
$(function() {
  if (location.pathname == '/') {
      $('#tab-navigation .nav-item a[href="/"').addClass('active')
  } else {
      $('#tab-navigation .nav-item a[href^="/' + location.pathname.substring(1) + '"]').addClass('active');
  }
})
