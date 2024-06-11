// -------------- Class 41 -----------------
const image_drop_area_class41 = document.querySelector("#image_drop_area_class55");
var uploaded_image_class55;

// Event listener for dragging the image over the div
image_drop_area_class55.addEventListener('dragover', (event) => {
  event.stopPropagation();
  event.preventDefault();
  // Style the drag-and-drop as a "copy file" operation.
  event.dataTransfer.dropEffect = 'copy';
});

// Event listener for dropping the image inside the div
image_drop_area_class55.addEventListener('drop', (event) => {
  event.stopPropagation();
  event.preventDefault();
  fileList = event.dataTransfer.files;

  document.querySelector("#file_name_class55").textContent = fileList[0].name;
  
  readImage_class55(fileList[0]);
});

// Converts the image into a data URI
readImage_class55 = (file) => {
  const reader = new FileReader();
  reader.addEventListener('load', (event) => {
    uploaded_image_class55 = event.target.result;
    document.querySelector("#image_drop_area_class55").style.backgroundImage = `url(${uploaded_image_class55})`;
	var formData = new FormData();
	formData.append('file', file);
	$.ajax({
		   url : 'https://api-ai-food.coecore.com/class55',
		   type : 'POST',
		   data : formData,
		   processData: false,  // tell jQuery not to process the data
		   contentType: false,  // tell jQuery not to set contentType
		   timeout: 10000,
		   success : function(data) {
			   console.log(data);
			   document.querySelector("#result_class55").value = JSON.stringify(data);
		   }
	});
  });
  reader.readAsDataURL(file);
}
