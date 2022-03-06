import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val token = StringTokenizer(readLine())
    var A = token.nextToken().toLong()
    var B = token.nextToken().toLong()
    val C = token.nextToken().toLong()

    A %= C
    val numMap = mutableMapOf(1L to A)
    val result = dnq(B, C, numMap)

    print(result)
}

fun dnq(b: Long, C:Long, numMap: MutableMap<Long, Long>): Long {
    if (numMap.containsKey(b)) {
        return numMap.get(b)!!
    } else {
        val half = b / 2
        val calc = (dnq(half, C, numMap) * dnq(b - half, C, numMap)) % C
        numMap[b] = calc
        return calc
    }
}