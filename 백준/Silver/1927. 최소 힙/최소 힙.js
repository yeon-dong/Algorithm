const [N, ...arr] = require("fs").readFileSync(0).toString().trim().split("\n").map(Number);

class MinHeap {
  constructor() {
    this.heap = [];
  }

  heapifyUp(index) {
    const parentIndex = Math.floor((index - 1) / 2);
    if (parentIndex >= 0 && this.heap[index] < this.heap[parentIndex]) {
      [this.heap[index], this.heap[parentIndex]] = [this.heap[parentIndex], this.heap[index]];
      this.heapifyUp(parentIndex);
    }
  }

  heapifyDown(index) {
    const len = this.heap.length;
    let smallest = index;
    const leftChild = 2 * index + 1;
    const rightChild = 2 * index + 2;

    if (leftChild < len && this.heap[leftChild] < this.heap[smallest]) {
      smallest = leftChild;
    }

    if (rightChild < len && this.heap[rightChild] < this.heap[smallest]) {
      smallest = rightChild;
    }

    if (smallest !== index) {
      [this.heap[smallest], this.heap[index]] = [this.heap[index], this.heap[smallest]];
      this.heapifyDown(smallest);
    }
  }

  insert(value) {
    this.heap.push(value);
    this.heapifyUp(this.heap.length - 1);
    
  }

  extractMin() {
    if (this.heap.length === 0) {
      return null;
    }
    
    const min = this.heap[0];
    const lastIdx = this.heap.length - 1;
    this.heap[0] = this.heap[lastIdx];
    this.heap.pop();
    this.heapifyDown(0);

    return min;
  }

  length(){
    return this.heap.length;
  }

}

const minHeap = new MinHeap;
const result = [];

for(let i = 0; i < N; i++){
  if(arr[i] == 0){
    if(minHeap.length() == 0){
      result.push(0);
    }else{
      result.push(minHeap.extractMin());
    }
  }else{
    minHeap.insert(arr[i]);
  }
}

console.log(result.join("\n"));
