const fs = require('fs');
const [N,K] = fs.readFileSync("./dev/stdin").toString().trim().split(" ").map(v=>+v);
class Node{
  constructor(item){
    this.item = item;
    this.next = null;
  }
}

class Queue{
constructor(){
  this.head = null; 
  this.tail = null; 
  // this.length = 0; 
}

push(item){
  const node = new Node(item);
  if(this.head==null){
    this.head = node;
  }else{
    this.tail.next = node;
  }

  this.tail = node; 
  // this.length +=1; 
}

pop(){
  const popItem = this.head;
  this.head = this.head.next; 
  // this.length -=1; 
  return popItem.item; 
}
}

function check(n){
  return !isVisited[n]
}



let answer = 0;
let isVisited = new Array(100001).fill(false);


let q = new Queue();
q.push([N,0]);
isVisited[N] = true;

while(true){
  let [now,sec] = q.pop();
  if(now==K){
    answer = sec;
    break; 
  }else{
    if(now-1>=0 && check(now-1)){
      isVisited[now-1] = true; 
      q.push([now-1,sec+1])
    }
    if(now+1<100001 && check(now+1)){
      isVisited[now+1] = true; 
      q.push([now+1,sec+1])
    }
    if(now*2<100001 && check(now*2)){
      isVisited[now*2] = true; 
      q.push([now*2,sec+1])
    }
  }
}

console.log(answer)