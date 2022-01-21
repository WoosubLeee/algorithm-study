import kotlin.math.round

fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()

    var total = 0
    var maxNum = -4000
    var minNum = 4000
    val nums = mutableListOf<Int>()
    val counts = IntArray(8001) { 0 }
    var num: Int
    for (i in 0 until N) {
        num = readLine().toInt()
        total += num
        if (num > maxNum) maxNum = num
        if (num < minNum) minNum = num
        nums.add(num)
        counts[num+4000]++
    }

    // 산술평균
    println(round((total.toDouble() / N)).toInt())

    val maxCount = counts.maxOrNull()
    val maxIdx = counts.mapIndexed { i, v -> if (v == maxCount) i else null }.filterNotNull().toMutableList()
    if (maxIdx.size >= 2) {
        maxIdx[0] = maxIdx[1]
    }

    for (i in 0..8000) {
        if (counts[i] > N/2) {
            // 중앙값
            println(i-4000)
            break
        }
        counts[i+1] += counts[i]
    }

    // 최빈값
    println(maxIdx[0]-4000)

    // 범위
    print(maxNum - minNum)
}