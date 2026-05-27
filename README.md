# YOLO 目标检测学习项目

大二机器人工程专业，之前做过嵌入式小车和无人机，这次想往软件方向拓展，学习计算机视觉相关的内容。

## 环境

- macOS (Apple M4)
- Python 3.9
- OpenCV 4.13.0
- Ultralytics (YOLOv8)

## 安装

```bash
pip install -r requirements.txt
```

第一次运行 `yolo_demo.py` 时会自动下载 YOLOv8 模型文件（约 6MB）。

## 文件说明

| 文件 | 功能 |
|------|------|
| `opencv_demo.py` | 摄像头实时画面，按 `g` 切换灰度/彩色，按 `q` 退出 |
| `yolo_demo.py` | YOLOv8 实时目标检测，能识别 80 种常见物体，按 `q` 退出 |
| `requirements.txt` | Python 依赖 |

## 使用过程

### 1. OpenCV 基础 — 摄像头调用

先从最基础的开始，用 OpenCV 打开摄像头，实时显示画面。加了一个灰度切换功能，熟悉 OpenCV 的基本操作：

```bash
python opencv_demo.py
```

核心就三行代码：`VideoCapture(0)` 打开摄像头，`cap.read()` 读帧，`imshow()` 显示。

### 2. YOLO 实时目标检测

在 OpenCV 的基础上接入 YOLO 模型，实现摄像头画面的实时物体检测：

```bash
python yolo_demo.py
```

流程是：摄像头读一帧 → YOLO 模型推理 → 在画面上画检测框 → 显示。用的是 YOLOv8s 模型，M4 芯片跑起来很流畅。

### 3. 模型选择

YOLOv8 有多个版本，按大小排序：

| 模型 | 大小 | 特点 |
|------|------|------|
| yolov8n | 6MB | 最快，精度最低 |
| yolov8s | 22MB | 速度快，精度适中（当前使用） |
| yolov8m | 50MB | 平衡 |
| yolov8l | 84MB | 较慢，精度较高 |
| yolov8x | 131MB | 最慢，精度最高 |

换模型只需要改一行：`model = YOLO("yolov8m.pt")`，首次运行自动下载。

## 后续计划

- [ ] 自定义数据集训练，识别特定物体
- [ ] 加入 AprilTag 识别，做机器人定位
- [ ] 结合之前的无人机项目，做视觉追踪
