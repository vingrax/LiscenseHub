document.addEventListener("DOMContentLoaded", (event) => {
    var addmodal = document.getElementById("assign-license-modal");
    var removemodal = document.getElementById('remove-license-modal');
    var addbtn = document.getElementById("assign-license-btn");
    var removebtn = document.getElementById("remove-license-btn");
    var devicetable = new DataTable('#myTable', {
      "paging": false
    });
    var historyTable = new DataTable('#history-table', {
      "paging": false
    });


    addbtn.onclick = function() {
      addmodal.style.display = "block";
    }

    removebtn.onclick = function() {
        removemodal.style.display = "block";
      }
   

    window.onclick = function(event) {
      if (event.target == addmodal || event.target == removemodal) {
        addmodal.style.display = "none";
        removemodal.style.display = "none";
      }
    }
  });
  


  

    