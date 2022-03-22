import kotlin.math.min

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val matrices = Array(N) { Array(2) { 0 } }

    for (i in 0 until N) {
        val matrix = readLine().split(" ").map { x -> x.toInt() }
        matrices[i][0] = matrix[0]
        matrices[i][1] = matrix[1]
    }

    val dp = Array(N) { Array(N) { 0 } }
    for (i in 1 until N) {
        for (j in i-1 downTo 0) {
            var minCost = Integer.MAX_VALUE

            val tempNewCost = matrices[j][0]*matrices[i][1]
            for (k in 0 until i-j) {
                val prevCost = dp[j][j+k] + dp[j+k+1][i]
                val newCost = tempNewCost*matrices[j+k][1]
                minCost = min(minCost, prevCost+newCost)
            }
            dp[j][i] = minCost
        }
    }

    print(dp[0][N-1])
}