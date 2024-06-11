$client = new-object System.Net.WebClient
$CUR_DIR = Get-Location
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip'
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/4G-EfficientNetB5-epoch2000.pb.zip",($CUR_DIR.Path+"\4G-EfficientNetB5-epoch2000.pb.zip"))
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip'
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/41CLASSES-EfficientNetB5-epoch2000.pb.zip",($CUR_DIR.Path+"\41CLASSES-EfficientNetB5-epoch2000.pb.zip"))
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip'
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip",($CUR_DIR.Path+"\10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip"))
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/yolo_v4_41CLASSES.zip'
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/yolo_v4_41CLASSES.zip",($CUR_DIR.Path+"\yolo_v4_41CLASSES.zip"))
echo 'Loading Model from https://assets.gezdev.com/model-ai/medical-waste/yolo_v5_41CLASSES.zip'
$client.DownloadFile("https://assets.gezdev.com/model-ai/medical-waste/yolo_v5_41CLASSES.zip",($CUR_DIR.Path+"\yolo_v5_41CLASSES.zip"))
echo 'Model Unzipping..................'
Expand-Archive -Path 4G-EfficientNetB5-epoch2000.pb.zip -DestinationPath ./
Expand-Archive -Path 41CLASSES-EfficientNetB5-epoch2000.pb.zip  -DestinationPath ./
Expand-Archive -Path 10FreqCLASSES-EfficientNetB5-epoch1000.pb.zip  -DestinationPath ./
Expand-Archive -Path yolo_v4_41CLASSES.zip  -DestinationPath ./
ls
echo ('Model Saved at ...' + $CUR_DIR.Path)
echo '++++++++++ [Load/Extract Model] Completed ++++++++++'