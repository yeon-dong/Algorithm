const [N, K] = require("fs")
  .readFileSync(0)
  .toString()
  .trim()
  .split(" ")
  .map(Number);


class Node{
  constructor(value){
    this.value = value;
    this.next = null;
  }
}

class Queue{
  constructor(){
    this.front = null;
    this.rear = null;
    this.length = 0;
  }

  push(value){ //요소 추가
    const newNode = new Node(value);
    if(!this.front){ // 큐가 비어있다면
      this.front = this.rear = newNode;
    }else{
      this.rear.next = newNode;
      this.rear = newNode;
    }
    this.length++;
  }

  shift(){
    if (!this.front) return null;  // 큐가 비어있다면 null 반환
    const dequeuedValue = this.front.value;
    this.front = this.front.next;
    if (!this.front) this.rear = null; // 큐가 비었다면 rear도 null 처리
    this.length--;
    return dequeuedValue;
  }

  unshift(value){
    const newNode = new Node(value);
    if(!this.front){ // 큐가 비어있다면
      this.front = this.rear = newNode;
    }else{
      const nextNode = this.front;
      this.front = newNode;
      this.front.next = nextNode;
    }
    this.length++;
  }

  length(){
    return this.length;
  }
}

const queue = new Queue;
const visited = new Array(100002).fill(false);
queue.push([N,0]);
while(queue.length){
  const [now, time] = queue.shift();
  if(now == K){
    console.log(time);
    break;
  }
  if(now * 2 > 0 && now * 2 <= 100000 && !visited[now * 2]){
    visited[now * 2] = true;
    queue.unshift([now * 2, time]);
  }
  for(i of [now-1,now+1]){
    if(i >= 0 && i <= 100000 && !visited[i]){
      visited[i] = true;
      queue.push([i,time + 1]);
    }
  }
}