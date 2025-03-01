[number,...arr] = require("fs").readFileSync("/dev/stdin").toString().trim().split("\n");
number = number.trim().split(" ").map(Number);
const N = number[0];
const M = number[1];
const min_arr = [];
arr = arr.map(row => row.trim());

//하얀색이 먼저 시작하는 판
const white = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
  ];
  
  //검은색이 먼저 시작하는 판
  const black = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
  ];
  
  //하얀색이 먼저 시작하는 판과 비교하여 다르다면 count
  function whiteFirst(x, y) {
    let count = 0;

    for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
        if (arr[i + x][j + y] !== white[i][j]) count++;
      }
    }
    return count;
  }
  
  //검은색이 먼저 시작하는 판과 비교하여 다르다면 count
  function blackFirst(x, y) {
    let count = 0;
    for (let i = 0; i < 8; i++) {
      for (let j = 0; j < 8; j++) {
        if (arr[i + x][j + y] !== black[i][j]) count++;
      }
    }
    return count;
  }
  
  //전체 판을 움직이는 형태로 작성했기에, -7을 해줌으로써 전체 판을 벗어나지 않게 해준다.
  for (let k = 0; k < N - 7; k++) {
    for (let l = 0; l < M - 7; l++) {
        min_arr.push(whiteFirst(k, l));
        min_arr.push(blackFirst(k, l));
    }
  }
  console.log(Math.min(...min_arr));