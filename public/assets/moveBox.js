let effectBox;

window.addEventListener("load", () => {
  effectBox = document.getElementById("effectBox");

  let startX = 0;
  let startY = 0;
  let isMoving = false;

  effectBox.addEventListener("mousedown", (e) => {
    if (e.target.nodeName !== "INPUT") {
      isMoving = true;
      startX = e.pageX - effectBox.offsetLeft;
      startY = e.pageY - effectBox.offsetTop;
    }
  });

  document.addEventListener("mouseup", (e) => {
    isMoving = false;
  });

  document.addEventListener("mousemove", (e) => {
    if (isMoving) {
      effectBox.style.left = e.pageX - startX + "px";
      effectBox.style.top = e.pageY - startY + "px";
    }
  });
});
