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

// 이벤트 등록
canvas.addEventListener("mousedown", startDrawing);
canvas.addEventListener("mouseup", stopDrawing);
canvas.addEventListener("mouseout", stopDrawing);
canvas.addEventListener("mousemove", draw);

canvas.addEventListener("touchstart", startDrawing);
canvas.addEventListener("touchend", stopDrawing);
canvas.addEventListener("touchcancel", stopDrawing);
canvas.addEventListener("touchmove", draw);

// 지우기
function clearCanvas() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "white";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
}

// 이미지 저장
function downloadImage() {
  const link = document.createElement('a');
  link.download = 'digit.png';
  link.href = canvas.toDataURL();
  link.click();
}
