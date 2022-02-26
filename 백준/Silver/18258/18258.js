const readline = require('readline')

const rl = readline.createInterface({
  input: process.stdin
})

let N
let count = 0
const stack = []
let front = -1, rear = -1
let result = []
rl.on('line', line => {
  if (!N) N = parseInt(line)
  else {
    switch (line) {
      case 'pop':
        if (front !== rear) {
          front++
          result.push(stack[front])
        } else {
          result.push(-1)
        }
        break
      case 'size':
        result.push(rear - front)
        break
      case 'empty':
        if (front === rear) result.push(1)
        else result.push(0)
        break
      case 'front':
        if (front !== rear) result.push(stack[front+1])
        else result.push(-1)
        break
      case 'back':
        if (front !== rear) result.push(stack[rear])
        else result.push(-1)
        break
      default:
        const num = parseInt(line.split(' ')[1])
        stack.push(num)
        rear++
    }

    count++
    if (count === N) rl.close()
  }
}).on('close', () => {
  console.log(result.join('\n'))
})