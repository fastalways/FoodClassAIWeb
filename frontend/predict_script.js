// -------------- Class 41 -----------------
const image_drop_area_class41 = document.querySelector("#image_drop_area_class41");
var uploaded_image_class41;

// Event listener for dragging the image over the div
image_drop_area_class41.addEventListener('dragover', (event) => {
  event.stopPropagation();
  event.preventDefault();
  // Style the drag-and-drop as a "copy file" operation.
  event.dataTransfer.dropEffect = 'copy';
});

// Event listener for dropping the image inside the div
image_drop_area_class41.addEventListener('drop', (event) => {
  event.stopPropagation();
  event.preventDefault();
  fileList = event.dataTransfer.files;

  document.querySelector("#file_name_class41").textContent = fileList[0].name;
  
  readImage_class41(fileList[0]);
});

// Converts the image into a data URI
readImage_class41 = (file) => {
  const reader = new FileReader();
  reader.addEventListener('load', (event) => {
    uploaded_image_class41 = event.target.result;
    document.querySelector("#image_drop_area_class41").style.backgroundImage = `url(${uploaded_image_class41})`;
	var formData = new FormData();
	formData.append('file', file);
	$.ajax({
		   url : 'https://medwaste-api.gezdev.com/class41',
		   type : 'POST',
		   data : formData,
		   processData: false,  // tell jQuery not to process the data
		   contentType: false,  // tell jQuery not to set contentType
		   timeout: 10000,
		   success : function(data) {
			   console.log(data);
			   document.querySelector("#result_class41").value = JSON.stringify(data);
		   }
	});
  });
  reader.readAsDataURL(file);
}


// -------------- Class 4G -----------------


const image_drop_area_class4G = document.querySelector("#image_drop_area_class4G");
var uploaded_image_class4G;

// Event listener for dragging the image over the div
image_drop_area_class4G.addEventListener('dragover', (event) => {
  event.stopPropagation();
  event.preventDefault();
  // Style the drag-and-drop as a "copy file" operation.
  event.dataTransfer.dropEffect = 'copy';
});

// Event listener for dropping the image inside the div
image_drop_area_class4G.addEventListener('drop', (event) => {
  event.stopPropagation();
  event.preventDefault();
  fileList = event.dataTransfer.files;

  document.querySelector("#file_name_class4G").textContent = fileList[0].name;
  
  readImage_class4G(fileList[0]);
});

// Converts the image into a data URI
readImage_class4G = (file) => {
  const reader = new FileReader();
  reader.addEventListener('load', (event) => {
    uploaded_image_class4G = event.target.result;
    document.querySelector("#image_drop_area_class4G").style.backgroundImage = `url(${uploaded_image_class4G})`;
	var formData = new FormData();
	formData.append('file', file);
	$.ajax({
		   url : 'https://medwaste-api.gezdev.com/class4G',
		   type : 'POST',
		   data : formData,
		   processData: false,  // tell jQuery not to process the data
		   contentType: false,  // tell jQuery not to set contentType
		   timeout: 10000,
		   success : function(data) {
			   console.log(data);
			   document.querySelector("#result_class4G").value = JSON.stringify(data);
		   }
	});
  });
  reader.readAsDataURL(file);
}

// -------------- Detect 41 by YoloV4 -----------------
// -------------- Class 41 -----------------
const image_drop_area_yolov4_41 = document.querySelector("#image_drop_area_yolov4_41");
var uploaded_image_yolov4_41;

// Event listener for dragging the image over the div
image_drop_area_yolov4_41.addEventListener('dragover', (event) => {
  event.stopPropagation();
  event.preventDefault();
  // Style the drag-and-drop as a "copy file" operation.
  event.dataTransfer.dropEffect = 'copy';
});

// Event listener for dropping the image inside the div
image_drop_area_yolov4_41.addEventListener('drop', (event) => {
  event.stopPropagation();
  event.preventDefault();
  fileList = event.dataTransfer.files;

  document.querySelector("#file_name_yolov4_41").textContent = fileList[0].name;
  
  readImage_yolov4_41(fileList[0]);
});

// Converts the image into a data URI
readImage_yolov4_41 = (file) => {
  const reader = new FileReader();
  reader.addEventListener('load', (event) => {
    uploaded_image_yolov4_41 = event.target.result;
    document.querySelector("#image_drop_area_yolov4_41").style.backgroundImage = `url(${uploaded_image_yolov4_41})`;
	var formData = new FormData();
	formData.append('file', file);
	$.ajax({
		   url : 'https://medwaste-api.gezdev.com/yolov4_41',
		   type : 'POST',
		   data : formData,
		   processData: false,  // tell jQuery not to process the data
		   contentType: false,  // tell jQuery not to set contentType
		   timeout: 10000,
		   success : function(data) {
			   console.log(data);
         res_json = JSON.stringify(data);
			   document.querySelector("#result_yolov4_41").value = data;
         var resObj = JSON.parse(data);
         var result_path = Object.keys(resObj)[0];
         document.querySelector("#file_name_yolov4_41").innerHTML = "<a href='"+result_path+"' target='_blank'>"+result_path+'</a>';
		   }
	});
  });
  reader.readAsDataURL(file);
}