from ultralytics import YOLO

# model = YOLO('yolov8x')
model = YOLO('C:/Users/henri/PROJETO_PDI/PDI_PROJECT/training/runs/detect/modelv3/weights/best.pt')

results = model.predict('C:/Users/henri/PROJETO_PDI/PDI_PROJECT/input_video/08fd33_4.mp4', save=True)


print(results[0])
print('======================================')

for box in results[0].boxes:
    print(box)
