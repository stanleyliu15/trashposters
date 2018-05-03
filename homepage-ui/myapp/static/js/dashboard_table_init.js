$(document).ready(function () {

  var STATUS_COL_INDEX = 5
  var DELETE_COL_INDEX = 6

  $('#dashboard-table-posts').DataTable({
    "columnDefs": [
      { orderable: false, targets: [STATUS_COL_INDEX, DELETE_COL_INDEX] }
    ]
  });

  $('#dashboard-table-users').DataTable();
})