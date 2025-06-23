// const canvas = document.getElementById('canvas');
// const ctx = canvas.getContext('2d');
// let drawing = false;

// // 초기 배경 흰색
// ctx.fillStyle = "white";
// ctx.fillRect(0, 0, canvas.width, canvas.height);
// ctx.lineWidth = 15;
// ctx.lineCap = "round";
// ctx.strokeStyle = "black";

// const startDrawing = (e) => {
//   drawing = true;
//   draw(e);
// };

// const stopDrawing = () => {
//   drawing = false;
//   ctx.beginPath();
// };

// const draw = (e) => {
//   if (!drawing) return;

//   const rect = canvas.getBoundingClientRect();
//   const x = (e.touches ? e.touches[0].clientX : e.clientX) - rect.left;
//   const y = (e.touches ? e.touches[0].clientY : e.clientY) - rect.top;

//   ctx.lineTo(x, y);
//   ctx.stroke();
//   ctx.beginPath();
//   ctx.moveTo(x, y);
// };

// // 이벤트 등록
// canvas.addEventListener("mousedown", startDrawing);
// canvas.addEventListener("mouseup", stopDrawing);
// canvas.addEventListener("mouseout", stopDrawing);
// canvas.addEventListener("mousemove", draw);

// canvas.addEventListener("touchstart", startDrawing);
// canvas.addEventListener("touchend", stopDrawing);
// canvas.addEventListener("touchcancel", stopDrawing);
// canvas.addEventListener("touchmove", draw);

// // 지우기
// function clearCanvas() {
//   ctx.clearRect(0, 0, canvas.width, canvas.height);
//   ctx.fillStyle = "white";
//   ctx.fillRect(0, 0, canvas.width, canvas.height);
// }

// // 이미지 저장
// function downloadImage() {
//   const link = document.createElement('a');
//   link.download = 'digit.png';
//   link.href = canvas.toDataURL();
//   link.click();
// }

const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');
let drawing = false;

// 초기 배경 흰색
ctx.fillStyle = "white";
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.lineWidth = 15;
ctx.lineCap = "round";
ctx.strokeStyle = "black";

const startDrawing = (e) => {
  drawing = true;
  draw(e);
};

const stopDrawing = () => {
  drawing = false;
  ctx.beginPath();
};

const draw = (e) => {
  if (!drawing) return;

  const rect = canvas.getBoundingClientRect();
  const x = (e.touches ? e.touches[0].clientX : e.clientX) - rect.left;
  const y = (e.touches ? e.touches[0].clientY : e.clientY) - rect.top;

  ctx.lineTo(x, y);
  ctx.stroke();
  ctx.beginPath();
  ctx.moveTo(x, y);
};

canvas.addEventListener("mousedown", startDrawing);
canvas.addEventListener("mouseup", stopDrawing);
canvas.addEventListener("mouseout", stopDrawing);
canvas.addEventListener("mousemove", draw);

canvas.addEventListener("touchstart", startDrawing);
canvas.addEventListener("touchend", stopDrawing);
canvas.addEventListener("touchcancel", stopDrawing);
canvas.addEventListener("touchmove", draw);

function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

function downloadImage() {
  const link = document.createElement('a');
  link.download = 'digit.png';
  link.href = canvas.toDataURL();
  link.click();
}

// -------------------------------------------
// TensorFlow.js 모델 불러오기 & 예측

let model = null;

// 모델을 비동기로 미리 불러오기
async function loadModel() {
  try {
    model = await tf.loadLayersModel('./lenet5_mnist.json');
    console.log("모델 로드 완료");
  } catch (e) {
    console.error("모델 로드 실패:", e);
  }
}

loadModel();

// canvas를 28x28 사이즈로 리사이즈하고, 흑백 정규화하여 텐서 생성
function getImageTensor() {
  const tempCanvas = document.createElement('canvas');
  tempCanvas.width = 28;
  tempCanvas.height = 28;
  const tempCtx = tempCanvas.getContext('2d');

  // 원본 canvas를 28x28로 축소
  tempCtx.drawImage(canvas, 0, 0, 28, 28);

  // 이미지 데이터 가져오기
  const imgData = tempCtx.getImageData(0, 0, 28, 28);
  const data = imgData.data;

  const grayScaled = [];

  for (let i = 0; i < data.length; i += 4) {
    // RGB 평균 → 흑백
    let avg = (data[i] + data[i + 1] + data[i + 2]) / 3;
    // 배경이 흰색이라 숫자는 검정 → 255에서 빼서 반전, 0~1 정규화
    grayScaled.push((255 - avg) / 255);
  }

  // Tensor 생성: [batch, height, width, channel]
  return tf.tensor4d(grayScaled, [1, 28, 28, 1]);
}

// Finish 버튼 클릭 시 예측 수행 함수
async function predict() {
  if (!model) {
    alert("모델이 아직 로드되지 않았습니다. 잠시 후 다시 시도하세요.");
    return;
  }

  const inputTensor = getImageTensor();
  const prediction = model.predict(inputTensor);
  const predictionData = prediction.dataSync();

  // 가장 높은 확률과 인덱스 찾기
  let maxProb = 0;
  let maxIndex = 0;
  for (let i = 0; i < predictionData.length; i++) {
    if (predictionData[i] > maxProb) {
      maxProb = predictionData[i];
      maxIndex = i;
    }
  }

  alert(`예측 숫자: ${maxIndex} (확률: ${(maxProb * 100).toFixed(2)}%)`);

  inputTensor.dispose();
  prediction.dispose();
}
