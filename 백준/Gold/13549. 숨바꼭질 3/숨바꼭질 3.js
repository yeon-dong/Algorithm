const [N, K] = require("fs")
  .readFileSync(0)
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const queue = [];
queue.push([N,0]);
const visited = new Array(100002).fill(0);
while (queue.length) {
  const [now, time] = queue.shift();
  if (now === K) {console.log(time); break;}
  for (next of [now * 2, now - 1, now + 1]) {
    if (!visited[next] && next >= 0 && next <= 100000) {
      visited[next] = 1;
      if (next == now * 2) {
        queue.unshift([next, time]); // 2X로 이동할 때는 시간을 증가시키지 않고, 우선순위를 반영하여 큐의 맨 앞에 넣어준다.
      } else {
        queue.push([next, time + 1]); // X-1, X+1로 이동할 때는 시간을 증가시키고, 큐에 순서대로 넣어준다.
      }
    }
  }
}


// class Node{
//   constructor(value){
//     this.value = value;
//     this.next = null;
//   }
// }

// class Queue{
//   constructor(){
//     this.front = null;
//     this.rear = null;
//     this.length = 0;
//   }

//   push(value){ //요소 추가
//     const newNode = new Node(value);
//     if(!this.front){ // 큐가 비어있다면
//       this.front = this.rear = newNode;
//     }else{
//       this.rear.next = newNode;
//       this.rear = newNode;
//     }
//     this.length++;
//   }

//   shift(){
//     if (!this.front) return null;  // 큐가 비어있다면 null 반환
//     const dequeuedValue = this.front.value;
//     this.front = this.front.next;
//     if (!this.front) this.rear = null; // 큐가 비었다면 rear도 null 처리
//     this.length--;
//     return dequeuedValue;
//   }

//   frontPush(value){
//     const newNode = new Node(value);
//     if(!this.front){ // 큐가 비어있다면
//       this.front = this.rear = newNode;
//     }else{
//       const nextNode = this.front;
//       this.front = newNode;
//       this.front.next = nextNode;
//     }
//     this.length++;
//   }
// }

// const queue = new Queue;
// const visited = new Array(100002).fill(0);
// queue.push(N);
// while(true){
//   const now = queue.shift();
//   if(now == K){
//     console.log(visited[now]);
//     break;
//   }
//   for(let i of [now-1,now+1]){
//     if(i >= 0 && i < 100000 && !visited[i]){
//       queue.push(i);
//       visited[i] = visited[now] + 1;
//     }
//   }
//   if(now * 2 > 0 && now * 2 < 100000 && !visited[now * 2]){
//     queue.frontPush(now * 2);
//     visited[now * 2] = visited[now];
//   }
// }