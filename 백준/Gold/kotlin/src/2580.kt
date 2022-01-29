fun sudokuCheck(num: Int, board: MutableList<MutableList<Int>>, r: Int, c: Int): Boolean {
    if (num in board[r]) {
        return false
    }
    for (i in 0 until 9) {
        if (num == board[i][c]) {
            return false
        }
    }
    var squareRowIdx = (r / 3) * 3
    var squareColIdx = (c / 3) * 3
    for (i in squareRowIdx until squareRowIdx+3) {
        for (j in squareColIdx until squareColIdx+3) {
            if (num == board[i][j]) {
                return false
            }
        }
    }
    return true
}

fun sudoku(board: MutableList<MutableList<Int>>, blanks: MutableList<Array<Int>>, idx: Int): Boolean {
    if (idx == blanks.size) {
        for (i in 0 until 9) {
            println(board[i].joinToString(" "))
        }
        return true
    }
    val r = blanks[idx][0]
    val c = blanks[idx][1]
    for (k in 1..9) {
        if (sudokuCheck(k, board, r, c)) {
            board[r][c] = k
            if (sudoku(board, blanks, idx+1)) {
                return true
            }
            board[r][c] = 0
        }
    }
    return false
}

fun main() = with(System.`in`.bufferedReader()) {
    var board = mutableListOf<MutableList<Int>>()
    var line: MutableList<Int>
    var blanks = mutableListOf<Array<Int>>()
    for (i in 0 until 9) {
        line = readLine().split(" ").map { num -> num.toInt()}.toMutableList()

        for (j in 0 until 9) {
            if (line[j] == 0) {
                blanks.add(arrayOf(i, j))
            }
        }

        board.add(line)
    }

    val x = sudoku(board, blanks, 0)
}