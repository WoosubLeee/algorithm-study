fun main() = with(System.`in`.bufferedReader()) {
    val n = readLine().toInt()
    val amounts = mutableListOf<Int>()
    for (i in 1..n) {
        amounts.add(readLine().toInt())
    }

    when (n) {
        1 -> {
            print(amounts[0])
        }
        2 -> {
            print(amounts[0] + amounts[1])
        }
        else -> {
            val result = mutableListOf(
                arrayOf(amounts[0], 0),
                arrayOf(amounts[1], amounts[1] + amounts[0]),
                arrayOf(amounts[2] + amounts[0], amounts[2] + amounts[1])
            )

            for (i in 3 until n) {
                result.add(arrayOf(
                    amounts[i] + intArrayOf(result[i-2].maxOrNull()!!, result[i-3].maxOrNull()!!).maxOrNull()!!,
                    amounts[i] + result[i-1][0]
                ))
            }
            print(intArrayOf(result[n-1].maxOrNull()!!, result[n-2].maxOrNull()!!, result[n-3].maxOrNull()!!).maxOrNull())
        }
    }
}