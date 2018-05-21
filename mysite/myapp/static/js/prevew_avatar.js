$(document).ready(function() {

  // Update the preview avatar whenever
  // preset avatar is clicked
  $(".preset-avatar").click(function(e) {
    var src = $(this).attr("src")
    $("#preview-avatar").attr("src", src)
  })

  // Update the preview avatar whenever
  // user uploads an image
  $("#avatarupload").change(function(e) {
      var reader = new FileReader();
      reader.onload = function(e) { $("#preview-avatar").attr("src", reader.result);}
      reader.readAsDataURL(e.target.files[0]);
  })

  // Whenever modal is closed
  // reset the preview avatar (of the modal) to the current avatar
  $(".close, [data-dismiss='modal']").click(function(e) {
    $("#preview-avatar").attr("src", $("#avatar").attr("src"))
  })

})