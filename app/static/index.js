if (window.history.replaceState) {
  window.history.replaceState(null, null, window.location.href);
}

function dispimg(ele) {
  document.getElementById("preview").src = window.URL.createObjectURL(
    ele.files[0]
  );
  document.getElementById("submit").style.display = "block";
  document.getElementById("step").innerHTML = "Step 2 : Predict Image";
  document.getElementById("step").style.color = "#60e414";
}
