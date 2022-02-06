import kotlin.math.max

fun main() = with(System.`in`.bufferedReader()) {
    val strA = readLine().toString()
    val strB = readLine().toString()

    // 1 쉽게 푼 방법
    val dp = Array(strA.length + 1) { IntArray(strB.length + 1) }

    for (i in 1..strA.length) {
        for (j in 1..strB.length) {
            if (strA[i-1] != strB[j-1]) {
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
            } else {
                dp[i][j] = dp[i-1][j-1] + 1
            }
        }
    }
    print(dp[strA.length][strB.length])


//    // 2 어렵게 푼 방법
//    val counts = mutableListOf<Int>()
//
//    var last: Int
//    var start: Int
//    var bIdxs: MutableList<Int>
//    var bIdx: Int
//
//    var l: Int
//    var r: Int
//    var m: Int
//    for (i in strA.indices) {
//        if (counts.isNotEmpty()) {
//            last = counts.last()
//        } else {
//            last = -1
//        }
//        bIdx = strB.indexOf(strA[i], last + 1)
//        if (bIdx != -1) {
//            counts.add(bIdx)
//        }
//
//        start = 0
//        bIdxs = mutableListOf()
//        while (true) {
//            bIdx = strB.indexOf(strA[i], start)
//            if (bIdx >= last || bIdx == -1) {
//                break
//            } else {
//                bIdxs.add(bIdx)
//            }
//            start = bIdx + 1
//        }
//
//        for (idx in bIdxs.reversed()) {
//            l = 0
//            r = counts.size - 1
//            while (l <= r) {
//                m = (l + r) / 2
//                if (counts[m] == idx) {
//                    break
//                } else if (counts[m] > idx) {
//                    r = m - 1
//                } else {
//                    l = m + 1
//                }
//            }
//            if (l > r) {
//                counts[l] = idx
//            }
//        }
//    }
//
//    print(counts.size)
}